import json

with open('medicina.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

f = open('medDict.txt', 'w+', encoding='utf-8')


for entry in data:
    f.write("Área(s): " + entry["area"] + "\n")
    f.write("Línguas:\n")
    for language, listSYN in entry["linguas"].items():
        f.write("\t- " + language + ":\n")
        for syn in listSYN:
            f.write("\t\t· " + syn + "\n")
    if "Nota" in entry.keys() :
        f.write("Nota: " + entry["Nota"] + "\n")

    f.write("\n\n")