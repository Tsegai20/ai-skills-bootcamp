# Day 1 — Streamlit AI Apps

**AI Skills Bootcamp | Tsegai Yhdego, PhD**

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.38-red)](https://streamlit.io)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow)](https://huggingface.co)

---

## What I Built

Two production-ready Streamlit web apps demonstrating real-time ML inference and LLM integration.

---

## App 1 — Sentiment Analyzer

Real-time text sentiment analysis using HuggingFace distilbert-base-uncased-finetuned-sst-2-english.

**What it does:**
- Accepts any text input
- Runs HuggingFace transformer model inference
- Returns POSITIVE/NEGATIVE prediction with confidence score
- Displays bar chart visualization of confidence

**Stack:** Streamlit · HuggingFace Transformers · PyTorch · Matplotlib

```bash
pip install streamlit transformers torch matplotlib
streamlit run app.py
```

---

## App 2 — AI Research Explorer

Interactive multi-input research analysis tool powered by Groq LLaMA.

**What it does:**
- Select research domain from 8 options including Intelligent Transportation, UAV Systems, Manufacturing, Healthcare AI
- Multi-select ML techniques to compare across 10 options
- Adjust analysis depth with slider from 1 to 5
- Enter custom research question
- Generates real-time bar chart and radar chart of technique relevance scores
- Runs AI analysis via Groq LLaMA API
- Download results as text file

**Stack:** Streamlit · Plotly · Groq LLaMA API · Pandas

```bash
pip install streamlit plotly groq pandas
streamlit run app2.py
```

**API:** Requires free Groq API key from console.groq.com

---

## Key Concepts Demonstrated

| Concept | Implementation |
|---------|---------------|
| HuggingFace pipeline API | Off-the-shelf sentiment model inference |
| Model caching | @st.cache_resource prevents reloading on every interaction |
| Interactive widgets | selectbox, multiselect, slider, text_area |
| Real-time charts | Plotly bar and radar charts update on selection change |
| LLM API integration | Groq LLaMA generates contextual technical analysis |
| Prompt engineering | Dynamic prompts constructed from user inputs |
| File download | Analysis exported as .txt file |

---

## Project Structure
day1/
├── app.py # Sentiment Analyzer
├── app2.py # AI Research Explorer
├── requirements.txt # Dependencies
└── README.md


---

## Run Locally

```bash
git clone https://github.com/Tsegai20/ai-skills-bootcamp-day1.git
cd ai-skills-bootcamp-day1
pip install -r requirements.txt

# Run Sentiment Analyzer
streamlit run app.py

# Run AI Research Explorer
streamlit run app2.py
```

---

## Skills Added to Resume

- Streamlit web app development
- HuggingFace Transformers inference pipeline
- Plotly interactive data visualization
- Groq LLaMA API integration
- Multi-input interactive UI design
- Real-time data-driven charts
- Prompt engineering for technical analysis

---

## Part of AI Skills Bootcamp

| Day | Project | Repo |
|-----|---------|------|
| **1** | **Streamlit AI Apps** | **You are here** |
| 2 | HuggingFace Fine-Tuning | Coming |
| 3 | FastAPI ML Serving | Coming |
| 4 | RAG Pipeline | Coming |
| 5 | MLflow + Federated Learning | Coming |
| 6 | Docker Federated System | [ai-skills-bootcamp6](https://github.com/Tsegai20/ai-skills-bootcamp6) |

---

## Author

**Tsegai Yhdego, PhD**  
Industrial Engineering — Machine Learning and Optimization  
Assistant Director, R-SEAT Center, FAMU-FSU  
USDOT-Funded Research — Intelligent Transportation and Autonomous Systems  
[GitHub](https://github.com/Tsegai20) · [LinkedIn](https://www.linkedin.com/in/tsegai-yhdego-ph-d-b6209b118/)
