import factory.fuzzy
from main import models
import datetime
import pytz


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Company

    name = factory.Faker('name')
    text = factory.fuzzy.FuzzyText()


class FlyingsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Flyings

    fr = factory.Faker('name')
    to = factory.Faker('name')
    wh = factory.fuzzy.FuzzyDateTime(datetime.datetime.now(tz=pytz.timezone('UTC')))
    price =factory.fuzzy.FuzzyInteger(0, 5000000)
    co = factory.fuzzy.FuzzyInteger(0, 5000000)
    Company_id = factory.SubFactory(CompanyFactory)


