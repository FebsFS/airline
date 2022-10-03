from django.test import TestCase
from main.tests.factories import FlyingsFactory, CompanyFactory


class TestCompanyModel(TestCase):
    def test_costr(self):
        comp = CompanyFactory(name='django')
        self.assertEqual(comp.__str__(), 'django')


class TestflyingsModel(TestCase):
    def test_flstr(self):
        fly = FlyingsFactory(fr='Moscow', to='Paris')
        self.assertEqual(fly.__str__(), 'Moscow - Paris')