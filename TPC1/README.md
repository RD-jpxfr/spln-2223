# TPC1
## Ficheiros:

- **medicina.pdf**: pdf sobre o vocabulário de medicina (galego-espanhol-inglés-portugués);
- **medicina.xml**: xml gerado sobre o ficheiro medicina.pdf com o comando:
    - pdftohtml medicina.pdf -xml -f 20 -l 543;
- **parsedxml.txt**: representação intermédia do ficheiro - **medicina.xml**;
- **xml_parser.py**: script em Python que transforma o ficheiro **medicina.xml** no formato intermédio do ficheiro **parsedxml.txt**.

## Entradas
- **Entradas completas**:
    - Índice;
    - Termo;
    - Categoria gramatical;
    - Áreas temáticas (1+)
    - Sinónimos (0+);
    - Variantes (0+);
    - Traduções:
        - Sinónimos em es (1+);
        - Sinónimos em en (1+);
        - Sinónimos em pt (1+);
        - Sinónimos em la (0+);
    - Nota informativa (opcional)
- **Entradas remissivas**:
    - Denomincação;
    - Palavra referênciada como sinónimo ou variante;