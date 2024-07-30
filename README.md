
# SMS SPAM CLASSIFIER

This project is an SMS spam classifier built using Streamlit, NLTK, scikit-learn, seaborn, wordcloud, and stop-words. The classifier aims to distinguish between spam and ham (non-spam) messages using machine learning techniques.


## Features

- Interactive Web App: Built with Streamlit for user-friendly interaction.
- Natural Language Processing: Utilizes NLTK and stop-words for text processing and feature extraction.
- Machine Learning: Implements models using scikit-learn to classify messages.
- Data Visualization: Uses seaborn and wordcloud for insightful visualizations of the data.


## Installation

1. Clone the repository:
```bash
  git clone https://github.com/yourusername/sms-spam-classifier.git
  cd sms-spam-classifier
```
2. Create a virtual environment:
```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

```

3. Install the required libraries:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```


## Usage

- Input: Enter or upload SMS messages.
- Classify: Click the classify button to see if the message is spam or ham.
- Visualize: View the wordcloud and other visualizations to understand the data distribution.



## Libraries Used

- Streamlit: For building the interactive web application.
- NLTK: For natural language processing and text cleaning.
- scikit-learn: For machine learning algorithms and model evaluation.
- seaborn: For data visualization and plotting.
- wordcloud: For generating word cloud visualizations.
- stop-words: For removing common stop words from the text.


## Model

The classifier is trained on a dataset of SMS messages, labeled as spam or ham. It uses a variety of text preprocessing techniques and machine learning models to achieve high accuracy.


## License

This project is licensed under the MIT License - see the [LICENSE](https://choosealicense.com/licenses/mit/) file for details.
