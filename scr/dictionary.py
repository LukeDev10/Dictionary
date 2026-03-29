import json
import os
import sys

print("\n-- Dictionary --\n\n- 'C' to close\n- 'L' to choose the language")

language = "english"
forbidden = r"0123456789\|/:;+*[]@#$%¨()£¢¬"

ARCHIVE = os.path.dirname(__file__)
FOLDER = os.path.dirname(ARCHIVE)

WORDS = os.path.join(FOLDER, "words.json")
with open(WORDS, "r", encoding="utf-8") as f: words = json.load(f)




def save(word, words, forbidden, language):
    # region Saving in English
    if language=="english":
        meaning = input("\n- Meaning: ").lower().strip() # Entrada do usuário

        if any(c in forbidden for c in meaning): # Tem caracteres inválidos
            print("\n- Have invalid caracters!")
            save(word, words, forbidden, language)

        else: # A palavra de tradução não tem caracteres inválidos
            words[word] = meaning

            with open(WORDS, "w", encoding="utf-8") as f:
                json.dump(words, f, indent=4, ensure_ascii=False)

            print("\n- The word was saved!")
            entry(words, forbidden, language)
    #endregion





    # region Saving in Portuguese
    elif language=="português":
        meaning = input("\n- Tradução: ").lower().strip()

        if any(c in forbidden for c in meaning): # Tem caracteres inválidos
            print("\n- Tem caracteres inválidos!")
            save(word, words, forbidden, language)


        else: # A palavra de tradução não tem caracteres inválidos
            words[meaning] = word

            with open(WORDS, "w", encoding="urtf-8") as f:
                json.dump(words, f, indent=4, ensure_ascii=False)

            print("\n- A palavra foi salva!")
            entry(words, forbidden, language)
            # trocar o valor da tradução pela chave
    # endregion





# region Defining language
def df_language(words, forbidden, language):
    print("\n-- Choosed language --\n\n- 1) English\n- 2) Português(Brasil)")

    try: # Altera o idioma
        l = int(input("\n- Language: "))
        if      l==1: print("- Language: English"); language="english"
        elif    l==2: print("- Idioma: Português(Brasil)"); language="português"

    except: # Idioma padrão
        if      language=="english": print("- It is not a choose, language not changed!")
        elif    language=="português": print("- Isso não é uma escolha, idioma não foi alterado!")
    entry(words, forbidden, language)
# endregion



def entry(words, forbidden, language):

# region Code in English
    if language=="english":

        word = input("\n- Word: ").lower().strip() # Entrada do usuário

        if any(c in forbidden for c in word): # Tem caracteres inválidos
            print("\n- Have invalid caracters!")
            entry(words, forbidden, language)

        else: # Não tem caracteres inválidos

            if word in words:
                print("- Word:", words[word])
                entry(words, forbidden, language)

            elif word=="c": sys.exit() # Fecha o programa

            elif word=="l": # Escolhe um idioma
                df_language(words, forbidden, language)

            else:
                print("- Word: Not found!")
                record = input("- Save this word? (Y/N) ").lower().strip()
                if record=="y": save(word, words, forbidden, language)
                else:
                    print("\n- The word was not saved!")
                    entry(words, forbidden, language)

                entry(words, forbidden, language)
# endregion


# region Code in Portuguese
    elif language=="português":




        word = input("\n- Palavra: ").lower().strip() # Entrada do usuário

        if any(c in forbidden for c in word): # Tem caracteres inválidos
            print("\n- Tem caracteres inválidos!")
            entry(words, forbidden, language)

        else: # Não tem caracteres inválidos

            if word in words.values():
                for key, value in words.items():
                    if word==value: print("- Palavra:",key)
                entry(words, forbidden, language)


            elif word=="c": sys.exit() # Fecha o programa

            elif word=="l": # Escolhe um idioma
                df_language(words, forbidden, language)

            else:
                print("- Palavra; Não encontrada!")
                record = input("- Salvar está palavra? (S/N) ").lower().strip()
                if record=="s": save(word, words, forbidden, language)
                else:
                    print("\n- Palavra não foi salva!")
                    entry(words, forbidden, language)

                entry(words, forbidden, language)
# endregion

entry(words, forbidden, language)