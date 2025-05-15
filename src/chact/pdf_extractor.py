"""
Document Extractor for the EU AI Act PDF file

This module provides robust PDF text extraction with formatting preservation,
specifically optimized for legal documents like the EU AI Act.
"""

import logging
import fitz  # PyMuPDF
from typing import Dict, List, Optional, Any, Generator, Union
from dataclasses import dataclass
from pathlib import Path


logger = logging.getLogger(__name__)

class PDFExtractionError(Exception):
    """Custom exception for PDF extraction errors."""
    pass

@dataclass
class TextBlock:
    """A data container of one piece of extracted text with its properties."""
    text: str
    bbox: tuple  # Bounding box coordinates that define the location of text on the page
    font_size: float
    font_name: str
    font_flags: int
    page_number: int
    attributes: Dict[str, Any] # Metadata about text role and hierarchy

@dataclass
class ExtractedPDF:
    """A data container of the entire extracted PDF as a collection of TextBlocks plus document-level information."""
    text: str
    blocks: List[TextBlock]
    metadata: Dict[str, Any]
    page_count: int

class PDFExtractor:
    """Extracts text and formatting from PDF files with PyMuPDF.
    
    Returns text blocks with font information and basic structural markers.
    Built for legal documents where preserving hierarchy matters. 
    Handles extraction errors gracefully and falls back to simple text when needed.
    """
    