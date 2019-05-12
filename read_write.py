fw = open('lekhalekhi.txt','w')
fw.write("I love eating chicks.\n\n")
fw.write("Do you ?")
fw.close()

fr = open('lekhalekhi.txt','r')
text = fr.read()
print(text)
fr.close()