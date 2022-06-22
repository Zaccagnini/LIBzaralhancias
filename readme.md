Uma lib que gera gírias de nicho de comunidade de League of Legends.


Utilização:

O arquivo generation.py contém as funções da lib, e também deve ficar junto com os outros arquivos .py

>>>import generation
>>>frase = generation.create_phrase()

Irá retornar uma frase aleatória com base nas templates disponíveis.
Você pode sugerir templates novas no meu twitter: https://twitter.com/zaccagnini_



>>>palavra = generation.treat_word('palavra')
>>>print(palavra)
>>>palavrancia

Irá retornar a palavra que você selecionou de forma "tratada" pra ficar no estilo de gíria de lol



>>>add_custom_word('comes e bebes')

Adiciona uma palavra que você queira ao arquivo do dicionario.py
Isso altera o arquivo do dicionário.
Caso a palavra já exista no dicionário, o comando vai printar essa informação para você.
