# TPC1
## Ficheiros:

- **parsedxml.txt**: representação obtida no último TPC;
- **medicina.json**: JSON file com o vocabulário de medicina estruturado para multi-língua (galego, espanhol, inglés, portugués, latim);
- **medDict.txt**: ficheiro com a informação de **medicina.json** formatada para melhor compreensão quando vista pelo olho humano; 
- **xml2json.py**: script em Python que transforma o ficheiro **parsedxml.txt** no ficheiro **medicina.json**;
- **json2dicionario.py**: script em Python que formata a informação do ficheiro **parsedxml.txt** para o ficheiro **medicina.json**;

## Entradas
```
Área(s): ...(      ...)*
Línguas:
    - ga:
        (· ...)+
    - es:
        (· ...)+
    - en:
        (· ...)+
    - pt:
        (· ...)+
    - la:
        (· ...)+
Nota informativa (opcional)
```