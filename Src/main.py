#!/usr/bin/env python
# coding: utf-8

# In[2]:

from flask import Flask, render_template, request
from src.preprocessing import extract_customer_responses
from src.model import analyze_transcript

# Define Flask App
app = Flask(__name__)

# Define Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "<h2>⚠️ No file uploaded.</h2><a href='/'>⬅️ Go Back</a>"

        file = request.files["file"]
        if file.filename == "":
            return "<h2>⚠️ No file selected.</h2><a href='/'>⬅️ Go Back</a>"

        # Read transcript content
        transcript_text = file.read().decode("utf-8")

        # Extract customer responses
        customer_text = extract_customer_responses(transcript_text)

        if not customer_text.strip():  # No customer response found
            return "<h2>⚠️ No customer responses found in transcript.</h2><a href='/'>⬅️ Go Back</a>"

        # Get AI analysis
        sentiment, sentiment_icon, outcome, outcome_icon = analyze_transcript(transcript_text)

        return f"""
        
    
        <h2>📞 AI-Powered Call Analysis</h2>
        
        <h3>📜 Full Call Transcript</h3>
        <textarea rows="8" cols="100" readonly>{transcript_text}</textarea>
        
        <h3>📃 Extracted Customer Responses</h3>
        <textarea rows="8" cols="100" readonly>{customer_text}</textarea>
        
        <h3>📝 AI Analysis Result</h3>
        <div style="background:#f9f9f9; padding:15px; border-radius:8px; margin-top:20px; font-size:18px;">
            <p style="font-size: 24px;"><strong>Sentiment:</strong> {sentiment_icon} {sentiment}</p>
            <p style="font-size: 24px;"><strong>Call Outcome:</strong> {outcome_icon} {outcome}</p>
        </div>
        <br>
        <a href="/">⬅️ Upload Another File</a>
        """

    return """
    <h2>📞 AI-Powered Call Analysis</h2>
    <p>Upload a call transcript (.txt) and analyze sentiment & call outcome.</p>
    <form action="/" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept=".txt" required>
        <br><br>
        <button type="submit">🔍 Run Analysis</button>
    </form>
    """



if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:
