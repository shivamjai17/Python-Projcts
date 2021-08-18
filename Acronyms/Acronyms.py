def Acro(s):
    ot=s[0]
    for i in range(1,len(s)):
        if s[i]==' ':
            ot+=s[i+1]
    ot=ot.upper() 
    return ot       
if __name__ == '__main__':
    print('Enter Acronyms'.center(50))
    Inp=str(input())
    out=Acro(Inp)
    print(out)    