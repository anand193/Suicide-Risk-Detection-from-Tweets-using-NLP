import streamlit as st
import pickle

# Load the model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

# Page Config
st.set_page_config(page_title="Suicide Risk Detector", page_icon="💬", layout="centered")

# Main Title Section
st.title("💬 Suicide Risk Detection from Tweets")
st.subheader("Analyze a tweet to identify signs of potential suicide risk.")
st.caption("This app uses Natural Language Processing (NLP) to classify tweets as **Potential Suicide Post** or **Not Suicide Post**.")

# Sidebar Info
with st.sidebar:
    st.header("ℹ️ About This App")
    st.write("This app analyzes tweets and predicts whether they indicate potential suicide risk based on emotional and linguistic patterns.")
    st.markdown("""
    **How to use:**
    1. Paste a tweet in the input box below.
    2. Click on 'Analyze Tweet'.
    3. See the prediction and helpful advice.
    """)
    st.write("---")
    st.markdown("🧠 Built to support early intervention and mental health awareness.")

# Tweet Input Section
with st.container():
    st.markdown("### 📝 Paste the Tweet Below")
    user_input = st.text_area(
        "Tweet Content:",
        height=180,
        placeholder="e.g., I feel like giving up... nothing makes sense anymore."
    )

# Analyze Button and Prediction
if st.button("🔍 Analyze Tweet"):
    if user_input.strip():
        st.markdown("### 📢 Prediction")

        # Process and Predict
        data = [user_input]
        vectorized_data = cv.transform(data).toarray()
        prediction = model.predict(vectorized_data)

        if prediction[0] == 0:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.success("💚 Not a Suicide Post")
            with col2:
                st.markdown("""
                - The tweet doesn't show signs of suicidal thoughts.  
                - Continue monitoring for emotional well-being if needed.  
                """)
        else:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.error("🚨 Potential Suicide Post Detected")
            with col2:
                st.markdown("""
                - The tweet may indicate emotional distress or suicidal thoughts.  
                - Encourage seeking help or contact a mental health helpline.  
                - Support and empathy can make a big difference.  
                """)

    else:
        st.warning("⚠️ Please enter a tweet before analyzing.")

# Footer
st.divider()
st.markdown("### ❤️ Mental Health Awareness")
st.markdown("""
- If you or someone you know is struggling, please reach out to a trusted person or a helpline.  
- In India: Call **AASRA (91-9820466726)** or **Snehi (91-9582208181)**  
- In the US: Dial **988 (Suicide and Crisis Lifeline)**  
- Remember: You are not alone. Help is always available.
""")
st.markdown("Developed with ❤️ by **Anand Mehto**")