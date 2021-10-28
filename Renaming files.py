import os

def main():
    extensions = ("jpg","JPG")
    f= open("guru99.txt","w",encoding='utf-8-sig')
    files = os.listdir(r"C:\Users\fildr\Documents\Python\New folder")
    for file in files:
        zkouska = (file[11:15])
        nazev = (file[0:9])
        main = "MAIN"
        if zkouska == main:f.write(f"{nazev}\n")
    f.close()
if __name__== "__main__":
    main()
