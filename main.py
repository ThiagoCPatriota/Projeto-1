import random

classfied_list = ['noite', 'claro', 'verde', 'cinza', 'negro', 'breve', 'largo', 'curto', 'velho', 'justo', 'baixo', 'forte', 'fraco']
classfied_word1, classfied_word2, classfied_word3, classfied_word4 = random.sample(classfied_list, 4)
print(classfied_word1, classfied_word2, classfied_word3, classfied_word4)

def menu():
    print('''
    MENU:

    1 - 1 PALAVRA
    2 - 2 PALAVRAS
    3 - 4 PALAVRAS      
    ''')
    result_menu = int(input())
    return result_menu



def palavra_1(classfied_word1, tentativa):
    for word in range(len(classfied_word1)):
        if classfied_word1[word] == tentativa[word]:
            print('✅  ', end='')
            print(tentativa[word].upper())
        elif classfied_word1[word] in tentativa[word]:
            print('🟨  ', end='')
            print(tentativa[word].upper())
        else:
            print('🟥  ', end='')
            print(tentativa[word].upper())
    return classfied_word1 == tentativa            

def palavra_2(classfied_word1, classfied_word2, acerto1, acerto2, tentativa):
    if not acerto1:
        print('___________________PALAVRA 1___________________')   
        acerto1 = palavra_1(classfied_word1, tentativa)
    if not acerto2:
        print('___________________PALAVRA 2___________________')   
        acerto2 = palavra_1(classfied_word2, tentativa)
    return acerto1, acerto2

def palavra_4(classfied_word1, classfied_word2, classfied_word3, classfied_word4, acerto1, acerto2, acerto3, acerto4, tentativa):
    if not acerto1:
        print('___________________PALAVRA 1___________________')   
        acerto1 = palavra_1(classfied_word1, tentativa)
    if not acerto2:
        print('___________________PALAVRA 2___________________')   
        acerto2 = palavra_1(classfied_word2, tentativa)
    if not acerto3:
        print('___________________PALAVRA 3___________________')
        acerto3 = palavra_1(classfied_word3, tentativa)
    if not acerto4:
        print('___________________PALAVRA 4___________________')
        acerto4 = palavra_1(classfied_word4, tentativa)
    return acerto1, acerto2, acerto3, acerto4


acerto1, acerto2, acerto3, acerto4 = False, False, False, False


    
result_menu = menu()
while(True):
    if result_menu == 1:
        tentativa = input('Digite sua tentativa: ').lower()
        acerto1 = palavra_1(classfied_word1, tentativa)
        if acerto1:
            print('Você acertou o termo de 1 PALAVRA, Parabéns!')
    elif result_menu == 2:
        tentativa = input('Digite sua tentativa: ').lower()
        acerto1, acerto2 = palavra_2(classfied_word1, classfied_word2, acerto1, acerto2, tentativa)
        if acerto1 and acerto2:
            print('Você acertou o termo de 2 PALAVRAS, Parabéns!')
    elif result_menu == 3:
        tentativa = input('Digite sua tentativa: ').lower()
        acerto1, acerto2, acerto3, acerto4 = palavra_4(classfied_word1, classfied_word2, classfied_word3, classfied_word4, acerto1, acerto2, acerto3, acerto4, tentativa)
        if acerto1 and acerto2 and acerto3 and acerto4:
            print('Você acertou o termo de 4 PALAVRAS, Parabéns!')