import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Unit tests for console.py"""

    def setUp(self):
        """Set up test environment"""
        storage.all().clear()

    def tearDown(self):
        """Tear down test environment"""
        storage.all().clear()

    def test_create_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_create_valid(self):
        """Test create command with valid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertIn("User.{}".format(user_id), storage.all())

    def test_show_missing_class(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_show_invalid_class(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        """Test show command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_show_no_instance_found(self):
        """Test show command with non-existent instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_show_valid(self):
        """Test show command with valid class and id"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User {}".format(user.id))
            output = f.getvalue().strip()
            self.assertIn("[User] ({})".format(user.id), output)

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        """Test destroy command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_destroy_no_instance_found(self):
        """Test destroy command with non-existent instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_destroy_valid(self):
        """Test destroy command with valid class and id"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User {}".format(user.id))
            self.assertNotIn("User.{}".format(user.id), storage.all())

    def test_all_invalid_class(self):
        """Test all command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_all_valid(self):
        """Test all command with valid class name"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            self.assertIn("[User] ({})".format(user.id), f.getvalue().strip())

    def test_update_missing_class(self):
        """Test update command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_update_invalid_class(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update MyModel 1234")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_update_no_instance_found(self):
        """Test update command with non-existent instance"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 1234")
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_update_missing_attr_name(self):
        """Test update command with missing attribute name"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {}".format(user.id))
            self.assertEqual(f.getvalue().strip(), "** attribute name missing **")

    def test_update_missing_attr_value(self):
        """Test update command with missing attribute value"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User {} first_name".format(user.id))
            self.assertEqual(f.getvalue().strip(), "** value missing **")

    def test_update_valid(self):
        """Test update command with valid class, id, and attribute"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('update User {} first_name "John"'.format(user.id))
            self.assertIn('"first_name": "John"', str(storage.all()))

    def test_update_with_dict(self):
        """Test update command with dictionary"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.update("{}", {{"first_name": "John", "age": 30}})'.format(user.id))
            self.assertIn('"first_name": "John"', str(storage.all()))
            self.assertIn('"age": 30', str(storage.all()))

    def test_count_invalid_class(self):
        """Test count command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.count()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_count_valid(self):
        """Test count command with valid class name"""
        user = User()
        storage.new(user)
        storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertEqual(f.getvalue().strip(), "1")


if __name__ == '__main__':
    unittest.main()

