from django.test import TestCase
from hello.models import Animal


# Create your tests here.
class TestAnimal(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sounds="roar")
        Animal.objects.create(name="cat", sounds="meow")

    def tearDown(self):
        pass

    def test_animal_say(self):
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), "the lion says roar ")
        self.assertEqual(cat.speak(), "the cat says meow ")