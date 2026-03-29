import json
import os

print("\n-- Dictionary --\n\n- 'C' to close\n- 'L' to choose the language")

language = "English"
forbidden = r"0123456789\|/:;+*[]@#$%¨()£¢¬"

ARCHIVE = os.path.dirname(__file__)
FOLDER = os.path.dirname(ARCHIVE)

WORDS = os.path.join(FOLDER, "words.json")
with open(WORDS, "r", encoding="utf-8") as f: words = json.load(f)







def save(word, words, forbidden, language):
    meaning = input("\n- Meaning: ").lower().strip() # Entrada do usuário

    if any(c in forbidden for c in word): # Tem caracteres inválidos
        print("\n- Have invalid caracters!")
        save(word, words, forbidden, language)

    else: # Não tem caracteres inválidos
        



def df_language(words, forbidden, language):
    print("\n-- Choosed language --\n\n- 1) English\n- 2) Português(Brasil)")

    try: # Altera o idioma
        l = int(input("\n- Language: "))
        if      l==1: print("- Language: English"); language="English"
        elif    l==2: print("- Idioma: Português(Brasil)"); language="Português"

    except: # Idioma padrão
        if      language=="English": print("- It is not a choose, language not changed!")
        elif    language=="Português": print("- Isso não é uma escolha, idioma não foi alterado!")
    entry(words, forbidden, language)


def entry(words, forbidden, language):
    if language=="English":
        word = input("\n- Word: ").lower().strip() # Entrada do usuário

        if any(c in forbidden for c in word): # Tem caracteres inválidos
            print("\n- Have invalid caracters!")
            entry(words, forbidden, language)

        else: # Não tem caracteres inválidos

            if word in words:
                print("- Word:", words[word].capitalize())
                entry(words, forbidden, language)

            elif word=="c": print("\n") # Fecha o programa

            elif word=="l": # Escolhe um idioma
                df_language(words, forbidden, language)

            else:
                print("- Word: Not found!")
                record = input("- Save this word? (S/N) ").lower().strip()
                if record=="s": save(word, words, forbidden, language)
                else:
                    print("\n- Word don't save!")
                    entry(words, forbidden, language)

                entry(words, forbidden, language)


    elif language=="Português":
        print("\n- Idioma está em português!")

entry(words, forbidden, language)