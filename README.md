# EU AI ChACT

Ask questions about the EU AI Act and get clear answers. This is a learning project that shows how to build a chatbot using RAG (Retrieval-Augmented Generation) and AWS.

## What it does

You type a question about the EU AI Act, and it:
1. Searches through the EU AI ACT text for relevant sections
2. Sends your question and those sections to Claude
3. Returns a plain-English answer

The whole thing runs on AWS Lambda, so it's cheap to host and scales automatically.

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
the EU AI Act is a complex legal document with clear hierarchical structure. It has titles, chapters, sections, articles, as well as sub-articles. Therefore, I decided on choosing the hierarchical chunking strategy. It allows both detailed provisions while preserving their broader context.

