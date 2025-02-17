#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re

# Function to extracts only the customer responses from a call transcript.

def extract_customer_responses(transcript):
    
    #Assumes that agent and customer parts are separated by labels like "Agent:" or "Member:".
    return " ".join(re.findall(r"Member: (.+)", transcript))


# In[ ]:




