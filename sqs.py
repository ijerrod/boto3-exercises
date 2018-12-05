# coding: utf-8
"""Using Boto3 to Manage AWS SQS"""

import boto3

session = boto3.Session(profile_name='pythonAutomation')
sqs = session.resource('sqs')

"""Creates queue with a 5 second delivery delay"""
queue = sqs.create_queue(QueueName='testqueue', Attributes={'DelaySeconds': '5'})
