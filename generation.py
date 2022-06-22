import random
import material
import dicionario




def Treat_Word(string):
    word = string
    vocals = ('a','e','i','o','u')
    if word[-1] in vocals:
        if word[-1] == 'a':
            word += random.choice(('ncia', 'da'))
        elif word[-1] == 'e':
            word += random.choice(('za','ncia'))
        elif word[-1] == 'i':
            word += random.choice(('lis','ssimo'))

    if word[-1] in vocals:
        word += 's'

    return word




def Create_Phrase():
    template = random.choice(material.templates)
    result = ''

    for word in template.split():
        if word == 'SUBJECT':
            result += random.choice(material.words['SUBJECT'])

        elif word == 'ACTION' or word == 'ANY':
            result += Treat_Word(random.choice(dicionario.words))

        else:
            result += word


        result += ' '
    return result
