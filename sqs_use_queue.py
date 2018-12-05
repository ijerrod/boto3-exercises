import boto3

session = boto3.Session(profile_name='pythonAutomation')
sqs = session.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='testqueue')

print(queue.url)
print(queue.attributes.get('DelaySeconds'))

for queue in sqs.queues.all():
    print(queue.url)
