import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    wordList = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll('a', {'class': 'title'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            wordList.append(each_word)
    clean_up_list(wordList)


def clean_up_list(wordlist):
    cleanWordList = []
    for word in wordlist:
        symbols = "!@#$%^&*()_\"+<>-.,?/:;{}[]|"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            print(word)
            cleanWordList.append(word)

    create_dictionary(cleanWordList)

def create_dictionary(cleanWordList):
    word_count = {}
    for word in cleanWordList:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    # sort dictionary

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)





start('https://thenewboston.com/forum/recent_activity.php')
