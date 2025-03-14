import os
from flask import Flask, render_template, request
import pickle

tokenizer = pickle.load(open('models/cv.pkl', 'rb'))
model = pickle.load(open('models/clf.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
   text = request.form.get('email-content')
   tokens = tokenizer.transform([text])
   prediction = model.predict(tokens)
   prediction = 1 if prediction == 1 else -1
   return render_template('index.html', prediction=prediction, text=text)

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)