from django.test import TestCase
from users.models import MyUserManager, User

class testmymanager(TestCase):
    def test_createuser(self):
        Mang = MyUserManager.create_user(MyUserManager, email='eail', username='userame',password= 'pasword')
