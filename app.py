from fastapi.openapi.docs import get_swagger_ui_html
from fastapi import FastAPI, HTTPException
from cloud_trail_event_model import CloudTrailEvent
from queue_publisher.sqs_queue_publisher import SQSQueuePublisher
from queue_publisher.queue_publisher_interface import QueuePublisherInterface
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
app = FastAPI()
queue_publisher: QueuePublisherInterface = SQSQueuePublisher(logger)


@app.post("/cloudtrail_event/")
async def cloudtrail_event(event: CloudTrailEvent):
    try:
        queue_publisher.write_to_queue(event)
        return {"message": "Event received and queued for processing"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing event: {str(e)}")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="CloudTrail Event Receiver")


@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    return app.openapi()


@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to CloudTrail Event Receiver. Go to /docs to see the Swagger UI."}
