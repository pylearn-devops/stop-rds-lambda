''' run this script to stop rds '''

import os
import sys
import json
import logging

import boto3
import botocore
from botocore.exceptions import ClientError

rds = boto3.client('rds')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    
	logger.info("Event: " + str(event))

	dbInstance = event.get('dbInstance')
	action = event.get('action')
	if ('stop' == action):
		stop_rds_instances(dbInstance)  	 
	elif (action == 'start'):
		start_rds_instances(dbInstance)

	return {
    	'statusCode': 200,
    	'body': json.dumps("Script execution completed. See Cloudwatch logs for complete output")
	}	

### stop rds instances
def stop_rds_instances(dbInstance):
	try:
		rds.stop_db_instance(DBInstanceIdentifier=dbInstance)
		logger.info('Success :: stop_db_instance ' + dbInstance) 
	except ClientError as e:
		logger.error(e)   
	return "stopped:OK"

def start_rds_instances(dbInstance):
	try:
		rds.start_db_instance(DBInstanceIdentifier=dbInstance)
		logger.info('Success :: start_db_instance ' + dbInstance) 
	except ClientError as e:
		logger.error(e)   
	return "started:OK"
