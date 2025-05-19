"""
Text extraction module using AWS Textract for the EU AI ChACT chatbot.
Handles document processing from S3 and text extraction.
"""

import boto3
import time
import logging
from config import *

SESSION = boto3.Session(profile_name=PROFILE_NAME)
S3_CLIENT = SESSION.client("s3", region_name=AWS_REGION)
TEXTRACT_CLIENT = SESSION.client("textract", region_name=AWS_REGION)

logging.basicConfig(
    level=logging.INFO if IS_DEVELOPMENT_MODE else logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def start_document_analysis(bucket_name, document_key):
    """
    Start an asynchronous Textract job for document analysis.
    
    Args:
        bucket_name: S3 bucket containing the document
        document_key: Path to the document in S3
        
    Returns:
        textract_job_id: ID of the Textract job
    """
    # AWS API calls should have error handling
    try:
        logger.info(f"Starting Textract analysis for s3://{bucket_name}/{document_key}")
        response = TEXTRACT_CLIENT.start_document_analysis(
            DocumentLocation={
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': document_key
                }
            },
            FeatureTypes=['TABLES', 'FORMS', "LAYOUT"]
        )

        job_id = response['JobId']
        logger.info(f"Textract job started with ID: {job_id }")
        return job_id 
    except Exception as e:
        logger.error(f"Failed to start Textract job: {str(e)}")
        raise

def check_job_status(job_id):
    """Check the current status of a Textract job."""
    response = TEXTRACT_CLIENT.get_document_analysis(JobId=job_id)
    status = response['JobStatus']
    logger.info(f"Job {job_id} status: {status}")
    return status    

def wait_for_job_completion(job_id, max_attempts=30, waiting_interval=10):
    """Wait for Textract job to finish by polling status."""
    logger.info(f"Waiting for job {job_id} to complete...")

    for attempt in range(max_attempts):
        status = check_job_status(job_id)
        
        if status == 'SUCCEEDED':
            logger.info(f"Job {job_id} completed successfully")
            return True
        
        elif status == 'IN_PROGRESS':
            logger.info(f"Job in progress. Checking again in 10 seconds... (Attempt {attempt+1}/{max_attempts})")
            time.sleep(waiting_interval)
            continue
        
        elif status == 'FAILED':
            logger.error(f"Job {job_id} failed")
            return False
        
        elif status == "PARTIAL_SUCCESS":
            logger.info(f"Job {job_id} partially completed. Please retry.")
            return False
        
        else:
            logger.warning(f"Unexpected job status: {status}. Continuing to poll...")
            time.sleep(waiting_interval)
            continue
    
    # If we reach max attempts and job is still not complete
    logger.error(f"Timeout waiting for job {job_id} to complete")
    return False

textract_job_id = start_document_analysis(bucket_name=S3_BUCKET_NAME, document_key=S3_PDF_KEY)

wait_for_job_completion(textract_job_id)

