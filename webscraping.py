from numpy import append
import requests
import re
from bs4 import BeautifulSoup
url = "http://cs.qau.edu.pk/faculty.php"
req = requests.get(url)
htmlContent = req.content
soup = BeautifulSoup(htmlContent, 'html.parser')
table = soup.table
text = table.text
pattern = re.compile(r'(Dr\.\s[a-zA-Z\s\.]+(Associate|Assistant))|([a-zA-Z\s\.]+Lecturer)')
matches = pattern.finditer(text)
names = []
for match in matches:
    names.append(match.group())
for i in range(len(names)):
    names[i] = names[i].replace('\n',' ')
    names[i] = " ".join(names[i].split())
    names[i] = names[i].replace(' Associate','')
    names[i] = names[i].replace(' Assistant','')
    names[i] = names[i].replace(' Lecturer','')
phonePattern = re.compile(r'\+92\-51\-9064\s[\d]{4}')
matches = phonePattern.finditer(text)
phones = []
for match in matches:
    phones.append(match.group())
phones.insert(5,'                ')
emailPattern = re.compile(r'[a-z\.]+\sat')
matches = emailPattern.finditer(text)
emails = []
for match in matches:
    emails.append(match.group())
for i in range(len(emails)):
    emails[i] = emails[i].replace(' at','')
    emails[i] = emails[i]+"@qau.edu.pk"
spaces = len(max(names,key=len)) + 1
f = open("faculty.txt", "w")
s = spaces - len("Name")
f.write("Name")
for i in range(s):
    f.write(" ")
f.write("Phone             Email\n")
for i in range(len(names)):
    s = spaces - len(names[i])
    f.write(names[i])
    for j in range(s):
        f.write(" ")
    f.write(phones[i]+"\t"+emails[i]+"\n")
f.close()