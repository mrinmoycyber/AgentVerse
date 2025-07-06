# AgentVerse

## Project Goal 🎯
This project is an AI Agent-powered Streamlit web application designed to assist users with queries related to the Marvel and DC comic universes.  
At its core is a master agent that intelligently routes user questions to the appropriate domain-specific agent, either Marvel or DC, using a Gemini-based LLM classifier.  

Users can interact with the system in two modes:  
1. **LLM-based assistant** for dynamic reasoning and conversation  
2. **Dataset-driven mode** where queries are answered using pre-curated information from structured Marvel and DC datasets.  

The system employs modular agents to separate concerns cleanly.  
Gemini API integration ensures lightweight, fast response generation.  
This architecture allows scalable, accurate, and context-aware responses across both comic book domains.

## Project Structure 📁
```plaintext
├── Agents/                  # Contains agent logic (e.g., master_agent.py, marvel_agent.py, dc_agent.py)
├── Dataset/                 # Contains Marvel/DC datasets                
├── streamlit_app.py         # Entry point for the Streamlit web application
├── utils.py                 # Shared utilities (e.g., LLM calls, search links)
├── .gitignore            
├── LICENSE                 
└── README.md 
``` 

## Video Output 🎥
Watch the project demo here: 

https://github.com/user-attachments/assets/1cf4324a-321e-4459-a99a-8940b422d536

## Requirements 📦
To run this project, ensure you have the following dependencies installed:

- `streamlit`
- `google-generativeai`
- `pandas`
- `python-dotenv`

You can install the required packages using pip:

```bash
pip install streamlit google-generativeai python-dotenv pandas
```
## Usage 🚀
Clone the repository:
```bash
git clone https://github.com/mrinmoycyber/AgentVerse.git
```
Navigate to the project directory:
```bash
cd AgentVerse
```
Create a .env file and add your Gemini API key:
```bash
GEMINI_API_KEY=your_api_key_here
```
Run the Streamlit app:
```bash
streamlit_app.py 
```
