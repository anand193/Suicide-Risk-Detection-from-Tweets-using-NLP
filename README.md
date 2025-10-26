# 💬 Suicide Risk Detection from Tweets using NLP

A **Machine Learning–powered Streamlit web app** that detects potential suicide risk in tweets based on emotional and linguistic patterns.  
This project aims to support early identification of distress signals and promote mental health awareness using **Natural Language Processing (NLP)**.

---

![Project Logo](https://img.shields.io/badge/Streamlit-Deployed-green)
**Deployed Application:** [Visit the App](https://suicide-risk-detection-from-tweets-using-nlp-cfwhect59jva9pmv6.streamlit.app/)

This repository hosts the **Suicide Risk Detection from Tweets** project, an interactive web app built using **Python and Streamlit**.  
It uses a trained **Machine Learning model** to classify tweets as **Potential Suicide Post** or **Not Suicide Post**, helping to identify early warning signs and promote mental health awareness.

---

## 🚀 Features

- Classifies tweets as **Potential Suicide Post** or **Not Suicide Post**.  
- Uses **NLP preprocessing** (cleaning, tokenization, stopwords removal, lemmatization).  
- **Bag of Words / TF-IDF Vectorization** for text representation.  
- Machine Learning model (e.g., Logistic Regression or Naive Bayes) for classification.  
- Interactive and clean UI built with **Streamlit**.  
- Real-time prediction with instant feedback and mental health resources.

---

## 🛠️ Technologies Used

- Python 🐍  
- Streamlit 🌐  
- Scikit-learn 🤖  
- NLTK (Natural Language Toolkit)  
- Pickle (for saving trained model and vectorizer)

---

## 💡 How It Works

1. **User Input:** Paste a tweet or short text in the input box.  
2. **Text Preprocessing:**  
   - Converts to lowercase  
   - Removes punctuation, stopwords, and links  
   - Lemmatizes the text  
3. **Vectorization:** The cleaned text is converted into numerical form using TF-IDF or BoW.  
4. **Prediction:** The model predicts whether the tweet expresses **potential suicidal intent** or **not**.  
5. **Output:** The app displays a clear, color-coded result with safety advice.  

---

## 🧠 Model Overview

The model is trained on labeled tweets dataset containing both *“Potential Suicide Posts”* and *“Not Suicide Posts”*.  
It learns language patterns associated with emotional distress to make predictions accurately.

---

## 📈 Future Improvements
- Integrate with **Twitter API** for real-time tweet analysis.  
- Use **deep learning models** like LSTMs or BERT for better accuracy.  
- Add **confidence score** and explainability (e.g., highlighting key words).  
- Support for multilingual tweet analysis.  

---

## 🧡 Mental Health Disclaimer

This tool is **not a diagnostic system**. It is intended to assist research and awareness efforts in detecting potential risk indicators.  
If you or someone you know is struggling, please reach out to professional help:

- **India:** AASRA (91-9820466726), Snehi (91-9582208181)  
- **USA:** Dial 988 (Suicide and Crisis Lifeline)  
- **UK:** Samaritans (116 123)  

You are not alone. Help is always available. 💛

---

## 📧 Contact

Made with ❤️ by **Anand Mehto**  
🔗 [LinkedIn](https://www.linkedin.com/in/anandmehto)  
📂 GitHub: [anand193](https://github.com/anand193)
