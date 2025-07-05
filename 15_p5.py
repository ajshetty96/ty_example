words =["donkey", "fuddu"]
with open("file.txt")as f:
    content= f.read()

for words in words:     
    content= content.replace(words, "#"* len(words))
   

with open("file.txt","w")as f:
    f.write(content)