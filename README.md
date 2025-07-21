# Caprae-Challenge

🧠 AI-Powered Lead Generation Tool  
Caprae Capital – AI Readiness Challenge Submission
Author: Kona Uma Mahesh

---

📌 Overview

This project simulates a lead generation tool designed for B2B SaaS companies, enhanced with AI-inspired logic to prioritize leads based on strategic relevance. It reflects Caprae Capital’s goal of empowering portfolio companies with actionable, intelligent solutions — especially post-acquisition.

---

🎯 Objective

To build a tool in under 5 hours that:
- Simulates scraping SaaS company data
- Uses a lightweight AI-based scoring engine
- Offers an easy-to-use UI for filtering and exporting leads

---

🚀 Key Features

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🛠 **Lead Generator**  | Simulates scraping 5 realistic SaaS companies and their basic data          |
| 🤖 **AI Lead Scoring**| Scores each lead using keyword relevance in company bios                    |
| 🖥 **Streamlit UI**    | Clean interface to filter leads by score and preview them interactively     |
| 📁 **CSV Export**     | Allows downloading filtered leads for CRM or marketing use                  |

---

📁 Project Structure

    caprae-ai-readiness/
    ├── ai_scored_leads.csv # Output dataset with AI scores
    ├── app.py # Streamlit UI code
    ├── leadgen.py # Lead generation + scoring script
    ├── README.md # Full project documentation
    ├── report.md # 1-page submission report
    └── video_script.txt # Video walkthrough script (for recording)


---

🧠 AI Scoring Logic

Each company’s bio is analyzed for business-relevant keywords like:

- **ai**, **cloud**, **analytics**, **iot**
- **fintech**, **fraud**, **learning**, etc.

These keywords are assigned weights, and the total score ranks the lead’s relevance to SaaS business development needs.

---

💡 Business Value

By simulating how real AI lead scoring works:
- Sales teams can **focus on high-priority targets**
- Reduces time spent on low-conversion outreach
- Supports Caprae’s mission to **build better post-acquisition workflows**

---

⚙️ How to Run

    ✅ Install Dependencies

    pip install streamlit pandas

▶️ Start the App

      streamlit run app.py

Then go to http://localhost:8501 in your browser to explore the tool.

📊 Sample Output
   | Company     | Score | Match Examples              |
|-------------|:-----:|-----------------------------|
| RetailMax   |  9    | `"analytics"`, `"real-time"`|
| EduSmart    |  8    | `"AI"`, `"learning"`        |
| FinVision   |  8    | `"fintech"`, `"fraud"`      |


🔄 Future Enhancements
Given more time, the tool could evolve into a production-grade product with:

    🔍 Live scraping from LinkedIn/Crunchbase
    
    🧠 GPT/OpenAI-powered bio analysis
    
    ✅ Email validation + enrichment APIs
    
    🔄 CRM Integration (HubSpot, Salesforce)
    
    📊 ICP filtering by industry, funding, geography

🙋‍♂️ About Me
Name: Kona Uma Mahesh
Background: Python & Data Science enthusiast with interest in AI-driven automation and product development.

Why Caprae? 
  I'm deeply aligned with Caprae's vision of combining AI, creativity, and business intelligence to drive sustainable innovation.

📬 Final Notes
This repository was built in response to Caprae Capital’s AI Readiness Challenge and includes:

    📄 Python scripts
    
    🧠 AI logic
    
    🖥️ Interactive UI
    
    📝 1-page report
    
    🎥 Video script



