🤖 AI Chatbot (ML Domain)
A full-stack, domain-specific AI chatbot application focused on Machine Learning concepts, powered by a Large Language Model (LLM) with Retrieval-Augmented Generation (RAG), containerized using Docker.

📌 Project Overview
This application allows users to ask natural language questions about Machine Learning topics and receive accurate, context-aware responses. The system leverages RAG to ground LLM responses in domain-specific knowledge, ensuring reliable and relevant answers.

🧠 Key Technologies
🔮 LLM (Large Language Model)

Powers the core question-answering capability of the chatbot
Generates intelligent, human-like responses to ML-related queries
Integrated via API within the backend service

📚 RAG (Retrieval-Augmented Generation)

Enhances LLM responses by retrieving relevant context from a domain-specific knowledge base
Reduces hallucinations by grounding answers in factual, curated ML content
Combines vector similarity search with generative responses

🐳 Docker

The entire application is containerized using Docker and orchestrated with docker-compose
Runs as a multi-container setup:

chatbot-frontend — serves the UI on port 8501
chatbot-backend — handles API requests on port 8000


Ensures consistent environments across development and production


🗂️ Project Structure
ai-chatbot-docker/
├── app/                  # Core application logic (AI service layer)
├── backend/              # Backend API service
├── frontend/             # Frontend UI application
├── docs/                 # Project documentation
├── tests/                # Unit tests for AI response service
├── .dockerignore         # Files excluded from Docker builds
├── .gitignore
├── Dockerfile            # Base Dockerfile with environment variable support
├── docker-compose.yml    # Multi-container orchestration
├── requirements.txt      # Python dependencies
└── README.md

🚀 Getting Started
Prerequisites

Docker Desktop installed and running
Git

Installation & Run

Clone the repository

bash   git clone <your-repo-url>
   cd ai-chatbot-docker

Set up environment variables
Create a .env file in the project root and add your LLM API key:

env   API_KEY=your_api_key_here

Build and start all containers

bash   docker-compose up --build

Access the application

Frontend UI: http://localhost:8501
Backend API: http://localhost:8000




🖥️ Application Demo
The chatbot interface allows users to type any ML-related question and receive a concise, accurate response:
Example:

Input: what is machine learning?
Output: Machine Learning enables systems to improve performance through exposure to data without explicit programming.


🐳 Docker Architecture
ContainerImagePortchatbot-frontendai-chatbot-docker-frontend8501:8501chatbot-backendai-chatbot-docker-backend8000:8000
Both containers are managed under the ai-chatbot-docker compose group.

🧪 Testing
Unit tests are available under the tests/ directory, covering the AI response service.
bash# Run tests inside the backend container
docker exec -it chatbot-backend pytest tests/

📦 Dependencies
All Python dependencies are listed in requirements.txt. Key categories include:

LLM client library
RAG / vector store integration
Backend web framework
Frontend UI framework (Streamlit)


🔐 Security Notes

API keys and secrets are managed via environment variables
A .dockerignore file ensures secrets and unnecessary files are excluded from Docker builds
Never commit .env files to version control


📁 Git Commit History Highlights
CommitDescriptionInitial commitFastAPI chatbot structure scaffoldedAI service layerResolved merge conflicts and integrated AI service layerDocker integrationFinalized Docker setup for full-stack chatbot systemUnit testsUpdated unit tests for AI response serviceFinal polishDemo readiness improvements across backend and frontend

📄 License
This project is intended for educational and demonstration purposes.
