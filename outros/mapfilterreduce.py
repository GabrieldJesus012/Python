from pprint import pprint #print vem do módulo pprint (pretty-print), que significa "impressão bonita" ou "organizada".
_print = print 
from functools import reduce
'''
Quando você faz print = pprint, você substitui temporariamente a função original print pela função pprint.
Antes disso, você salva a versão original em _print, caso queira usar depois.
'''
print=pprint
produtos = [
    {'nome': 'P1', "preco": 59.90, "peso_kg":1.312,'variações':['a','b']},
    {'nome': 'P2', "preco": 19.55, "peso_kg":2.300,'variações':['c','d']},
    {'nome': 'P3', "preco": 9.13, "peso_kg":0.150,'variações':['e','f']},
    {'nome': 'P4', "preco": 3.49, "peso_kg":0.789,'variações':['g','h']},
    {'nome': 'P5', "preco": 33.22, "peso_kg":3.578,'variações':['i','j']},
]

#map
#precos_map = list(map(lambda p:{**p,'preco':round(p['preco']*1.05)},produtos)) #altera tanto produto e preco
'''precos_map = list(map(lambda p:p['preco'],produtos))
precos_map_listcomprehension = [produto['preco'] for produto in produtos] #fazendo a mesma coisa.
print(precos_map)
print(precos_map_listcomprehension)'''

#filter
'''precos_filter = list(filter(lambda p:p['preco']<10.00,produtos))
print(precos_filter)'''

#reduce
def precoreduce(ac,p):
    return  ac + p['preco']  # só trocar o lambda por isso caso queira

preco_totais = reduce(lambda ac,p: ac+p['preco'], produtos,0)
#preco_totais = reduce(precoreduce, produtos,0)
print(round(preco_totais))