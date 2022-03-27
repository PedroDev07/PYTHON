import requests
from bs4 import BeautifulSoup  
import operator
from collections import Counter





def start(url):

    word_list = [] #vai armazenar o conteúdo do site
    source_code = requests.get(url).text #source code vai receber a url 
# Baixar o HTML do site:
    soup = BeautifulSoup(source_code, 'html.parser')#transforma em html

    for each_text in soup.findAll('div', {'class': 'entry-content'}):#vai procurar por div cujo a classe tenha nome em entrycontent
        content = each_text.text #recebe o conteudo
        words = content.lower().split() #quebra o conteudo em linhas

    for each_word in words: #coloca tudo em lista
        word_list.append(each_word)
        clean_wordlist(word_list)



# Remove os caracteres especiais de wordlist, criando uma clean_list:

def clean_wordlist(word_list): #remove os simbolos indesejados

    clean_list = []

    symbols = '!@#$%&*()+-+=[]{}|\"/,.;:?<> '

    symbols += '–…'



    for word in word_list:#para cada palvara em wordlist

        for i in range(0, len(symbols)): #ele percorre do inicio ao fim 

            word = word.replace(symbols[i], '') #troca os simbolos por nada



        if len(word) > 0:

            clean_list.append(word)

            create_dictionary(clean_list)





def create_dictionary(clean_list):#seleciona as palavras mais utilizadas no site

    word_count = {}



    for word in clean_list:

        if word in word_count:

            word_count[word] += 1

        else:

            word_count[word] = 1



    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):

        print(f'{key} : {value}')



    c = Counter(word_count)

    top = c.most_common(10)





if __name__ == '__main__':


    url='https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar'

    start(url)