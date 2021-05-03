from df112.utilidadescev import dado
from df112.utilidadescev import moeda

price = dado.readmoney('Digite o preço: R$')
moeda.resumo(price, 20, 90)