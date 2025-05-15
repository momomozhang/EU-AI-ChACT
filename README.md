# EU AI ChACT

Ask questions about the EU AI Act and get clear answers. This is a learning project that shows how to build a chatbot using RAG (Retrieval-Augmented Generation) and AWS.

## What it does

You type a question about the EU AI Act, and it:
1. Searches through the EU AI ACT text for relevant sections
2. Sends your question and those sections to Claude
3. Returns a plain-English answer

The whole thing runs on AWS Lambda, so it's cheap to host and scales automatically.

## Target audience:
Tech professionals and general people interested in GenAI technology but unfamiliar with the EU AI Act.
It provides accessible first glimpse of legal regulations, helping users understand how the EU AI Act might relate to GenAI development and deployment. However, users should consult legal professionals for commercial products or specific project advice.

## Tech used

**Backend stuff**: Python, AWS Lambda, API Gateway
**AI parts**: Claude for chat, vector embeddings for search
**Infrastructure**: CDK to set everything up
**Vector storage**: TBD (probably Pinecone or OpenSearch)

## Status

Still building this. It's a portfolio project to learn about:
- RAG systems
- Document chunking and embeddings
- AWS serverless architecture
- CDK for infrastructure

Right now I have the basic structure set up. Next steps are getting the document processing working, then the chat interface.

## Why the EU AI Act?

It's a complex legal document that's perfect for testing RAG systems. Plus it's actually useful - the Act affects lots of businesses but isn't easy to understand.

## License

MIT

## WIP:
# Document Ingestion: 
the file format is PDF. After consideration, I chose to work with PyMuPDF as the parsing library for the following reasons:
1. It can handle complex layouts and formatting
2. It is able to preserve formatting that indicates hierarchy
3. Fast performance

# Chunking strategy: 

The EU AI Act is a complex legal document with:
- 113 articles across 13 chapters
- 13 detailed annexes
- hierarchical structure: chapter -> section -> article -> paragraph
- cross references between articals

Therefore, I decided on choosing the hierarchical chunking with semantic boundaries. It allows both detailed provisions while preserving their broader context.
- primary chunks: complete articles (ca 500 - 1500 tokens)
- child chunks: for articles exceeding 1000 tokens - paragraphs / sub-sections
- special handling for annexes as separate chunks with parent references to the articles
- preserve structural hierachy: chapter -> section -> article -> paragraph

# Document Processing Steps:

1. Extract PDF content: Use PyMuPDF to pull text
2. Parse document structure - Find articles, sections, chapters, and those chunky annexes at the end
3. Break into chunks - Split by articles mostly, but break up the really long ones at paragraph boundaries
4. Add metadata - Tag each chunk with its location, related articles, and key concepts
5. Create embeddings - Convert everything to vectors and stuff them in one database
6. Build search index - Set it up so you can find both specific details and general concepts

# File Structure
/src/chact/
├── pdf_extractor.py      # class PDFExtractor
├── structure_analyzer.py # class StructureAnalyzer
├── document_segmenter.py # class DocumentSegmenter
└── document_pipeline.py # class DocumentPipeline