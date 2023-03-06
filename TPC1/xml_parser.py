import re

file1 = open('medicina.xml', 'r', encoding='utf-8')
text = file1.read()

# new file for the parsed xml
file2 = open('parsedxml1.txt', 'w', encoding='utf-8')

# remove header and page number
def remove_header_footer(text):
    text = re.sub(r'<page.*?>\n', r'', text)
    text = re.sub(r'\s+<fontspec.*?/>\n', r'', text)
    text = re.sub(r'</page>', r'', text)

    text = re.sub(r'<text.*>ocabulario</text>', r'###', text)
    text = re.sub(r'<text.*?\n###\n.*?</text>\n', r'', text)

    return text

# remove lines without information
def remove_emptylines(text):
    text = re.sub(r'<text.*>(<[b|i]>)?\s+(</[b|i]>)?</text>\n', r'', text)

    return text

# mark entry
def markE(text):
    text = markEC(text)
    text = markER(text)
    return text

# mark "entradas completas", this start with a number
# Note: there may be spaces before the number appears 
def markEC(text):
    text = re.sub(r'<text.*?><b>\s*(\d+.*)</b></text>', r'\n##C  \1', text)
    text = mark_languages(text)
    
    return text

# mark the languages -> es, en, pt, la
def mark_languages(text):
    text = re.sub(r'<text.*?>\s*(es|en|pt|la)\s*</text>\n', r'@\1  ', text)

    return text

# mark "entradas remisivas", this do not start with a number
# Note: there may be spaces before the word appears 
def markER(text):
    text = re.sub(r'<text.*?>(<i>)?<b>\s*(.*)</b>(</i>)?</text>', r'\n##R  \2', text)

    return text

text = remove_emptylines(text)
text = remove_header_footer(text)
text = markE(text)

# remove the xml-only information and correct entries
def remove_filler(text):
    text = re.sub(r'<text.*?>\s*', r'', text)
    text = re.sub(r'\s*</text>', r'', text)

    text = re.sub(r';\n<i>\s*', r'; ', text)
    text = re.sub(r'</i>\n;', r';', text)
    text = re.sub(r'\n<i>\s{6}', r'', text)
    text = re.sub(r'<i>\s*', r'', text)
    text = re.sub(r'</i>', r'', text)
    text = re.sub(r'</b>', r'', text)
    text = re.sub(r'\n\[', r' [', text)
    text = re.sub(r'\n\(', r' (', text)
    return text

text = remove_filler(text)

# correct miss/void entries
while re.search(r'(##.*?)\n\n##.  ', text):
    text = re.sub(r'(##.*?)\n\n##.  ', r'\1', text)

# correct when the area stays on the first line
text = re.sub(r'(##C  \d+  .*?      [a-z]+( [a-z]+)?)[ ]*([A-Z].*)\n', r'\1\n\3\n', text)

# correct multi lined areas
while re.search(r'(##C.*?)\n(.*?)\n[^\@|SIN|VAR]', text):
    text = re.sub(r'(##C.*?)\n(.*?)\n([^\@|SIN|VAR].*?)\n', r'\1\n\2\3\n', text)

# correct multi lined "SIN.-"
while re.search(r'(SIN\.-.*?)\n[^\@|V]', text):
    text = re.sub(r'(SIN\.-.*?)\n([^\@|V].*?)\n', r'\1 \2\n', text)

# correct multi lined "Vid.-"
while re.search(r'(Vid\.-?.*?)\n(.+?)\n', text):
    text = re.sub(r'(Vid\.-?.*?)\n(.+?)\n', r'\1 \2\n\n', text)

# correct multi lined "VAR.-"
while re.search(r'(VAR\.-.*?)\n[^\@|S]', text):
    text = re.sub(r'(VAR\.-.*?)\n([^\@|S].*?)\n', r'\1 \2\n', text)

# correct multi lined languages
while re.search(r'(\@.*?)\n[^\@|\s|NOTA]', text):
    text = re.sub(r'(\@.*?)\n([^\@|\s|NOTA].*?)\n', r'\1\2\n', text)

# correct multi lined "Nota.-"
while re.search(r'(Nota\.-.*?)\n(.+?)\n', text):
    text = re.sub(r'(Nota\.-.*?)\n(.+?)\n', r'\1 \2\n', text)

# write on new file
file2.write(text)

file2.close()
file1.close()