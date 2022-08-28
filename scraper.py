import pandas as pd #Analisa dados
import requests #Pega HTMLs
from bs4 import BeautifulSoup #Procura tag em HTMLs

class Scraper:
    def __init__(self):
        pass
    
    def scrape_pd_tables(self, url:str):
        data = pd.read_html(url)
        return data

    def scrape_tag(self, local:str, columns:list, font:str='url', tag:str='', attrs:dict={}):
        if font == 'url':
            html_text = requests.get(local).text
        elif font == 'input':
            html_text = ''
            for i in range(int(local)):
                html_text += input(f'\nHTML ({i}) > ')

        bsp_texto = BeautifulSoup(html_text, 'html.parser')

        table_tuples = bsp_texto.find_all(tag, attrs=attrs)
        
        dict_table = {i:[] for i in columns}

        for column in range(len(columns)):
            for tupl in table_tuples:
                list_keys = list(dict_table.keys())
                key = list_keys[column]
                text = tupl.contents[column].text
                dict_table[key].append(text)
        
        return pd.DataFrame(dict_table)


def main():
    scraper = Scraper()

    url = 'https://www.google.com/search?q=tabela+campeonato+brasileiro&client=firefox-b-e&biw=1920&bih=995&sxsrf=ALiCzsZdr1dmxvE_eqDZg7jRQfO7CQCtPw%3A1661708973236&ei=raoLY_yEDv-v5OUPl-yv4A0&oq=tabela+cam&gs_lcp=Cgdnd3Mtd2l6EAMYADILCAAQgAQQsQMQgwEyCAgAEIAEELEDMggIABCABBCxAzILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6CggAELEDEIMBEENKBAhBGABKBAhGGABQSFhyYK0KaAFwAXgAgAHkAYgBwgSSAQUwLjIuMZgBAKABAcgBCMABAQ&sclient=gws-wiz#sie=lg;/g/11sfc7_5p3;2;/m/0fnk7q;st;fp;1;;;'

    columns = [
        'GRUPO',
        'CÓDIGO',
        'DESCRIÇÃO'
    ]

    tag = 'h5'
    attrs = {}

    #data = scraper.scrape_table(url, columns, tag, attrs)
    data = scraper.scrape_pd_tables(url)

    for df in data:
        print(df.head)

if __name__ == '__main__':
    main()
