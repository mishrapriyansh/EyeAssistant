# EyeAssist AI

An AI-powered ophthalmology screening and knowledge assistant designed to combine
retinal image analysis with Retrieval-Augmented Generation (RAG) and trusted
medical web research.

> Disclaimer: EyeAssist AI is an academic/research project. It is not a
> medical diagnostic system and must not be used as a substitute for evaluation
> by a qualified healthcare professional.
## Project Overview
EyeAssist AI aims to provide two major capabilities:

1. Analyze retinal/fundus images using a pretrained ophthalmology image
   classification model to identify patterns associated with selected eye
   conditions.

2. Provide an ophthalmology knowledge assistant that retrieves information from
   a curated medical knowledge base and, when necessary, searches trusted
   medical sources on the web.

The project is being developed incrementally, with data acquisition forming
the foundation for the future RAG system.
### Phase 1 — Ophthalmology Data Collection

**Status: Completed**

The first phase focused on building a reliable medical knowledge acquisition
pipeline.

Current workflow:

User Query
    ↓
Web Search
    ↓
Trusted Domain Filtering
    ↓
Web Scraping
    ↓
HTML Parsing
    ↓
Clean Medical Text
    ↓
Knowledge Base

### Completed Components

- Web search module
- Trusted-domain filtering
- Web scraping
- HTML parsing
- Error handling for inaccessible webpages
- Medical content extraction
- Knowledge-base storage
- Environment/configuration management
- Modular project structure

---

## Trusted Sources

The project restricts web research to selected trusted medical and
ophthalmology sources.

Examples include:

- American Academy of Ophthalmology (AAO)
- National Eye Institute (NEI)
- MedlinePlus
- PubMed
- EyeWiki
- World Health Organization (WHO)
- Mayo Clinic
- NHS
- Cleveland Clinic

The list of allowed domains is maintained in the project configuration.

---

## Phase 2 — Image Analysis

**Status:Planned / In Progress**

The next phase will evaluate pretrained ophthalmology image-classification
models rather than training a model from scratch.

The initial target classes are:

- Normal
- Cataract
- Glaucoma

The system will focus on retinal/fundus images compatible with the selected
model.

The model will be evaluated using publicly available, de-identified
ophthalmology datasets.

Planned workflow:

Fundus Image
    ↓
Image Validation
    ↓
Preprocessing
    ↓
Pretrained Model
    ↓
Prediction
    ↓
Confidence / Class Probabilities
    ↓
Screening Result

The model output will be treated as an AI screening result rather than a
medical diagnosis.

---

## Phase 3 — Vector Database and RAG

**Status: Planned**

The cleaned ophthalmology documents collected during Phase 1 will be converted
into a searchable knowledge base.

Planned pipeline:

Medical Documents
    ↓
Document Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Retriever
    ↓
Relevant Medical Information
    ↓
Local LLM
    ↓
Answer

The vector database will preserve source metadata so that answers can be
associated with their original medical sources.

---

## Phase 4 — Web Research Fallback

**Status: Planned**

If the vector database does not contain sufficient information to answer a
user's question, the system will use the web research pipeline.

Planned workflow:

User Question
    ↓
Vector Database
    ↓
Sufficient Information?
    │
    ├── Yes → Generate Answer
    │
    └── No
          ↓
      Trusted Web Search
          ↓
        Scraper
          ↓
        Parser
          ↓
      Content Validation
          ↓
      Generate Answer

Only approved/trusted domains will be considered for medical information.

---

## Phase 5 — Backend API

**Status: Planned**

A backend API will expose the system's functionality to the website.

Potential endpoints:

POST /analyze-image
POST /chat
GET  /report/{id}

The exact API design will be finalized during implementation.

## Phase 6 — Web Application

**Status: Planned**

The final application will provide role-based interfaces.

### Healthcare Staff

Healthcare staff will be able to:

- Upload retinal/fundus images
- Run AI screening
- View model predictions
- Generate screening reports

### Patients

Patients will be able to:

- View their screening report
- Learn about the reported condition
- Ask ophthalmology-related questions
- Access information from trusted sources

### Ophthalmologist

A future interface may allow an ophthalmologist to:

- Review the original image
- View AI screening results
- Review relevant medical information
- Make the final clinical assessment

The AI system will not replace professional diagnosis.


## Project Architecture

The planned high-level architecture is:
                    EyeAssist AI
                         |
        +----------------+----------------+
        |                |                |
        v                v                v
 Image Analysis      RAG System       Web Research
        |                |                |
        v                v                v
 Pretrained Model    Vector DB        Trusted Sources
        |                |                |
        +----------------+----------------+
                         |
                         v
                    Local LLM
                    (Ollama)
                         |
                         v
                    Backend API
                         |
                         v
                    Web Application

---
EyeAssist-AI/
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── search.py
│   ├── scraper.py
│   ├── parser.py
│   ├── file_manager.py
│   └── ...
│
├── data/
│   └── knowledge_base/
│       ├── raw/
│       ├── cleaned/
│       └── metadata/
│
├── logs/
│
├── tests/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md