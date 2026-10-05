import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from groq import Groq
import pandas as pd

st.set_page_config(
    page_title="AI Research Explorer",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Research Explorer")
st.write("Explore AI and ML techniques across research domains — powered by Groq")
st.divider()

# Sidebar
st.sidebar.header("Configure Your Analysis")

domain = st.sidebar.selectbox(
    "Select Research Domain",
    options=[
        "Intelligent Transportation",
        "Autonomous UAV Systems",
        "Manufacturing Quality Control",
        "Supply Chain Optimization",
        "Healthcare AI",
        "Financial Forecasting",
        "Natural Language Processing",
        "Computer Vision"
    ]
)

techniques = st.sidebar.multiselect(
    "Select ML Techniques to Compare",
    options=[
        "Deep Learning (CNN/RNN/LSTM)",
        "Federated Learning",
        "Reinforcement Learning",
        "Transformer Models",
        "Gradient Boosting",
        "Random Forest",
        "Optimization (OR/LP)",
        "Anomaly Detection",
        "Generative AI",
        "Causal Inference"
    ],
    default=["Deep Learning (CNN/RNN/LSTM)", "Federated Learning", "Transformer Models"]
)

complexity = st.sidebar.slider(
    "Analysis Depth",
    min_value=1,
    max_value=5,
    value=3,
    help="1 = Brief overview, 5 = Deep technical analysis"
)

question = st.sidebar.text_area(
    "Your Research Question",
    placeholder="e.g. How can federated learning improve privacy in UAV systems?",
    height=100
)

api_key = st.sidebar.text_input(
    "Groq API Key",
    type="password",
    placeholder="gsk_..."
)

# Relevance scores database
domain_scores = {
    "Intelligent Transportation": {
        "Deep Learning (CNN/RNN/LSTM)": 92,
        "Federated Learning": 78,
        "Reinforcement Learning": 85,
        "Transformer Models": 70,
        "Gradient Boosting": 65,
        "Random Forest": 60,
        "Optimization (OR/LP)": 95,
        "Anomaly Detection": 80,
        "Generative AI": 55,
        "Causal Inference": 72
    },
    "Autonomous UAV Systems": {
        "Deep Learning (CNN/RNN/LSTM)": 95,
        "Federated Learning": 70,
        "Reinforcement Learning": 98,
        "Transformer Models": 65,
        "Gradient Boosting": 50,
        "Random Forest": 45,
        "Optimization (OR/LP)": 90,
        "Anomaly Detection": 85,
        "Generative AI": 60,
        "Causal Inference": 55
    },
    "Manufacturing Quality Control": {
        "Deep Learning (CNN/RNN/LSTM)": 90,
        "Federated Learning": 95,
        "Reinforcement Learning": 60,
        "Transformer Models": 75,
        "Gradient Boosting": 70,
        "Random Forest": 72,
        "Optimization (OR/LP)": 80,
        "Anomaly Detection": 98,
        "Generative AI": 65,
        "Causal Inference": 68
    },
    "Supply Chain Optimization": {
        "Deep Learning (CNN/RNN/LSTM)": 75,
        "Federated Learning": 65,
        "Reinforcement Learning": 80,
        "Transformer Models": 60,
        "Gradient Boosting": 85,
        "Random Forest": 80,
        "Optimization (OR/LP)": 98,
        "Anomaly Detection": 75,
        "Generative AI": 55,
        "Causal Inference": 82
    },
    "Healthcare AI": {
        "Deep Learning (CNN/RNN/LSTM)": 92,
        "Federated Learning": 98,
        "Reinforcement Learning": 70,
        "Transformer Models": 90,
        "Gradient Boosting": 75,
        "Random Forest": 72,
        "Optimization (OR/LP)": 65,
        "Anomaly Detection": 88,
        "Generative AI": 85,
        "Causal Inference": 90
    },
    "Financial Forecasting": {
        "Deep Learning (CNN/RNN/LSTM)": 88,
        "Federated Learning": 72,
        "Reinforcement Learning": 75,
        "Transformer Models": 82,
        "Gradient Boosting": 95,
        "Random Forest": 90,
        "Optimization (OR/LP)": 85,
        "Anomaly Detection": 92,
        "Generative AI": 70,
        "Causal Inference": 88
    },
    "Natural Language Processing": {
        "Deep Learning (CNN/RNN/LSTM)": 85,
        "Federated Learning": 70,
        "Reinforcement Learning": 65,
        "Transformer Models": 99,
        "Gradient Boosting": 45,
        "Random Forest": 40,
        "Optimization (OR/LP)": 50,
        "Anomaly Detection": 60,
        "Generative AI": 98,
        "Causal Inference": 55
    },
    "Computer Vision": {
        "Deep Learning (CNN/RNN/LSTM)": 99,
        "Federated Learning": 75,
        "Reinforcement Learning": 70,
        "Transformer Models": 90,
        "Gradient Boosting": 40,
        "Random Forest": 38,
        "Optimization (OR/LP)": 55,
        "Anomaly Detection": 85,
        "Generative AI": 88,
        "Causal Inference": 50
    }
}

# Charts section
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📊 Technique Relevance Scores")
    if techniques:
        scores = domain_scores.get(domain, {})
        selected_scores = {t: scores.get(t, 50) for t in techniques}

        df = pd.DataFrame({
            "Technique": list(selected_scores.keys()),
            "Relevance Score": list(selected_scores.values())
        })

        fig_bar = px.bar(
            df,
            x="Relevance Score",
            y="Technique",
            orientation="h",
            color="Relevance Score",
            color_continuous_scale="viridis",
            title=f"Technique Relevance for {domain}",
            range_x=[0, 100]
        )
        fig_bar.update_layout(height=400)
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("Select at least one ML technique from the sidebar.")

with col2:
    st.subheader("🕸️ Radar Chart — Technique Profile")
    if len(techniques) >= 3:
        scores = domain_scores.get(domain, {})
        selected_scores = {t: scores.get(t, 50) for t in techniques}

        categories = list(selected_scores.keys())
        values = list(selected_scores.values())
        values.append(values[0])
        categories.append(categories[0])

        fig_radar = go.Figure(data=go.Scatterpolar(
            r=values,
            theta=categories,
            fill="toself",
            line_color="rgba(99, 110, 250, 0.8)",
            fillcolor="rgba(99, 110, 250, 0.2)"
        ))

        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            title=f"Technique Profile — {domain}",
            height=400
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    else:
        st.info("Select at least 3 techniques to see the radar chart.")

# Comparison table
st.divider()
st.subheader("📋 Technique Comparison Table")

if techniques:
    scores = domain_scores.get(domain, {})
    comparison_data = []
    for t in techniques:
        score = scores.get(t, 50)
        if score >= 90:
            level = "⭐ Excellent"
        elif score >= 75:
            level = "✅ Strong"
        elif score >= 60:
            level = "👍 Good"
        else:
            level = "📌 Moderate"

        comparison_data.append({
            "Technique": t,
            "Relevance Score": score,
            "Fit Level": level
        })

    comparison_df = pd.DataFrame(comparison_data)
    comparison_df = comparison_df.sort_values("Relevance Score", ascending=False)
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)

# AI Analysis section
st.divider()
st.subheader("🤖 AI Powered Research Analysis")

if st.button("Generate Analysis", type="primary"):
    if not techniques:
        st.warning("Please select at least one ML technique.")
    elif not question.strip():
        st.warning("Please enter a research question.")
    elif not api_key.strip():
        st.warning("Please enter your Groq API key.")
    else:
        with st.spinner("Analyzing your research question..."):

            depth_map = {
                1: "brief 2-3 sentence",
                2: "concise one paragraph",
                3: "detailed 3-4 paragraph",
                4: "comprehensive technical",
                5: "in-depth expert level"
            }

            prompt = f"""You are an expert AI researcher specializing in {domain}.

The user wants a {depth_map[complexity]} analysis of the following:

Research Question: {question}

ML Techniques to focus on: {', '.join(techniques)}

Domain: {domain}

Provide:
1. Direct answer to the research question
2. How each selected technique applies to this domain
3. Key challenges and opportunities
4. Recommended approach

Be specific and technical."""

            try:
                client = Groq(api_key=api_key)

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=1000,
                    temperature=0.7
                )

                analysis = response.choices[0].message.content

                st.markdown("### Analysis Results")
                st.markdown(analysis)

                # Metrics row
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Domain", domain)
                with col_b:
                    st.metric("Techniques Analyzed", len(techniques))
                with col_c:
                    st.metric("Analysis Depth", f"{complexity}/5")

                st.download_button(
                    label="📥 Download Analysis",
                    data=analysis,
                    file_name=f"analysis_{domain.replace(' ', '_')}.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Check your API key at console.groq.com")

st.divider()
st.caption("Built by Tsegai Yhdego — PhD Industrial Engineering | AI/ML Researcher | R-SEAT Center FAMU-FSU")