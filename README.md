# Wasserstoff AI Intern Task

## Overview
This project is a minimalist yet functional AI-powered document chatbot for the Wasserstoff internship task.

## Features
- Upload PDFs or text files
- FastAPI backend with basic endpoints
- Streamlit UI for upload and querying
- Ready for extension: OCR, FAISS, OpenAI, etc.

## Run Locally

### Backend
```bash
cd backend
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
streamlit run app.py
```

## Next Steps
- Integrate FAISS and embeddings
- Add OCR with Tesseract
- Enhance UI/UX

This repo will evolve with your progress.
