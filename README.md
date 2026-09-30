# EyeAssist AI — Phase-wise Implementation

EyeAssist AI is a research-oriented AI assistant for ophthalmology that combines **Retrieval-Augmented Generation (RAG)**, trusted medical knowledge sources, web retrieval, and eventually **medical image classification** to provide evidence-grounded information about common eye diseases.

## Phase 1 — Trusted Data Collection & Knowledge Base ✅

**Objective:** Build a reliable ophthalmology knowledge base from trusted medical sources.

### Implementation

* Identified authoritative ophthalmology and healthcare sources.
* Collected information related to common eye diseases.
* Automated web-page extraction and PDF downloading.
* Organized documents topic-wise.
* Created a structured data directory for raw and processed knowledge.
* Implemented data-quality validation and reporting.

### Trusted Sources

* American Academy of Ophthalmology (AAO)
* National Eye Institute (NEI)
* World Health Organization (WHO)
* PubMed
* MedlinePlus
* Mayo Clinic
* NHS
* EyeWiki

### Current Knowledge Base

Topics include:

* Cataract
* Diabetic Retinopathy
* Glaucoma
* Eye Redness
* Other ophthalmology-related information

**Status:** Completed

---

## Phase 2 — Document Processing & Preparation

**Objective:** Convert collected medical documents into clean, retrieval-ready text.

### Implementation

* Inspect and clean downloaded documents.
* Remove irrelevant HTML/content artifacts.
* Normalize text.
* Handle duplicate and low-quality documents.
* Organize documents according to disease/topic.
* Prepare metadata such as:

  * Source
  * Disease/topic
  * Document name
  * URL
  * Document type

### Planned Processing Pipeline

```text
Raw Documents
      ↓
Text Extraction
      ↓
Cleaning & Normalization
      ↓
Metadata Creation
      ↓
Quality Validation
      ↓
Processed Knowledge Base
```

**Status:** In progress

---

## Phase 3 — Text Chunking & Embeddings

**Objective:** Convert medical documents into meaningful searchable chunks.

### Implementation

* Divide documents into semantically useful chunks.
* Experiment with chunk size and overlap.
* Preserve document metadata with every chunk.
* Generate vector embeddings using a local embedding model.
* Prepare embeddings for vector database storage.

### Pipeline

```text
Processed Documents
        ↓
Text Chunking
        ↓
Embedding Model
        ↓
Vector Representations
```

**Status:** Next implementation stage

---

## Phase 4 — Vector Database & Retrieval

**Objective:** Build the retrieval layer of the RAG system.

### Implementation

* Store document chunks and embeddings in a vector database.
* Implement semantic similarity search.
* Retrieve the most relevant medical passages for a user query.
* Preserve source metadata for citation and traceability.
* Experiment with the number of retrieved documents (`Top-K`).

### Retrieval Pipeline

```text
User Query
    ↓
Query Embedding
    ↓
Vector Search
    ↓
Relevant Medical Chunks
    ↓
Context
```

**Status:** Planned

---

## Phase 5 — RAG-Based Medical Assistant

**Objective:** Generate responses grounded in the retrieved ophthalmology knowledge base.

### Implementation

* Connect the retrieval system with a local LLM.
* Use retrieved documents as contextual information.
* Generate answers based on retrieved evidence rather than relying only on model knowledge.
* Include source information with responses.
* Design prompts specifically for ophthalmology-related queries.
* Reduce unsupported or hallucinated responses.

### RAG Architecture

```text
                 ┌─────────────────┐
                 │   User Query    │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Query Embedding │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Vector Database │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Relevant Context│
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │      LLM        │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ Grounded Answer │
                 └─────────────────┘
```

**Status:** Planned

---

## Phase 6 — Trusted Web Retrieval Fallback

**Objective:** Allow EyeAssist to retrieve newer information when the local knowledge base does not contain sufficient information.

### Logic

```text
User Query
    ↓
Knowledge Base Retrieval
    ↓
Relevant Information Found?
   / \
 Yes  No
 ↓     ↓
RAG   Web Search
 ↓     ↓
Answer + Sources
```

### Implementation

* Perform knowledge-base retrieval first.
* Evaluate whether the retrieved context is sufficient.
* If information is insufficient, search trusted web sources.
* Restrict web retrieval to approved medical domains where possible.
* Extract relevant information.
* Provide source attribution.

This creates a **hybrid RAG + web research architecture** rather than relying exclusively on static documents.

**Status:** Planned

---

## Phase 7 — Ophthalmology Image Classification

**Objective:** Extend EyeAssist from a text-based research assistant into a multimodal system capable of analysing eye images.

### Planned Capabilities

The image-analysis component will investigate classification of conditions such as:

* Normal eye
* Cataract
* Glaucoma
* Diabetic Retinopathy
* Other relevant ophthalmic conditions depending on dataset availability

### Implementation Approach

```text
Eye Image
    ↓
Image Preprocessing
    ↓
Pre-trained / Fine-tuned CNN or Vision Model
    ↓
Disease Prediction
    ↓
Confidence / Classification Result
```

Model development and experimentation will use GPU-based environments such as Kaggle where required.

**Status:** Planned / Research stage

---

## Phase 8 — Hybrid EyeAssist Architecture

**Objective:** Combine image analysis, RAG, and web retrieval into a single AI assistant.

### Proposed Architecture

```text
                    ┌───────────────┐
                    │     User      │
                    └───────┬───────┘
                            ↓
                 ┌────────────────────┐
                 │   EyeAssist AI     │
                 └─────────┬──────────┘
                           ↓
              ┌────────────────────────┐
              │    Query / Image       │
              │      Analysis           │
              └───────────┬────────────┘
                          ↓
             ┌────────────┴─────────────┐
             ↓                          ↓
      Text Question                 Eye Image
             ↓                          ↓
       RAG Pipeline              Image Classifier
             ↓                          ↓
      Vector Database             Prediction
             ↓                          ↓
             └────────────┬─────────────┘
                          ↓
                 ┌─────────────────┐
                 │ Medical Context │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │      LLM        │
                 └────────┬────────┘
                          ↓
                 ┌─────────────────┐
                 │ User Response   │
                 │ + Sources       │
                 └─────────────────┘
```

The goal is to allow the system to use **both structured medical knowledge and visual information** when responding to users.

**Status:** Planned

---

## Phase 9 — Backend & Web Application

**Objective:** Convert the research prototype into an accessible web application.

### Planned Components

* Python backend
* RAG pipeline
* Vector database
* LLM integration
* Image upload and classification
* Source/citation display
* User-friendly chat interface

### User Flow

```text
User
 ↓
Upload Image / Ask Question
 ↓
EyeAssist Processing
 ↓
RAG / Image Analysis / Web Retrieval
 ↓
AI Response
 ↓
Sources + Relevant Information
```

**Status:** Planned

---

## Phase 10 — Evaluation & Research Validation

**Objective:** Evaluate the reliability and performance of the complete system.

### RAG Evaluation

* Retrieval relevance
* Context quality
* Answer faithfulness
* Source correctness
* Hallucination analysis
* Response latency

### Image Model Evaluation

* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrix
* Class-wise performance

### System Evaluation

* End-to-end response quality
* Retrieval failure cases
* Image classification failure cases
* Performance under different query types
* Comparison of different models/configurations

**Status:** Planned

---

# Overall Development Roadmap

```text
Phase 1
Trusted Data Collection
        ↓
Phase 2
Document Processing
        ↓
Phase 3
Chunking + Embeddings
        ↓
Phase 4
Vector Database + Retrieval
        ↓
Phase 5
RAG Assistant
        ↓
Phase 6
Trusted Web Fallback
        ↓
Phase 7
Image Classification
        ↓
Phase 8
Hybrid AI System
        ↓
Phase 9
Web Application
        ↓
Phase 10
Evaluation + Research Validation
```

## Current Focus

The immediate development priority is the **RAG pipeline**:

**Data → Cleaning → Chunking → Embeddings → Vector Database → Retrieval → LLM → Grounded Response → Citations**

The image-classification component will be integrated after the core RAG assistant is functioning reliably.
