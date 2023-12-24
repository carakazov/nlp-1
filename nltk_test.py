import nltk

nltk.download("all")
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
import json

default_text = "Сегодня мы изучаем одну из библиотек для обработки естественного языка. Изучим разные случаи."
mistakes_text = "Содня   мы,  изучм  оду из  бимвиотек  для  овработки есесвенного язика.  Изучм  розные случаи."

multi_language_text = "Today мы изучаем библиотеку nltk для языка программирования Python. Она позволяет выплнять базовые алгоритмы NLP"
one_word_one_sentence_text = "Сегодня. Мы. Изучаем. Одну. Из. Библиотек. Для. Обработки. Естественного. Языка. Изучим. Разные. Случаи."
translit_text = "Segodnya my izuchaem odnu iz bibliotek dlya obrabotki estestvennogo yazyka. Izuchim raznye sluchai."

def tokenize_words(text):
    words = word_tokenize(text, language="russian")
    stop_words = stopwords.words("russian")
    filtered_words = list(filter(lambda word: word not in stop_words, words))
    return filtered_words


def lemmatize(words):
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word in words:
        lemmatized_words.append(lemmatizer.lemmatize(word))
    return lemmatized_words


def stemm_words(words_list):
    stemmer = SnowballStemmer(language="russian")
    stemmed_words = []
    for word in words_list:
        stemmed_words.append(stemmer.stem(word))
    return stemmed_words


def mark_words(words):
    marked_words = pos_tag(words, lang='rus')
    return marked_words


def write_in_json(content, path):
    words_in_json = json.dumps(content, ensure_ascii=False)
    json_file = open(path, "w")
    json_file.write(words_in_json)
    json_file.close()


def pipeline(text, result_file):
    tokenized_words = tokenize_words(text)
    lemmatized_words = lemmatize(tokenized_words)
    stemmed_words = stemm_words(lemmatized_words)
    marked_words = mark_words(stemmed_words)
    print(marked_words)
    write_in_json(marked_words, result_file)


pipeline(default_text, "results/default_result.json")
pipeline(mistakes_text, "results/mistakes_result.json")
pipeline(multi_language_text, "results/multi_language_result.json")
pipeline(one_word_one_sentence_text, "results/one_word_one_sentence_result.json")
pipeline(translit_text, "results/translit_result.json")
