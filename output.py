from text_preprocessing import textprocessing
import pandas as pd
import joblib

vectorizer = joblib.load('vector.pkl')
model = joblib.load('model.pkl')

import pandas as pd

def finalOutput(text):
    try:
        labels = {
            0 : "negative",
            1 : "neutral",
            2 : "positive"
        }
        series = pd.Series([text])
        reduced_text = series.apply(textprocessing)
        vector = vectorizer.transform(reduced_text)
        prediction = model.predict(vector)
        return labels[prediction[0]]
    except Exception as e:
        print("An error occurred:", e)  
        return "Error"
    
print(finalOutput("He is very depressed"))



