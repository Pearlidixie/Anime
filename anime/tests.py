
from django.test.testcases import TestCase

# Create your tests here.

from django import forms
from .models import User
from .forms import UserReg
from datetime import date

class UserRegModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(firstname="Bame", surname="malapeng", username="bamsey",user_dob= date(1997,5,3), user_email="bm@yahoo.com", password="mornings", re_enter_password="mornings")

        self.form = UserReg({
                'firstname':"Bame",

                'surname':"malapeng",

                'username':"bamsey",

                'user_dob':date(1997,5,3),

                'user_email':"bm@yahoo.com",

                'password': "kemokemo",

                're_enter_password':"kemokemo",})


    """test if the form is valid"""
    def test_valid_data(self):
        self.assertTrue(self.form.is_valid())
        user = self.form.save()
        #user.save()
        print(user.__dict__)
        self.assertEqual(user.firstname, "Bame")
        self.assertEqual(user.surname, "malapeng")
        self.assertEqual(user.username, "bamsey")
        self.assertEqual(user.user_dob, date(1997,5,3))
        self.assertEqual(user.user_email, "bm@yahoo.com")
        self.assertEqual(user.password, "kemokemo")
        self.assertEqual(user.re_enter_password, "kemokemo")

    """ test if the first password matches the second password """
    def test_password_match(self):

        user = self.form.save()
        pass1 = user.password
        pass2 = user.re_enter_password
        self.assertEqual(pass1,pass2)

    """ test whether the password is longer than 7 characters """
    def test_password_length(self):
        user = self.form.save()
        pass1 = user.password
        self.assertTrue(pass1 > str(7))

    """ test if the date of birth entered is not in the future """
    def test_date_of_birth_not_future(self):
        user = self.form.save()
        dob = user.user_dob
        self.assertTrue(dob < date.today())

    """ test if the date of birth entered is the correct type"""
    def test_date_type(self):
        user = self.form.save()
        dob = user.user_dob
        self.assertIsInstance(dob, date)

    """ test if the '@' is present in the email """
    def test_email_correct(self):
        user = self.form.save()
        email = user.user_email
        self.assertIn('@',email)

    """ test if the firstname is not the password """
    def test_firstname_not_password(self):
        user = self.form.save()
        name = user.firstname
        pass1 = user.password
        self.assertNotEqual(name,pass1)

    """ test if the surname is not the password """
    def test_surname_not_password(self):
        user = self.form.save()
        surname = user.surname
        pass1 = user.password
        self.assertNotEqual(surname,pass1)

    """ test if the username is not the password """
    def test_username_not_password(self):
        user = self.form.save()
        uname = user.username
        pass1 = user.password
        self.assertNotEqual(uname,pass1)
