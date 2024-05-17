# Ingestion Service

This service provides an endpoint to receive CloudTrail event data from the CloudTrail Producer (Amazon CloudTrail) and handle it by writing it to an SQS queue for further processing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have Python 3.8 or later installed on your system.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ymichels/ingestion-service.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ingestion-service
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration
Set up your AWS credentials and region by modifying the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_REGION` variables in config.py

## Usage

To run the service, use the following command:

```bash
uvicorn app:app --host 0.0.0.0 --port 8200
```

The service will start and be accessible at http://localhost:8200.

## API Documentation

Swagger UI is available for exploring and testing the API endpoints. Access it at `http://localhost:8200/docs`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.