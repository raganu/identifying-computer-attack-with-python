grams=[]
fr=open("3gramstcomplete","r")
grams3attackcomplete=fr.read();
fr=open("5gramstcomplete","r")
grams5attackcomplete=fr.read();
fr=open("7gramstcomplete","r")
grams7attackcomplete=fr.read();
fr=open("3gramsvcomplete","r")
grams3validatecomplete=fr.read();
fr=open("5gramsvcomplete","r")
grams5validatecomplete=fr.read();
fr=open("7gramsvcomplete","r")
grams7validatecomplete=fr.read();
grams.append(grams3attackcomplete)
grams.append(grams5attackcomplete)
grams.append(grams7attackcomplete)
grams.append(grams3validatecomplete)
grams.append(grams5validatecomplete)
grams.append(grams7validatecomplete)
for i in range(len(grams)):
	for j in range(i+1,len(grams)):
		print(grams[i]==grams[j])

print("\n")
grams2=[]
fr=open("3gramsfrequency_","r")
text=fr.read();
grams2.append(text)
fr=open("5gramsfrequency_","r")
text=fr.read()
grams2.append(text)
fr=open("7gramsfrequency_","r")
text=fr.read()
grams2.append(text)
fr=open("3gramsfrequency","r")
text=fr.read();
grams2.append(text)
fr=open("5gramsfrequency","r")
text=fr.read();
grams2.append(text)
fr=open("7gramsfrequency","r")
text=fr.read();
grams2.append(text)
print(grams[0]==grams2[0])
print(grams[1]==grams2[1])
print(grams[2]==grams2[2])
print(grams[3]==grams2[3])
print(grams[4]==grams2[4])
print(grams[5]==grams2[5])

