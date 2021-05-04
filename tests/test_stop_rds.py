import unittest
import stop_rds
import boto3
from unittest import mock
from unittest.mock import patch, MagicMock

from moto import mock_rds

# import boto3_mocking


class Test_lambda_handler(unittest.TestCase):
    @patch("stop_rds.stop_rds_instances", return_value="stopped:OK")
    def test_stopping_rds(self, mock_stop_rds_instances):
        boto3 = MagicMock()
        boto3.client("rds")
        event = {"action": "stop", "dbInstance": "rds-name"}
        result = stop_rds.lambda_handler(event, {})

    @patch("stop_rds.start_rds_instances", return_value="started:OK")
    def test_start_rds(self, mock_stop_rds_instances):
        boto3 = MagicMock()
        boto3.client("rds")
        event = {"action": "start", "dbInstance": "rds-name"}
        result = stop_rds.lambda_handler(event, {})

    # def test_stop_rds_instances(self):
    #     # boto3.client('rds', 'us-east-1')
    #     boto3 = MagicMock()
    #     boto3.client('rds', 'us-east-1')
    #     result = stop_rds.stop_rds_instances('dbInstance')
    #     print(result)


if __name__ == "__main__":
    unittest.main()
