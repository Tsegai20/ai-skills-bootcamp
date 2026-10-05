
import streamlit as st
from transformers import pipeline
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sentiment Analyzer", page_icon="🧠")
st.title("🧠 Sentiment Analyzer")
st.write("Built with HuggingFace Transformers and Streamlit")
st.divider()

@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

classifier = load_model()

text = st.text_area("Enter your text below", height=150,
    placeholder="Type something here...")

if st.button("Analyze Sentiment", type="primary"):
    if text.strip() == "":
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Analyzing..."):
            result = classifier(text)[0]
            label = result["label"]
            score = result["score"]

        if label == "POSITIVE":
            st.success(f"Sentiment: {label}")
        else:
            st.error(f"Sentiment: {label}")

        st.metric("Confidence Score", f"{score:.2%}")

        fig, ax = plt.subplots(figsize=(6, 2))
        ax.barh(["Confidence"], [score],
                color="green" if label == "POSITIVE" else "red")
        ax.set_xlim(0, 1)
        st.pyplot(fig)

        with st.expander("Raw output"):
            st.json(result)