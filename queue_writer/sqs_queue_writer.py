from queue_writer.queue_writer_interface import QueueWriterInterface
from cloud_trail_event_model import CloudTrailEvent
import boto3
import json
from config import REGION_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


class SQSQueueWriter(QueueWriterInterface):

    def write_to_queue(self, event: CloudTrailEvent):
        sqs_client = boto3.client('sqs', region_name=REGION_NAME,
                                  aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
        sqs_client.send_message(
            QueueUrl='https://sqs.eu-north-1.amazonaws.com/767398004368/orca-excercise',
            MessageBody=json.dumps(event.__dict__)
        )
        # Implement the logic to write the event to a queue here
        print("Writing event to queue:", event.eventID)
