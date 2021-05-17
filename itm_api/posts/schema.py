import graphene

from graphene_django import DjangoObjectType  # , DjangoListField
from .models import Image


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
    filename = graphene.String()
    datetime = graphene.String()
    location = graphene.String()
    uploaded_by = graphene.String()
    tags = graphene.String()
    thumbnail = graphene.String()


class CreateImage(graphene.Mutation):
    class Arguments:
        image_data = ImageInput(required=True)

    img = graphene.Field(ImageType)

    @staticmethod
    def mutate(root, info, image_data=None):
        image_instance = Image(
            fileurl = image_data.fileurl,
            datetime = image_data.datetime,
            location = image_data.location,
            uploaded_by = image_data.uploaded_by,
            tags = image_data.tags,
            thumbnail = image_data.thumbnail,
        )
        image_instance.save()
        return CreateImage(image=image_instance)


class UpdateImage(graphene.Mutation):
    class Arguments:
        image_data = ImageInput(required=True)

    img = graphene.Field(ImageType)

    @staticmethod
    def mutate(root, info, image_data=None):

        image_instance = Image.objects.get(pk=image_data.id)

        if image_instance:
            image_instance.fileurl = image_data.fileurl
            image_instance.datetime = image_data.datetime
            image_instance.location = image_data.location
            image_instance.uploaded_by = image_data.uploaded_by
            image_instance.tags = image_data.tags
            image_instance.thumbnail = image_data.thumbnail
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
