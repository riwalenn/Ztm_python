from translate import Translator

translator = Translator('fr')
# correction : Translator(to_lang='fr')

translation = translator.translate('This is a pen')
print(translation)

with open('toTranslate.txt', mode='r') as my_file:
    texte = my_file.read()
    translation2 = translator.translate(texte)
    print(translation2)

# correction

try:
    with open('toTranslate.txt', mode='r') as my_file:
        texte = my_file.read()
        translation3 = translator.translate(texte)
        with open('test-fr.txt', mode='w') as my_file2:
            my_file2.write(translation3)
except FileNotFoundError as err:
    print('File not found')
