#import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.request.URLError:
    print('\33[31m''O site não está acessível!''\33[0m')
else:
    print('\33[33m''O site está acessível!!''\33[0m')
    print(site.read()) # pega o conteúdo HTML do site IMPORTANTE!!!