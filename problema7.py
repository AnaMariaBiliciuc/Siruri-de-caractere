S=str(input('Introduceti sirul de caractere:  '))
n=0
for i in range(0,len(S)) :
    x=ord(S[i])
    if x==65:
        n+=1
print('Numarul de aparitie a caracterului A in sirul S:',n)   
S1=[]
for i in S:
    S1=S.replace('A' ,'*')
print('Sirul obtinut prin substituirea caracterului A prin caracterul * : ',S1)
S2=[]
for i in S:
    S2=S.replace('B','')
print('Sirul obtinut prin radierea din sirul S a tuturor aparitiilor a caracterului B:',S2)
n1=0 
for i in S:
    n1=S.count('MA')
print('Numarul de aparitii a silabei MA in sir:',n1)
S3=[]
for i in S:
    S3=S.replace('MA','TO')
print('Sirul obtinut prin inlocuirea silabei MA cu silaba TA:',S3)
S4=[]
for i in S:
    S4=S.replace('TO',' ')
print('Sirul format prin radierea din sirul S a tuturor aparitiilor silabei TO:',S4)
S5=[]
S5=S[::-1]
print('Scrierea inversa a sirului:',S5)