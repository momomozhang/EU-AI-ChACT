"""
Configuration settings for the EU AI ChACT application.
Contains AWS settings and application parameters.
"""

# AWS Basic Configuration
AWS_REGION = "eu-central-1"
S3_BUCKET_NAME = "eu-ai-chact"
PROFILE_NAME = "boto-course"

# Document Setting
PDF_FILENAME = "EU_AI_ACT.pdf"
S3_PDF_KEY = PDF_FILENAME
S3_PDF_URI = f"s3://{S3_BUCKET_NAME}/{S3_PDF_KEY}"

# Testing Configuration
TEST_MODE = True  # Set to True to avoid running actual Textract jobs 
SAVED_JOB_ID = "b1e81e31c7e2e90bfc38e388418bf55cdee9c7118f2cc3b71b1eea5fc85788a9" 
OUTPUT_FILE = "eu_ai_act_text.txt"

# Application Settings
IS_DEVELOPMENT_MODE = True
