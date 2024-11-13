def polynome():
    p=[]
    a = input("Entrer un coefficient: ")
    while(a!='f'):
        p.append(int(a))
        a = input("Entrer un coefficient ou f si fin:")
    return p

p=polynome()
print(p)

def afficher(p):
    # p.reverse()
    p2 = p[::-1]
    poly = ''
    j=len(p)
    for i,a in enumerate(p2):
        j-=1
        if(i<len(p)-1):
            poly+=f"{a}X^{j}+"
        else : 
            poly+=f"{a}"
    print(poly)
        
afficher(p)

def get_valeur(p,x):
    #p.reverse()
    sum = 0
    for i,a in enumerate(p):
        sum+=a*(x**i)
    return sum
    

res = get_valeur(p,2)
print(res)

def deriver(p):
    p2 = p[::-1]
    poly = ''
    j=len(p)
    for i,a in enumerate(p2):
        j-=1
        if(i<len(p)-2):
            poly+=f"{a*j}X^{j-1}+"
        elif(i<len(p)-1) : 
            poly+=f"{a}"
    print(poly)
    
deriver(p)