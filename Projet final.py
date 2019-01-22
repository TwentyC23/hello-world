M=0
while M!=7:
    M=int(input('''\n       ===================
              MENU
       ===================
    1-codage césar
    2-codage affine
    3-codage vigenère
    4-décodage césar
    5-décodage affine
    6-décodage vigenère
    7-quitter le programme
    \nn° du choix : '''))
    if M<1 or M>7:
        print("\nce choix est impossible !")
        M=int(input('''\n        ===================
               MENU
        ===================
    1-codage césar
    2-codage affine
    3-codage vigenère
    4-décodage césar
    5-décodage affine
    6-décodage vigenère
    7-quitter le programme
    \nn° du choix : '''))


    if M==1:
        MC=input('\nEntrez le message à chiffrer: ')
        k=int(input('Entrez la clé de chiffrement: '))
        A=[0]*len(MC)
        for i in range(len(MC)):
            if ord(MC[i])>64 and ord(MC[i])<91:
                A[i]=ord(MC[i])-65
            if ord(MC[i])>96 and ord(MC[i])<123:
                A[i]=ord(MC[i])-97
            A[i]=(k+A[i])%26
            if ord(MC[i])>64 and ord(MC[i])<91:
                A[i]=chr(A[i]+65)
            if ord(MC[i])>96 and ord(MC[i])<123:
                A[i]=chr(A[i]+97)
        A=''.join(A)
        print('message codé:',A)


    if M==2: 
        MA=input('Entrez un message à chiffrer: ')
        a=0
        while a!=1:
            x=int(input('Entrez le coefficient multiplicateur parmi les nombres premiers avec 26 (1,3,5,7,9,11,15,17,19,21,23,25): '))
            y=int(input('Entrez le coefficiant additionel: '))
            a=max(x,y)
            b=min(x,y)
            while b!=0 :
                r=a-b*int(a/b)
                a=b
                b=r
            if a!=1:
                print("\nLe coefficient multiplicateur doit etre premier avec 26 (nombres de lettres de l'alphabet)\n")
        A=[0]*len(MA)
        for i in range(len(MA)) :
            if ord(MA[i])>64 and ord(MA[i])<91:
                A[i]=ord(MA[i])-65
            if ord(MA[i])>96 and ord(MA[i])<123:
                A[i]=ord(MA[i])-97
            A[i]=((A[i]*x)+y)%26
            if ord(MA[i])>64 and ord(MA[i])<91:
                A[i]=chr(A[i]+65)
            if ord(MA[i])>96 and ord(MA[i])<123:
                A[i]=chr(A[i]+97)
        A=''.join(A)
        print(A)


    if M==3:
        message_a_chiffrer=input('\nmessage à chiffrer: ')
        cle=input('clé de codage: ')
        A=[0]*len(message_a_chiffrer)
        for i in range(len(cle)) :
            if ord(cle[i])>64 and ord(cle[i])<91:
                A[i]=ord(cle[i])-65
            if ord(cle[i])>96 and ord(cle[i])<123:
                A[i]=ord(message_a_chiffrer[i])-97
        for i in range(len(message_a_chiffrer)) :
            if ord(message_a_chiffrer[i])>64 and ord(message_a_chiffrer[i])<91:
                A[i]=ord(message_a_chiffrer[i])-65
            if ord(message_a_chiffrer[i])>96 and ord(message_a_chiffrer[i])<123:
                A[i]=ord(message_a_chiffrer[i])-97
            

            
            if ord(message_a_chiffrer[i])>64 and ord(message_a_chiffrer[i])<91:
                A[i]=chr(A[i]+65)
            if ord(message_a_chiffrer[i])>96 and ord(message_a_chiffrer[i])<123:
                A[i]=chr(A[i]+97)


    if M==4:
        DC=input('\nEntrer le message codé (chiffrement de Cesar): ')
        B=[0]*len(DC)
        print('décalage de','|','message décodé\n')
        for k in range(1,26):
            for i in range(len(DC)):
                if ord(DC[i])>64 and ord(DC[i])<91:
                    B[i]=ord(DC[i])-65
                if ord(DC[i])>96 and ord(DC[i])<123:
                    B[i]=ord(DC[i])-97
                B[i]=((26-k)+B[i])%26
                if ord(DC[i])>64 and ord(DC[i])<91:
                    B[i]=chr(B[i]+65)
                if ord(DC[i])>96 and ord(DC[i])<123:
                    B[i]=chr(B[i]+97)
            if k<10:
                print('        ',k,' :',''.join(B))
            else:
                print('        ',k,':',''.join(B))


    if M==5:
        DA=input('\nEntre le message codé (chiffre affine): ')
        B=[0]*len(DA)
        print('coefficients a/b','|','message décodé\n')
        a=[1,3,5,7,9,11,15,17,19,21,23,25]
        z=[1,9,21,15,3,19,7,23,11,5,17,25]
        for k in range(len(z)):
            for b in range(1,26):
                for i in range(len(DA)):
                    if ord(DA[i])>64 and ord(DA[i])<91:
                        B[i]=ord(DA[i])-65
                    if ord(DA[i])>96 and ord(DA[i])<123:
                        B[i]=ord(DA[i])-97
                    B[i]=z[k]*(B[i]-b)%26
                    if ord(DA[i])>64 and ord(DA[i])<91:
                        B[i]=chr(B[i]+65)
                    if ord(DA[i])>96 and ord(DA[i])<123:
                        B[i]=chr(B[i]+97)
                if a[k]<10 and b<10:
                    print('        ',a[k],'/',b,'  :',''.join(B))
                if a[k]<10 and b>10:
                    print('        ',a[k],'/',b,' :',''.join(B))
                if a[k]>10 and b<10:
                    print('        ',a[k],'/',b,' :',''.join(B))
                if a[k]>10 and b>10:
                    print('        ',a[k],'/',b,':',''.join(B))
        
