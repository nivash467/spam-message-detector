# 📧 Spam Message Detector

A Machine Learning-powered Spam Message Detection application built using Python, Scikit-learn, and Streamlit. The application classifies text messages as **Spam** or **Not Spam** using the Naive Bayes algorithm and Natural Language Processing (NLP) techniques.

## 📌 Project Overview

Spam messages are unwanted messages that often contain advertisements, scams, or malicious content. This project uses Machine Learning to automatically classify messages as Spam or Not Spam based on their text content.

The application provides a simple and interactive web interface where users can enter a message and instantly receive a prediction.

---

## 🚀 Features

- Detects whether a message is Spam or Not Spam.
- Interactive web interface built with Streamlit.
- Uses Natural Language Processing (NLP) techniques.
- Implements Count Vectorization for text feature extraction.
- Uses Multinomial Naive Bayes for classification.
- Fast and lightweight prediction system.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- CountVectorizer
- Multinomial Naive Bayes

---

## 📂 Project Structure

```text
Spam-Message-Detector/
│
├── app.py
├── spam.csv
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

The dataset contains two columns:

| Column Name | Description |
|------------|-------------|
| Category | Spam or Ham |
| Message | Text message content |

Example:

| Category | Message |
|----------|----------|
| ham | Hey, are you coming today? |
| spam | Congratulations! You won ₹10,000. Claim now! |

---

## ⚙️ How It Works

### 1. Data Preprocessing
- Load the dataset using Pandas.
- Remove duplicate entries.
- Convert labels:
  - ham → Not Spam
  - spam → Spam

### 2. Feature Extraction
- Convert text into numerical features using CountVectorizer.
- Remove common English stop words.

### 3. Model Training
- Split data into training and testing sets.
- Train a Multinomial Naive Bayes classifier.

### 4. Prediction
- User enters a message.
- The message is transformed using the trained vectorizer.
- The model predicts whether the message is Spam or Not Spam.

---

## 🔧 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/spam-message-detector.git

cd spam-message-detector
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📦 Required Libraries

Create a `requirements.txt` file containing:

```text
streamlit
pandas
scikit-learn
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 🎯 Machine Learning Model

### Algorithm Used
- Multinomial Naive Bayes

### Text Processing
- CountVectorizer
- English stop-word removal

### Train-Test Split
- 80% Training Data
- 20% Testing Data

---

## 💡 Sample Messages

### Not Spam

```text
Hey, let's meet tomorrow for lunch.
```

### Spam

```text
Congratulations! You've won a free iPhone. Click here to claim now.
```

---

## 🎯 Learning Outcomes

Through this project, you will learn:

- Text preprocessing using NLP techniques.
- Feature extraction with CountVectorizer.
- Building a classification model using Naive Bayes.
- Developing interactive ML applications using Streamlit.
- Deploying Machine Learning projects.

---

## 🔮 Future Enhancements

- Support for Email Spam Detection.
- Use TF-IDF Vectorization.
- Improve accuracy with advanced ML models.
- Add model performance metrics.
- Deploy on Streamlit Cloud.

---

## 👨‍💻 Author

**Nivash M**

BE Computer Science and Engineering (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, Data Science, and NLP.

⭐ If you found this project useful, consider giving it a star on GitHub!
