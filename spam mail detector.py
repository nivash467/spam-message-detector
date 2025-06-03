import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st

# Load dataset
data = pd.read_csv("E:\\spam mail detector\\spam.csv")


data.drop_duplicates(inplace=True)
data['Category'] = data['Category'].replace(['ham', 'spam'], ['Not Spam', 'Spam'])

mess = data['Message']
cat = data['Category']

# Split data
mess_train, mess_test, cat_train, cat_test = train_test_split(mess, cat, test_size=0.2)

# Vectorize
cv = CountVectorizer(stop_words='english')
features = cv.fit_transform(mess_train)

# Train model
model = MultinomialNB()
model.fit(features, cat_train)


features_test = cv.transform(mess_test)

# Streamlit GUI
st.title("Spam Message Detector")
input_message = st.text_area("Enter a message to check if it's Spam")

if st.button("Check"):
    if input_message.strip():
        input_vector = cv.transform([input_message])
        prediction = model.predict(input_vector)[0]
        if prediction == "Spam":
            st.error("❌ This message is Spam.")
        else:
            st.success("✅ This message is Not Spam.")
    else:
        st.warning("Please enter a message.")