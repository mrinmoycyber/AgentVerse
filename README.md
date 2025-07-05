# AgentVerse
A multi-agent streamlit app that answers Marvel and DC questions using intelligent routing and dataset-driven insights.

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
- `python-dotenv`

You can install the required packages using pip:

```bash
pip install streamlit google-generativeai python-dotenv
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
streamlit run app.py
```
