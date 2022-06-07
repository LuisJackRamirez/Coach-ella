import spacy

from coachella.career import asked_credits
from coachella.horario import asked_schedule
from coachella.kardex import asked_grades
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_phrase (phrase):
    # Stop words
    stop_words = set(stopwords.words('spanish'))

    # Tokenize query for future processing
    word_tokens = word_tokenize (phrase)

    # Remove stop words
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append (w)

    return ' '.join(filtered_sentence)

def lemmatize_phrase (phrase):
    # Load spacy database
    nlp = spacy.load("es_core_news_sm")

    # Tokenize query
    doc = nlp (phrase)

    # Lemmatization
    lemmas = []
    for token in doc:
        if (token.pos_) != 'PUNCT':
            lemmas.append(token.lemma_)

    return lemmas

# Query processing
def read_query (query):
    preprocessed_phrase = preprocess_phrase (query)

    materias_kw = [
        'objetos',
        'probabilidad',    
        'diferenciales',
        'estructuras',
        'lineal',
        'económicos',
        'vectorial',
        'terminal'
    ]

    materias = []
    for word in preprocessed_phrase.split(' '):
        print (word)
        if word in materias_kw:
            materias.append (word)

    lemmatized_phrase = lemmatize_phrase (preprocessed_phrase)
    print (lemmatized_phrase)

    # Analyzes query and finds operation
    for lemma in lemmatized_phrase:
        if asked_schedule (lemma) == True:
            return 1
        elif asked_grades (lemma) == True:
            return 2
        elif asked_credits (lemma) == True:
            return 3

    return -1, materias
