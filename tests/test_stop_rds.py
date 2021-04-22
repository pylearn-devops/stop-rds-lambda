import unittest
import stop_rds
from unittest import mock
from unittest.mock import patch, MagicMock

from moto import mock_rds
import boto3_mocking


class Test_lambda_handler(unittest.TestCase):
    @patch("stop_rds.stop_rds_instances", return_value=None)
    def test_stopping_rds(self, mock_stop_rds_instances):

        boto3 = MagicMock()
        client = boto3.client("rds")
        event = {"action": "stop", "dbInstance": "rds-name"}
        result = stop_rds.lambda_handler(event, {})
        print(result)

    @patch("stop_rds.start_rds_instances", return_value=None)
    def test_start_rds(self, mock_stop_rds_instances):

        boto3 = MagicMock()
        client = boto3.client("rds")
        event = {"action": "start", "dbInstance": "rds-name"}
        result = stop_rds.lambda_handler(event, {})
        print(result)

    def test_stop_rds_instances(self):
        boto3_mocking.engage_patching()
        boto3_mocking.clients.stop_db_instance("rds")
        result = stop_rds.stop_rds_instances("rds-name")
        print(result)


if __name__ == "__main__":
    unittest.main()
