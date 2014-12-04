from tkinter import *
from tkinter import ttk
import os
#import paramiko
#import scp




werte=None

def center_window(w=300, h=200):
    ws = master.winfo_screenwidth()
    hs = master.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    master.geometry('%dx%d+%d+%d' % (w, h, x, y))

def bestaetigung():
    wert1=w1.get()
    wert2=w2.get()
    wert3=w3.get()
    wert4=w4.get()
    wert5=w5.get()
    werte=str(wert1)+"dB, "+str(wert2)+"dB, "+str(wert3)+"dB, "+str(wert4)+"dB, "+str(wert5)+"dB"
    werteAusgabe=str(wert1)+"\n"+str(wert2)+"\n"+str(wert3)+"\n"+str(wert4)+"\n"+str(wert5)
    ausgabe=Label(master,text=werte, fg="black")
    ausgabe.place(x=320,y=25)
    fo=open("C:/Users/Noah/Documents/Workspace/PPM/ausgabe.txt", "w")
    line=fo.writelines(werteAusgabe)
    
    #filePath = "C:/Users/Noah/Documents/Workspace/PPM/ausgabe.txt"
    #serverPath = "/home/pi/server/ausgabe.txt"
    #os.system("scp "+filePath+" pi@192.168.137.11:22"+serverPath)
    
    #hostname = '192.168.137.11'
    #password = 'arminmader'
    #username = "pi"
    #port = 22
    #mypath='C:/Users/Noah/Documents/Workspace/PPM/ausgabe.txt'
    #remotepath='/home/pi/server/ausgabe.txt'
    #t = paramiko.Transport((hostname, port))
    #t.connect(username=username, password=password)
    #sftp = paramiko.SFTPClient.from_transport(t)
    #sftp.put(mypath, remotepath)
    
    #client = scp.Client(host="192.168.137.11", user="pi", keyfile="arminmader")
    #client.transfer('C:/Users/Noah/Documents/Workspace/PPM/ausgabe.txt', '/home/pi/server/ausgabe.txt')
    
master = Tk()
w1=Scale(master, from_=15, to=-15)
w2=Scale(master, from_=15, to=-15)
w3=Scale(master, from_=15, to=-15)
w4=Scale(master, from_=15, to=-15)
w5=Scale(master, from_=15, to=-15)
einsatz=ttk.Frame(master, borderwidth=5, relief="sunken", width=200, height=100)


text1=Label(master, text="60Hz", fg="black")
text2=Label(master, text="230Hz", fg="black")
text3=Label(master, text="910Hz", fg="black")
text4=Label(master, text="4kHz", fg="black")
text5=Label(master, text="14kHz", fg="black")
button1=ttk.Button(master, text="Bestaetigen", command=bestaetigung)
button2=ttk.Button(master, text="Beenden", command=master.destroy)

w1.set(0)
w2.set(0)
w3.set(0)
w4.set(0)
w5.set(0)


w1.place(x=10,y=20)
text1.place(x=25,y=125)
w2.place(x=70,y=20)
text2.place(x=85,y=125)
w3.place(x=130,y=20)
text3.place(x=145,y=125)
w4.place(x=190,y=20)
text4.place(x=205,y=125)
w5.place(x=250,y=20)
text5.place(x=265,y=125)
einsatz.place(x=310,y=20)
button1.place(x=170,y=150)
button2.place(x=300,y=150)

center_window(540, 190)
mainloop()