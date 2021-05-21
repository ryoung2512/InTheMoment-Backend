[![Actions Status](https://github.com/InTheMoment-App/InTheMoment/workflows/Lint/badge.svg)](https://github.com/InTheMoment-App/InTheMoment/actions)

# InTheMoment-Backend
An app to share pictures and videos anonymously. The content is automatically deleted if they are not liked within a certain period of time.
Backend written in [GraphQL](https://graphql.org/) with [Django](https://www.djangoproject.com/).

## Installation
**Note:** These commands currently assume you are running them in the root of the directory. Assume they only work there!
1. Install [python 3.8](https://www.python.org/downloads/release/python-380/)
2. Ensure you have `pipenv` installed. If not, run `pip install pipenv`.
3. Install the needed packages `pipenv install`.
4. Generate the migrations and apply them `pipenv run generate && pipenv run migrate`
5. Rename `.env.example` in `itm_api` to `.env` and update LOCAL_IP in it with your local ip
6. Run `pipenv run start` to start the server.
7. Visit http://{local-ip}:8000/graphql in your browser
8. Run this example query to make sure it works:
```
query {
  allBooks {
    id
    title
    author
    yearPublished
    review
  }
}
```

## Useful Resources
- [Graphene Documentation](https://docs.graphene-python.org/en/latest/)
- [Building GraphQL APIs in Django Tutorial](https://www.twilio.com/blog/graphql-apis-django-graphene)
- [Advanced Usage of Pipenv](https://pipenv-fork.readthedocs.io/en/latest/advanced.html)
- [Linter fixit](https://github.com/Instagram/Fixit)
