'''array = [2, 4, -2, 11, 8, 13, -3, 1]
def soma(arr):
  if max(arr) + min(arr) == 10:
    return [max(arr), min(arr)]
  else:
    return []
print(soma(array))'''

"""black = [150, 179, 149, 152, 154]
orange = [162, 181, 151, 160, 170]
def escola(black, orange):
  b = sorted(black)
  o = sorted(orange)
  fila = [b, o]
  print(fila)
  if min(orange) <= max(black):
    print(False)
escola(black, orange)"""
#BBBBBBBBBBBBBAACCCDD
string = 'BBBBBBBBBBBBBAACCCDD'
def stri(string):
  a = 0
  b = 0
  c = 0
  d = 0
  #print(string.strip())
  i = string.strip()
  for s in i:
    if s == 'B':
      b += 1
      b2 = b - 9
      b3 = b - b2
    if s == 'A':
      a += 1
    if s == 'C':
      c += 1
    if s == 'D':
      d += 1
  print(f'{b3}B{b2}B{a}A{c}C{d}D')
stri(string)
