from abc import ABC, abstractmethod
from cloud_trail_event_model import CloudTrailEvent


class QueuePublisherInterface(ABC):
    @abstractmethod
    def write_to_queue(self, event: CloudTrailEvent):
        """
        Write a CloudTrailEvent object to a queue.

        Parameters:
        - event (CloudTrailEvent): The CloudTrailEvent object to write to the queue.
        """
        pass
