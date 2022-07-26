import os, requests, sys
import pandas as pd
from bs4 import BeautifulSoup


def extract_article(filename):
    """This function extracts text from the articles including heading and paragraphs"""
    input_file = str(filename)
    input_file = pd.read_excel(input_file)
    url_list = [str(link) for link in input_file['URL']]
    # counter for file names
    count = 1

    try:
        for url in url_list:
            response = requests.get(url, headers={'User-Agent': 'XY'})
            soup = BeautifulSoup(response.text, 'lxml')
            # find the header
            header = soup.find('div', class_='td-post-header')
            header = header.h1
            # find the content
            content = soup.find('div', class_='td-post-content')
            # write the extracted article to new file
            file_name = "files/articles/URL_"+str(count)+".txt"
            with open(file_name, 'w', encoding='utf-16') as file:
                file.write(header.text)
                file.write(content.text)

            count+=1
    except:
        print("Some error occured, while parsing at:")
        print(url)
    else:
        print("Articles extracted completely!")