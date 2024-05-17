from fastapi.openapi.docs import get_swagger_ui_html
from fastapi import FastAPI, HTTPException
from cloud_trail_event_model import CloudTrailEvent
from queue_writer.sqs_queue_writer import SQSQueueWriter
app = FastAPI()
queue_writer = SQSQueueWriter()


# free tier Amazon 
# sqs - queue of Amazon, poto3 sqsclient put and get
# kinesis firehoes - queue of Amazon
# kafka
# EC2 (kubernetes amazon)


@app.post("/cloudtrail_event/")
async def cloudtrail_event(event: CloudTrailEvent):
    """
    Receive CloudTrail event data and handle it by writing to a queue.
    
    This route receives CloudTrail event data from the CloudTrail Producer (Amazon CloudTrail).
    
    The event is then handled by writing it to a queue for further processing.
    """
    try:
        queue_writer.write_to_queue(event)
        return {"message": "Event received and queued for processing"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing event: {str(e)}")

# Generate Swagger documentation with Swagger UI
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="CloudTrail Event Receiver")

@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    return app.openapi()

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Welcome to CloudTrail Event Receiver. Go to /docs to see the Swagger UI."}