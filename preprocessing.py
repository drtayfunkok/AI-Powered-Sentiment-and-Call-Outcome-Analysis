#!/usr/bin/env python
# coding: utf-8

# In[1]:

import os  
import re 

# Function to extract only customer responses from the transcript
def extract_customer_responses(transcript):
    """
    Extracts only the customer's responses from a full conversation transcript.
    
    Args:
        transcript (str): The full call transcript.
    
    Returns:
        str: A cleaned version containing only the customer's responses.
    """
    return " ".join(re.findall(r"Member: (.+)", transcript))  # Extracts lines starting with "Member: "

# In[ ]:




