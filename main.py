from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

sentence = "saya bangga jadi warga nahdlatul ulama sidoarjo"
words = word_tokenize(sentence)

for word in words:
    print(word + ":" + ps.stem(word))
