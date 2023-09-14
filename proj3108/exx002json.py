import requests
import json 

def translate(text, lang):
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    params = {
      'key': 'trnsl.1.1.20230831T144244Z.c6f503de2167ce05.c5e2111a7ec5b04862675a46fa39747ed509d125',
      'text': text,
      'lang': lang,
    }
   
    response = requests.get(url, params=params)
    return response.json()['text'][0]


def main():
    # carregando texto de input.json
    with open('imput.json', 'r') as file:
        data = json.load(file)
        text_to_translate = data['text']

    translation_pt = translate(text_to_translate, 'pt')
    translation_es = translate(text_to_translate, 'es')

    translations = {
        "Tradução em Português": translation_pt,
        "Tradução em Espanhol": translation_es
    }

    # gravando as traduções em output.json
    with open('output.json', 'w') as file:
        json.dump(translations, file)
    
if __name__ == '__main__':
    main()
