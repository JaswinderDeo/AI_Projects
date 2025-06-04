AI Content Research & Writing Assistant
A powerful content generation system built with CrewAI that combines research, analysis, and writing capabilities to produce high-quality blog posts on any topic.

 Goal
Enhance your Research Agent by giving it access to local documents (PDFs, text, CSV, etc.) or vector-based knowledge it can search and use when answering.

Steps to Add RAG
We'll use:

Its not worked ->crewai_tools.VectorStoreTool So i used Instead of relying on VectorStoreTool, use LangChain directly.
Documents → split → embed → store → search

🚀 Features
Automated research using Wikipedia and WolframAlpha
AI-powered content writing and analysis
Sentiment analysis and keyword extraction
Streamlit web interface for easy interaction
Downloadable markdown output
📋 Prerequisites
Python 3.9+
OpenAI API key
WolframAlpha API key
🛠️ Installation
Clone the repository:
git clone <repository-url>
cd CrewAI-Demo
Create and activate a virtual environment:
conda create -n crewai python==3.12 -y
conda activate crewai
Install dependencies:
pip install -r requirements.txt
Set up environment variables:
Copy .env.example to .env
Add your API keys to .env:
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_key
🚀 Running the Application
Command Line Version
Run the basic version using:

python app.py
Web Interface
Launch the Streamlit web interface:

streamlit run streamlit_app.py
Then open your browser and navigate to http://localhost:8501

💻 Usage
Web Interface:

Enter your desired topic in the sidebar
Adjust the temperature setting if needed
Click "Generate Content"
Wait for the AI to generate your article
Download the result as a markdown file
Command Line:

Edit the topic in app.py
Run the script
Results will be printed to console
🔧 Project Structure
ai-content-assistant/
├── streamlit_app.py    # Web interface
├── app.py             # Command line version
├── requirements.txt   # Project dependencies
├── .env              # Environment variables
└── README.md         # Documentation