def clean(fname):
    c=""    
    with open(fname,'r', encoding='utf8', errors ='ignore') as fin:
        fstring = fin.read().lower()
    # print(fstring)
    for i in range(len(fstring)-1):
        if fstring[i].isalpha() or fstring[i].isdigit() or fstring[i]=='.' or fstring[i]==',' or fstring[i]=="'"or fstring[i]=='-':
            c=c+fstring[i]
        elif fstring[i]=='\n':
            c=c+'\n'
        elif fstring[i]==" " and fstring[i+1]!=' ': #removes multiple spaces
            c=c+' '
    return c