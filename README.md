# TextClassification

Experimented with classifiers to automate essay grading

### Data files
- train.tsv
- test.tsv

### Data processing
- Removed punctuations 
- Removed stop words with NLTK, also customized an additional list of words to remove (e.g., "dear", "caps#", "num#") that is specific to this dataset
- Stemming/lemmatization
- Tokenization

### Feature selection
- Constructed the TF-IDF weights to represent textual data
- TF-IDF matrix contains information on the importance of tokens. For example, the token "computer" appears frequently in essays, but it does not effectively indicate the quality of essays. By using TF-IDF, the importance of frequently used words get reduced, while the importance of less frequently used words increase. This help to differentiate among essays.


### Model selection
(1)Experimented with the Ridge model to aviod overfitting (test MSE - 1.04)
(2)Experimented with the SVM model. SVM model works well with unstructred data, such as texual data in this essay grading task. 
-- SVM benchmark model (without tuning hyperparameters): test MSE is 3.23
-- SVM hyperparameter tuing (using GridSearch): test MSE is 1.22
(3) Experimented with the Universal Sentence Encoder
