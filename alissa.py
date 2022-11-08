import webbrowser as wb

print(
'…………..$……………………………………..$…………..\n'
'…………$$……………………………………..$$…………\n'
'…………$$……………………………………..$$…………\n'
'…………..$$s………………………………s$$…………..\n'
'…………….$$$$……………………….$$$$…………….\n'
'………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………………\n'
'………………..³$$$$..¶¶¶¶¶¶..$$$$³………………..\n'
'………………¶..$$$$$..¶¶¶¶..$$$$$..¶………………\n'
'…………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶………………\n'
'…………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶………………\n'
'…………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………\n'
'………………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………..\n'
'.……………..¶¶……..¶¶¶¶……….¶……………………\n'
'………………..¶¶……..¶¶¶¶……….¶¶………………….\n'
'………………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶………………….\n'
'………………….¶¶¶¶¶¶……¶¶¶¶¶¶¶………………….\n'
'……………………….¶¶¶¶¶¶¶¶¶…………………………\n'
'……………………….¶..¶..¶..¶..¶…………………………\n'
'…………¶…………..¶…………..¶…………..¶…………..\n'
'……….¶¶……………………………………….¶¶…………\n'
'……….¶¶……………………………………….¶¶…………\n'
'……….¶¶…………..¶¶……….¶¶…………..¶¶…………\n'
'……….¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶…………\n'
'……¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶……..\n'
'….¶¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶¶……\n'
'……¶¶¶¶..¶¶..¶¶………………….¶¶..¶¶..¶¶¶¶……..')

m = str(input('\033[31mOlá jovem, diga-me o seu nome:\033[m'))
q = m.strip()
n = q.lower()
f = 'seven' , 'one' , 'two', 'three' , 'four' , 'five' , 'six ', 'eight' , 'nine' , 'ten'

if n in f:
    print('\033[31mOlá mestre, aqui estão algumas funções <3\n\033[m')
    print( '\033[32m 1 [GOOGLE] 2 [YOUTUBE] 3 [HK] 4 [KALI LINUX] 5 [VM] 6 [FERRAMENTAS(BETA)] 7 [TOR] 8 [SITES TOR] 9 [SAIR] \033[m \n ')

else :
    print('\033[31m Olá {}, vejo que não me conhece, eu sou Alissa, prazer em te conhecer {}!!!\033[m\n'.format(q , q))
    print( '\033[32m 1 [GOOGLE] 2 [YOUTUBE] 3 [HK] 4 [KALI LINUX] 5 [VM] 6 [FERRAMENTAS(BETA)] 7 [TOR] 8 [SITES TOR] 9 [SAIR]  \033[m \n')

def main():
    while True:
        k = int(input('\033[31m O que desejas?\033[m'))
        if k == 1:
            wb.open('https://google.com/')
        elif k == 2 :
            wb.open('https://www.youtube.com/')
        elif k == 3 :
            wb.open('https://hkbrs.blogspot.com/')
        elif k == 4 :
            wb.open('https://www.kali.org/')
        elif k == 5 :
            wb.open('https://www.virtualbox.org/')
        elif k == 7 :
            wb.open('https://www.torproject.org/download/')
        elif k == 8 :
            wb.open('https://www.100security.com.br/deepweb-sites/')
        elif k == 9 :
            input('\033[31mAperte enter para sair:\033[m')
            break
        else:
            qw = input('\033[31mEu não entendi, por favor digite novamente:\033[m')
main()