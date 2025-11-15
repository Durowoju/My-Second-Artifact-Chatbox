# My-Second-Artifact-Chatbox 
_A Collaborative AI Chatbot Built from Real Student Stories_

## 📌 Project Overview
This project showcases a custom chatbot built from TED-style presentation scripts written by multiple graduate students. The chatbot can answer questions about each speaker, summarize their talk, and respond in a motivational, personalized tone using curated content.

The core knowledge base is a structured dataset extracted from student TED-style talk outlines and introductions. :contentReference[oaicite:0]{index=0}

## 🧠 What the Chatbot Can Do
- Answer questions about each speaker’s background, vision, and key message  
- Provide short motivational summaries based on a chosen speaker  
- List speakers by theme or tag (e.g., growth, AI, courage, career change)  
- Demonstrate how structured text content can power a simple conversational agent  

## 🛠️ Technologies Used
- Python 3.x  
- JSON for structured data storage  
- Simple rule-based retrieval over a curated dataset  

_No external NLP libraries are required for this basic portfolio version._

## 📂 Repository Structure
```text
data/
  presentations.json      # Structured TED-style speaker data
src/
  chatbot.py              # Simple console-based chatbot
README.md                 # Project documentation
requirements.txt          # Dependencies (minimal)
