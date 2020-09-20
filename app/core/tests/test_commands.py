from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):
    def test_wait_for_db_connect(self):
        """Test database Connection errors"""
        with patch("django.db.utils.ConnectionHandler.__getitem__") as getItem:
            getItem.return_value = True
            call_command("wait_for_db")

            self.assertEqual(getItem.call_count, 1)

    @patch("time.sleep", return_value=True)
    def test_wait_for_db(self, ts):
        """Test Waiting for DB Connection"""
        with patch("django.db.utils.ConnectionHandler.__getitem__") as getItem:
            getItem.side_effect = [OperationalError] * 5 + [True]
            call_command("wait_for_db")
            self.assertEqual(getItem.call_count, 6)
