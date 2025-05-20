# Configuration settings for the EU AI Act assistant
import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

# Document settings
PDF_FILE = RAW_DATA_DIR / "EU_AI_ACT.pdf"

# Chunking settings
MAX_CHUNK_SIZE = 1500
MIN_CHUNK_SIZE = 150
CHUNK_OVERLAP = 100  