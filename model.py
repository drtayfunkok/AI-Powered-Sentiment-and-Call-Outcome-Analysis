#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai
import os

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
1️⃣ Transcript: "I am very happy with the support. They solved my issue quickly!"
   Sentiment: Positive
   Call Outcome: Issue Resolved

2️⃣ Transcript: "The service is terrible. My issue is still not fixed!"
   Sentiment: Negative
   Call Outcome: Follow-up Needed

3️⃣ Transcript: "It was okay. Took longer than expected, but they helped me."
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

def analyze_transcript(transcript):
    
    try:
        # Extract only customer responses
        customer_text = extract_customer_responses(transcript)

        if not customer_text.strip():  # If no customer response found
            return "No Customer Response", "❌", "No Data", "❌"

        # 
        prompt = prompt = FEW_SHOT_PROMPT.format(text=customer_text)
        
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
        )

        result = response.choices[0].message.content

        print("🔹 OpenAI Response:", result)  # Debugging

        # Extract sentiment & call outcome
        sentiment = "Neutral"
        outcome = "Follow-up Needed"

        if "Positive" in result:
            sentiment = "Positive"
            sentiment_icon = "😊"
        elif "Negative" in result:
            sentiment = "Negative"
            sentiment_icon = "😡"
        else:
            sentiment_icon = "😐"

        if "Resolved" in result:
            outcome = "Issue Resolved"
            outcome_icon = "✅"
        else:
            outcome_icon = "🔄"

        return sentiment, sentiment_icon, outcome, outcome_icon

    except Exception as e:
        print("❌ OpenAI API Error:", e)
        return "Error", "❌", "Error", "❌"


# In[ ]:




