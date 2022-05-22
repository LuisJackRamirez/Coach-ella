import spacy
from career import asked_credits
from horario import asked_schedule
from kardex import asked_grades
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess_phrase (phrase):
    # Palabras stop
    stop_words = set(stopwords.words('spanish'))

    # Tokenizar la cadena de entrada
    word_tokens = word_tokenize (phrase)
    # print (word_tokens)

    # Eliminar palabras stop
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            #filtered_sentence.append (w + ' ')
            filtered_sentence.append (w)

    return ' '.join(filtered_sentence)

def lemmatize_phrase (phrase):
    # Cargar base de datos
    nlp = spacy.load("es_core_news_sm")

    # Tokenizar la cadena de entrada
    doc = nlp (phrase)

    # Lematización
    lemmas = []
    for token in doc:
        if (token.pos_) != 'PUNCT':
            lemmas.append(token.lemma_)

    return lemmas

""" Query processing """
def read_query (query):
    preprocessed_phrase = preprocess_phrase (query)
    lemmatized_phrase = lemmatize_phrase (preprocessed_phrase)
    print (lemmatized_phrase)

    """ Analyzes query and finds operation """
    for lemma in lemmatized_phrase:
        if asked_schedule (lemma) == True:
            return 1
        elif asked_grades (lemma) == True:
            return 2
        elif asked_credits (lemma) == True:
            return 3

    return -1
