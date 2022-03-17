from random import choice
from string import ascii_letters,digits
from pyfiglet import print_figlet

print_figlet('Parola\nOluşturucu')
print('-'*60)
########################################
try:
    uzunluk = int(input('Parolanız ne kadar uzun olsun (varsayılan : 10) : '))
    if uzunluk < 1:
        uzunluk = 10
except:
    uzunluk = 10
########################################
try:
    adet = int(input('Kaç adet olsun (varsayılan : 1) : '))
    if adet < 1:
        adet = 1
except:
    adet = 1
########################################
parola = ""
if adet == 1:
    for a in range(uzunluk):
        parola += choice(ascii_letters+digits*2)
    print('-'*60+f'\nParolanız : {parola}')
else:
    sira = 0
    print('-'*60+'\nParolalarınız ;')
    for a in range(adet):
        parola = ""
        for b in range(uzunluk):
            parola += choice(ascii_letters+digits*2)
        sira += 1
        print(sira,'-',parola)
        
input('-'*60+'\nÇıkmak için ENTER basınız...')