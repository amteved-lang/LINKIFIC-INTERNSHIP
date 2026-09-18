# 📝 Natural Language Processing

## Project Overview

This project demonstrates the basics of Natural Language Processing (NLP) using Python.

A small text dataset related to Artificial Intelligence and Machine Learning was used to perform text preprocessing and TF-IDF vectorization.

## Learning Objectives

- Understand basic NLP concepts
- Learn text preprocessing techniques
- Perform tokenization
- Remove stopwords
- Convert text into numerical features
- Understand TF-IDF vectorization

## Text Preprocessing

The following preprocessing techniques were implemented:

### Lowercasing

All text was converted to lowercase to maintain consistency during text processing.

### Tokenization

Text was divided into individual words using NLTK tokenization.

### Stopword Removal

Common English stopwords were removed from the tokenized text.

### Special Character Removal

Non-alphabetic characters were removed during preprocessing.

## TF-IDF Vectorization

TF-IDF (Term Frequency-Inverse Document Frequency) was used to convert the processed text into numerical feature vectors.

TF-IDF gives higher importance to words that are more informative within the dataset and lower importance to words that occur frequently across documents.

## Dataset

The dataset contains 10 short text documents related to:

- Artificial Intelligence
- Machine Learning
- Natural Language Processing
- Python
- Data Science
- Deep Learning

## Workflow

1. Load the text dataset
2. Convert text to lowercase
3. Remove special characters
4. Tokenize text
5. Remove stopwords
6. Apply TF-IDF vectorization
7. Generate TF-IDF feature matrix
8. Save TF-IDF output

## Technologies Used

- Python
- Pandas
- NLTK
- Scikit-learn
- Jupyter Notebook
- VS Code
- Git
- GitHub

## Project Files

- `nlp_text_preprocessing.ipynb` - NLP practice notebook
- `text_dataset.csv` - Text dataset
- `tfidf_output.csv` - Generated TF-IDF feature matrix
- `README.md` - Project documentation

## References

NLTK Documentation:

https://www.nltk.org/

Scikit-learn TF-IDF Documentation:

https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction

## Conclusion

This project provided practical experience with basic Natural Language Processing. Text preprocessing techniques such as lowercasing, tokenization, stopword removal, and special character removal were implemented. TF-IDF was then used to transform the processed text into numerical features suitable for Machine Learning applications.
