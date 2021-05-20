import graphene
import os

from graphene_django import DjangoObjectType  # , DjangoListField
from .models import Image
from .aws import s3, bucket, get_s3_client, get_presigned_url, upload_file_to_bucket
from io import BytesIO

module_dir = os.path.dirname(__file__)  # get current directory


class ImageType(DjangoObjectType):
    class Meta:
        model = Image
        fields = "__all__"


class Query(graphene.ObjectType):
    all_images = graphene.List(ImageType)
    img = graphene.Field(ImageType, image_id=graphene.Int())

    def resolve_all_images(self, info, **kwargs):
        return Image.objects.all()

    def resolve_image(self, info, image_id):
        return Image.objects.get(pk=image_id)


class ImageInput(graphene.InputObjectType):
    id = graphene.ID()
    fileurl = graphene.String()
    title = graphene.String()
    datetime = graphene.String()
    location = graphene.String()
    author = graphene.String()
    tags = graphene.String()
    thumbnail = graphene.String()
    video = graphene.Boolean()


class CreateImage(graphene.Mutation):
    class Arguments:
        image_data = ImageInput(required=True)

    image = graphene.Field(ImageType)

    @staticmethod
    def mutate(root, info, image_data=None):
        response = get_presigned_url("2048.jpg")
        print(response)
        filename_to_upload = '2048.jpg'
        file_path = os.path.join(module_dir, filename_to_upload)

        upload_response = upload_file_to_bucket(file_path, response)

        file_url = get_s3_client().generate_presigned_url('put_object', ExpiresIn=60000, Params={'Bucket': "itmimages", 'Key': filename_to_upload})

        print(f"Upload response: {upload_response.status_code}")

        image_instance = Image(
            fileurl = file_url,
            title = image_data.title,
            datetime = image_data.datetime,
            location = image_data.location,
            author = image_data.author,
            tags = image_data.tags,
            thumbnail = image_data.thumbnail,
            video = image_data.video,
        )
        image_instance.save()
        return CreateImage(image=image_instance)


class UpdateImage(graphene.Mutation):
    class Arguments:
        image_data = ImageInput(required=True)

    image = graphene.Field(ImageType)

    @staticmethod
    def mutate(root, info, image_data=None):

        image_instance = Image.objects.get(pk=image_data.id)

        if image_instance:
            image_instance.fileurl = image_data.fileurl
            image_instance.title = image_data.title
            image_instance.datetime = image_data.datetime
            image_instance.location = image_data.location
            image_instance.author = image_data.author
            image_instance.tags = image_data.tags
            image_instance.thumbnail = image_data.thumbnail
            image_instance.video = image_data.video
            image_instance.save()

            return UpdateImage(image=image_instance)
        return UpdateImage(image=None)


class DeleteImage(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    image = graphene.Field(ImageType)

    @staticmethod
    def mutate(root, info, id):
        image_instance = Image.objects.get(pk=id)
        image_instance.delete()

        return None


class Mutation(graphene.ObjectType):
    create_image = CreateImage.Field()
    update_image = UpdateImage.Field()
    delete_image = DeleteImage.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
