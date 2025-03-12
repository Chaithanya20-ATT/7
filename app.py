from flask import Flask, request, jsonify, render_template  # Add 'render_template' to the imports
from textblob import TextBlob

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the index.html template

# Route for sentiment analysis API
@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json  # Access JSON data from the request
    text = data.get('text')
    if not text:
        return jsonify({'error': 'No text provided'}), 400

    # Perform sentiment analysis
    blob = TextBlob(text)
    sentiment = blob.sentiment

    # Determine sentiment label
    if sentiment.polarity > 0:
        sentiment_label = 'Positive'
    elif sentiment.polarity < 0:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    return jsonify({
        'text': text,
        'sentiment': sentiment_label,
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity
    })

if __name__ == '__main__':
    app.run(debug=True)