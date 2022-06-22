templates = [
    'mee SUBJECT foi de ACTION',
    'SUBJECT ta de ACTION',
    'SUBJECT ta no ANY',
    'mee ai foi pro ANY',
    'mee ai foi de ANY',
    'ANY do ANY',
    'ANY do ANY',
    'eu to ACTION no ACTION purinho',
    'mandei o cara ir de ANY ele veio zaralhar pra cima de mim tankei foi nada',
    'tava ACTION do ACTION na soloqueue maluco veio de ACTION pra cima de mim meti logo um ANY mandei o cara p ANY maluco tendeu foi nada',
    'cara na minha frente foi de ANY tankei nao tbh',
    'maluco veio no ANY purinho pra cima de mim como que tanka'
]


words = {
    'SUBJECT':['brtt', 'jovi', 'jukes', 'jukera', 'veio', 'melao', 'maos soltas', '4lan',
               'veio', 'jao', 'muca', 'mayumi', 'kami', 'faker', 'chines', 'coreano', 'djoko', 'keio',
               'arthur lanches', 'maradona', 'pelé', 'ribamar', 'guigo']

}


import random
result = ''
result += random.choice(words['SUBJECT'])