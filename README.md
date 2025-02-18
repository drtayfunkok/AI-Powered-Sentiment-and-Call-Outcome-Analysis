# AI-Powered-Sentiment-and-Call-Outcome-Analysis

## Overview
This project leverages **AI and Large Language Models (LLMs)** to analyze customer service call transcripts. It automatically classifies **sentiment** (Positive, Neutral, Negative) and determines the **call outcome** (Resolved or Follow-Up Needed). 


## Features 
- **Extracts Customer Responses** from call transcripts
- **Sentiment Analysis** using GPT-based models
- **Call Outcome Prediction** (Issue Resolved or Follow-Up Needed)
- **Visual Insights** with graphs and word clouds
- **Web Interface** built with Flask for easy transcript analysis


## Installation & Setup 
1. Clone this repository:
   ```sh
   git clone https://github.com/drtayfunkok/AI-Powered-Sentiment-and-Call-Outcome-Analysis.git
   cd AI-Powered-Sentiment-and-Call-Outcome-Analysis
   
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    
3. Set your OpenAI API Key:
   ```sh
     set OPENAI_API_KEY="your_api_key_here"

4. Run the Flask application:
   ```sh
    preprocessing.py
    model.py
    python src/main.py

### Business Impact 
- Reduces Manual Work by automating transcript analysis.
- Improves Decision Making with AI-driven insights.
- Enhances Customer Satisfaction by identifying unresolved issues faster.
- Supports Fraud Detection in insurance claim calls.

### Next Steps
- Scale with larger datasets for better accuracy.
- Test with different LLMs (e.g., Claude, Gemini).
- Deploy in live customer support systems.

