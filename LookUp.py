import os
import docx
#The error is reading files

    

#




look = input("Enter the keyword: ")
look=str(look)
#print(os.listdir(r"C:\Users\Richard\Desktop\LookupTest"))
Results=[]
def searchThroughFileDocx(filename):
    doc=docx.Document(filename)
    FullText=""
    for z in range(len(doc.paragraphs)):
        FullText+= " " + doc.paragraphs[z].text
    if look in FullText:
          Results.append(filename)

def searchThroughFile(filename):    
    with open(filename,encoding="Latin-1") as l:
        if look in l.read():
          Results.append(l)
        else:
            print(f"{l} is not one of them")


path=r"C:\Users\Richard\Desktop\LookupTest" #MOstImportant
#os.chdir(path)

for i in os.listdir(path):
    New=os.path.join(path,i)
    if os.path.isdir(New):
        for y in os.listdir(New):
            print(f"file is {y}")
            if "docx" in y:
                searchThroughFileDocx(y)
            else:
                searchThroughFile(y)
    print(f"file is {New}")
    #if os.path.isfile(New):
        #print(f"file is def a file{New}")
    if "docx" in i:
        searchThroughFileDocx(os.path.join(path,New))
    else:
        searchThroughFile(os.path.join(path,New))
print("\n\n\n")

for x,y in enumerate(Results):
    print(str(x) + ", " + y)
        
