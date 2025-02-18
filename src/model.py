#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
import os
from src.preprocessing import extract_customer_responses

# Loads API key from env variable
openai.api_key = os.getenv("OPENAI_API_KEY")  

# Define Few-Shot Prompt
FEW_SHOT_PROMPT = """
You are an AI assistant trained in customer service analysis. Your task is to classify customer transcripts.

### Instructions:
For each transcript, provide:
1. **Sentiment**: (Positive, Negative, Neutral)
2. **Call Outcome**: (Issue Resolved, Follow-up Needed)

### Examples:
1 Transcript: "I am very happy with the support. They solved my issue quickly!"
   Sentiment: Positive
   Call Outcome: Issue Resolved

2️ Transcript: "The service is terrible. My issue is still not fixed!"
   Sentiment: Negative
   Call Outcome: Follow-up Needed

3️ Transcript: "It was okay. Took longer than expected, but they helped me."
   Sentiment: Neutral
   Call Outcome: Issue Resolved

---

Now analyze the following customer transcript:
Transcript: "{text}"

Provide the response in this JSON format:
{{
  "sentiment": "...",
  "call_outcome": "..."
}}
"""

# Function to analyze transcript sentiment and call outcome using GPT-4 Turbo
def analyze_transcript(transcript):
    """
    Uses OpenAI's GPT-4 Turbo to classify sentiment and call outcome from the customer's responses.

    Args:
        transcript (str): The full call transcript.
    
    Returns:
        tuple: (sentiment, sentiment_icon, outcome, outcome_icon)
    """

    try:
        # Extract only the customer responses
        customer_text = extract_customer_responses(transcript)

        # If no customer responses found, return default values
        if not customer_text.strip():  
            return "No Customer Response", "❌", "No Data", "❌"

        # Format the prompt for the LLM
        prompt = FEW_SHOT_PROMPT.format(text=customer_text)

        # Send request to OpenAI's GPT-4 Turbo model
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
        )

        # Extract response from the model
        result = response.choices[0].message.content
        print("🔹 OpenAI Response:", result)  # Debugging print statement

        # Initialize default labels
        sentiment = "Neutral"
        sentiment_icon = "😐"
        outcome = "Follow-up Needed"
        outcome_icon = "🔄"

        # Check for sentiment classification in model response
        if "Positive" in result:
            sentiment = "Positive"
            sentiment_icon = "😊"
        elif "Negative" in result:
            sentiment = "Negative"
            sentiment_icon = "😡"

        # Check for call outcome classification in model response
        if "Resolved" in result:
            outcome = "Issue Resolved"
            outcome_icon = "✅"

        return sentiment, sentiment_icon, outcome, outcome_icon

    except Exception as e:
        # Handle API errors gracefully
        print("❌ OpenAI API Error:", e)
        return "Error", "❌", "Error", "❌"

# In[ ]:
