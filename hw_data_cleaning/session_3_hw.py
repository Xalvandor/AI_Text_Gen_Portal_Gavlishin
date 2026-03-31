import re

#regex for matching html tags
html_re = r'<(/?)([\w][\w\d]*)(\s[^>]*)?(\/?)>'
#regex for matching non-alpha characters with spaces in front and/or behind
non_alpha_regex = r' \W+ | \W+$|\A\W+ '
#regex for matching more than one space
blank_space_re = r' {2}'

#reads file to memory
filename = "data/corrupt_movie_corpus.txt"
with open(filename, mode='r', encoding='utf-8') as f:
   data = f.read()
#creates list for clean data
clean_data = []
#creates list of lines for corrupted data
data = data.splitlines()
#reads through each line and replaces if there is a regex match
for line in data:
    x = re.sub(html_re, '', line)
    x = re.sub(blank_space_re, ' ', x)
    x = re.sub(non_alpha_regex, ' ', x)
    x = re.sub(non_alpha_regex, ' ', x)
    # appends to clean data list
    clean_data.append(x.strip() + "\n")
#print statement for checking output
# for x in range(200, 400):
#    print(clean_data[x])
#writes clean data to file
with open('data/clean_movie_corpus.txt', mode='w', encoding='utf-8') as f:
    f.writelines(clean_data)