# tests/test_console.py

import unittest
from io import StringIO
from unittest.mock import patch, MagicMock
from console import HBNBCommand
from models import storage
from models.user import User
import uuid

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.cli = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_user(self, mock_stdout):
        with patch('models.storage') as mock_storage:
            mock_storage.new = MagicMock()
            mock_storage.save = MagicMock()
            self.cli.onecmd('create User')
            output = mock_stdout.getvalue().strip()
            try:
                uuid_obj = uuid.UUID(output, version=4)
                self.assertTrue(True)  # If no exception, the output is a valid UUID
            except ValueError:
                self.fail("Output is not a valid UUID")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_user(self, mock_stdout):
        user = User()
        user_id = user.id
        storage.new(user)
        storage.save()
        self.cli.onecmd(f'show User {user_id}')
        output = mock_stdout.getvalue().strip()
        self.assertIn(user_id, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_user(self, mock_stdout):
        user = User()
        user_id = user.id
        storage.new(user)
        storage.save()
        self.cli.onecmd(f'destroy User {user_id}')
        self.assertNotIn(f'User.{user_id}', storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all_users(self, mock_stdout):
        user1 = User()
        user2 = User()
        storage.new(user1)
        storage.new(user2)
        storage.save()
        self.cli.onecmd('all User')
        output = mock_stdout.getvalue().strip()
        self.assertIn(user1.id, output)
        self.assertIn(user2.id, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_user(self, mock_stdout):
        user = User()
        user_id = user.id
        storage.new(user)
        storage.save()
        self.cli.onecmd(f'update User {user_id} first_name "John"')
        updated_user = storage.all()[f'User.{user_id}']
        self.assertEqual(updated_user.first_name, 'John')

if __name__ == '__main__':
    unittest.main()

