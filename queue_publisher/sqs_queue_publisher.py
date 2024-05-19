from queue_publisher.queue_publisher_interface import QueuePublisherInterface
from cloud_trail_event_model import CloudTrailEvent
import boto3
import json
from config import REGION_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
import logging


class SQSQueuePublisher(QueuePublisherInterface):

    def __init__(self, logger:logging.Logger) -> None:
        self.logger = logger
        self.sqs_client = boto3.client('sqs', region_name=REGION_NAME,
                                  aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    def write_to_queue(self, event: CloudTrailEvent):
        try:
            self.logger.info(f"Writing event to queue: {event.eventID}")
            self.sqs_client.send_message(
                QueueUrl='https://sqs.eu-north-1.amazonaws.com/767398004368/orca-excercise',
                MessageBody=json.dumps(event.to_json())
            )
        except Exception as e:
            self.logger.exception(f"Unexpected error: {e}")
