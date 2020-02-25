import os,sys,shutil  #only for security
dir="C:\\Windows\\Fonts"
print("Welcome to Windows Font Changer-Enter '-h' for help.")
while True:

    e=str(input("\n> "))
    if e=="-c":
        font=str(input("Enter font name:"))
        print("Generating strings")
        fontfuse='"Segoe UI"="'
        fontln=font+'"'
        fontfuse=fontfuse+fontln
        print("Creating registry script")
        q=open("d.txt","r")
        f=open("dl.reg","w+")
        for line in q:
            f.write(line)
        q.close()
        f.close()
        print("Configuring registry script")
        fpo=open("dl.reg","a+")
        fpo.write(fontfuse)
        fpo.close()
        print("Running script")
        try:
            os.system("dl.reg")
            flag1=True
        except:
            print("Oops, wrong font(make sure the font is installed on your system)")
            continue
        if flag1:
            os.remove("dl.reg")
            print("Please reboot your system to complete the process.")
            continue
    if e=="-r":
        os.system("h.reg")
        print("If you gave access to the computer, than your font has been resetted.")
        continue
    if e=="-l":

        from os import listdir
        for x in listdir(dir):
            if x.endswith('.ttf'):
                print(x.strip('.ttf'))
            if x.endswith('.ttc'):
                print(x.strip('.ttc'))
            if x.endswith('.fon'):
                print(x.strip('.fon'))
                continue
    if e=="-l -f":
        from os import listdir
        for p in listdir(dir):
            print(p)
            continue
    if e=="-e":
        quit()
    if e=="-h":
        print("To change font, enter '-c'; To reset font, enter '-r'; To get a list of available font files on the system, enter '-l')(enter -l -f to get them in file extensions); To quit, enter '-e'\n")
        continue
