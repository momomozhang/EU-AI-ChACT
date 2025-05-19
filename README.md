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

## Technical Process Flow
1. Document Storage: S3
2. Text Extraction: AWS Textract + Lambda
3. Document Chunking: Python + Lambda
4. Embedding Generation: Amazon Bedrock
5. Vector Storage: Amazon OpenSearch Service
6. Metadata Management: Amazon DynamoDB


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


## License

MIT
