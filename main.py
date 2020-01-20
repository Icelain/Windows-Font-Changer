import os,sys,shutil  #only for security
print("Welcome to Windows Font Changer\nDo you want to-\n1. Change font: enter 'c'\n2. Reset original font: enter 'r'")
e=str(input(""))
if e=="c":
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
    if flag1:
        os.remove("dl.reg")
        print("Please reboot your system to complete the process.")
if e=="r":
    os.system("h.reg")
    print("If you gave access to the computer, than your font has been resetted.")
