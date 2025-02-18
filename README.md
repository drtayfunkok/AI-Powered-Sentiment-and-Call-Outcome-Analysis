# AI-Powered-Sentiment-and-Call-Outcome-Analysis

## Overview
This project leverages **AI and Large Language Models (LLMs)** to analyze customer service call transcripts. It automatically classifies **sentiment** (Positive, Neutral, Negative) and determines the **call outcome** (Resolved or Follow-Up Needed). 


The goal is to automate transcript analysis, reduce manual effort, and provide data-driven insights for customer service improvement.


AI-Powered-Sentiment-and-Call-Outcome-Analysis/
│── src/                    # Source code directory
│   ├── main.py             # Flask web app for transcript analysis
│   ├── preprocessing.py     # Functions to extract customer responses from transcripts
│   ├── model.py            # AI model logic for sentiment & call outcome classification
│── test/                   # Contains test cases for model evaluation
│── requirements.txt        # Required libraries for the project
│── README.md               # Project documentation
│── presentation.pdf        # 10-minute presentation slides
│── sample_transcripts/     # Example call transcripts for testing

Installation & Setup : 

1. Clone the Repository

git clone https://github.com/drtayfunkok/AI-Powered-Sentiment-and-Call-Outcome-Analysis.git
cd AI-Powered-Sentiment-and-Call-Outcome-Analysis

2. Create a Virtual Environment
venv\Scripts\activate     # For Windows

3. Install Dependencies
pip install -r requirements.txt

4. Set Your OpenAI API Key
set OPENAI_API_KEY="your_api_key_here"

5. Running the Application
python preprocessing.py
python model.py
python main.py

