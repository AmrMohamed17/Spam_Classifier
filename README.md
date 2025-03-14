# Spam Detective - Email Analysis Tool

A web application that analyzes email content to detect potential spam messages using machine learning.

## Live Demo

The application is deployed and accessible at: [https://spam-classifier-pied.vercel.app/](https://spam-classifier-pied.vercel.app/)

## Features

- Email content analysis using machine learning
- Real-time spam detection
- Sample email templates for testing
- User-friendly interface with loading animations
- Responsive design

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: scikit-learn
- **Deployment**: Vercel

## How It Works

The application uses a trained machine learning model to classify email content as spam or not spam. When a user submits an email for analysis, the content is processed by:

1. Tokenizing the text using a CountVectorizer (loaded from `cv.pkl`)
2. Passing the tokenized text to a classifier model (loaded from `clf.pkl`)
3. Returning the prediction to the user with appropriate styling

## Installation and Local Development

### Prerequisites

- Python 3.9
- pip

### Setup

1. Clone the repository
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the application:
```
python app.py
```
4. Open your browser and navigate to `http://localhost:5000`

## Deployment

This project is configured for deployment on Vercel using the following:

- `vercel.json` - Configuration for Vercel deployment
- `build.sh` - Installation script for dependencies

## Project Structure

- `app.py` - Main Flask application
- `models/` - Contains machine learning models (cv.pkl and clf.pkl)
- `templates/` - HTML templates (index.html)
- `requirements.txt` - Required Python packages
- `vercel.json` - Vercel deployment configuration
- `build.sh` - Build script for deployment

## License

[MIT License]

## Acknowledgments

- Uses Flask for the web framework
- Utilizes scikit-learn for machine learning capabilities
