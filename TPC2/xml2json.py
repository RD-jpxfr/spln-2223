import re

file = open('parsedxml.txt', 'r', encoding='utf-8')
text = file.readlines()

EC = []
ER = []
i = 0

def store_EC(text, ln):
    d = {}
    d["linguas"] = {}
    
    # \d+  .*      [m|f]
    ln1 = re.search(r'##C  (\d+)\s*(.+?)(\s{2,}(.*?))?\n', text[ln])
    #d[ln1.group(1)] = ln1.group(2)
    ga = []
    aux = ln1.group(2)
    if ln1.group(4) :
        aux += " (" + ln1.group(4) + ")"
    ga.append(aux)
    ln = ln + 1
    
    # area(s)
    ln2 = re.search(r'(.*?)\n', text[ln])
    d['area'] = ln2.group(1)
    ln = ln + 1
    
    # SIN (may not have)
    if re.search(r'(SIN)\.-?\s*(.*?)\n', text[ln]):
        ln3 = re.search(r'(SIN)\.-?\s*(.*?)\n', text[ln])
        aux = ln3.group(2).split("; ")
        ga += (aux)
        ln = ln + 1
    
    # VAR (may not have)
    if re.search(r'(VAR)\.-?\s*(.*?)\n', text[ln]):
        ln3 = re.search(r'(VAR)\.-?\s*(.*?)\n', text[ln])
        aux = ln3.group(2).split("; ")
        ga += [s + " [VAR.]" for s in aux]
        ln = ln + 1
    
    d["linguas"]["ga"] = ga

    # @es
    ln4 = re.search(r'@(es)  (.*?)\n', text[ln])
    d["linguas"]["es"] = ln4.group(2).split("; ")
    ln = ln + 1
    
    # @en
    ln5 = re.search(r'@(en)  (.*?)\n', text[ln])
    d["linguas"]["en"] = ln5.group(2).split("; ")
    ln = ln + 1
    
    # @pt
    ln6 = re.search(r'@(pt)  (.*?)\n', text[ln])
    d["linguas"]["pt"] = ln6.group(2).split("; ")
    ln = ln + 1
    
    # @la (may not have)
    if ln<len(text) and re.search(r'@(la)  (.*?)\n', text[ln]):
        ln7 = re.search(r'@(la)  (.*?)\n', text[ln])
        d["linguas"]["la"] = ln7.group(2).split("; ")
        ln = ln + 1
    
    # Nota (may not have)
    if ln<len(text) and re.search(r'(Nota)\.- (.*?)\n', text[ln]):
        ln8 = re.search(r'(Nota)\.- (.*?)\n', text[ln])
        d[ln8.group(1)] = ln8.group(2)
        ln = ln + 1

    EC.append(d)
    return ln

def store_ER(text, ln):
    d = {}
    # .*
    ln1 = re.search(r'##R  (.*?)\s*?\n', text[ln])
    ln = ln + 1
    # Vid.- .*
    ln2 = re.search(r'Vid\.-? (.*?)\n', text[ln])
    ln = ln + 1
    d[ln1.group(1)] = ln2.group(1)

    ER.append(d)
    return ln

while i<len(text):
    if re.search(r'##R (.*?)\n', text[i]):
        i = store_ER(text, i)
    if re.search(r'##C (.*?)\n', text[i]):
        i = store_EC(text, i)
    i += 1


#print(len(EC))
#print(len(ER))

import json
with open("medicina.json", "w+", encoding="utf-8") as fp:
    json.dump(EC, fp, indent=4, ensure_ascii=False) #ensure_ascii=False para poder escrever em utf-8

file.close()