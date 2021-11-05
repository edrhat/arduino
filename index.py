from tkinter import *
import tkinter as tk
import os

#Imagens TAMANHO: 175x120
#TAMANHO DA JANELAS SECUNDÁRIAS 1000x600

class Tela():

    def __init__(self, master):

        
     


        hc06 = tk.PhotoImage(file="hc06.png")
        self.labelhc06 = tk.Label(janela, image=hc06)
        self.labelhc06.hc06 = hc06
        self.labelhc06.place(x=40,y=200)
        self.labelhc06.bind("<Enter>", self.infohc06)
        self.labelhc06.bind("<Leave>", self.fecharinfohc06)
        self.labelhc06.bind("<Button-1>", self.clickhc06)
     


        teclado_matricial = tk.PhotoImage(file="teclado_matricial.png")
        self.labelteclado = tk.Label(janela, image=teclado_matricial)
        self.labelteclado.teclado_matricial = teclado_matricial
        self.labelteclado.place(x=250,y=200)
        self.labelteclado.bind("<Enter>", self.infoteclado)
        self.labelteclado.bind("<Leave>", self.fecharteclado)
        self.labelteclado.bind("<Button-1>", self.clickteclado)

        l298n = tk.PhotoImage(file="l298n.png")
        self.labell298n = tk.Label(janela, image=l298n)
        self.labell298n.l298n = l298n
        self.labell298n.place(x=460,y=200)
        self.labell298n.bind("<Enter>", self.infol298n)
        self.labell298n.bind("<Leave>", self.fecharl298n)
        self.labell298n.bind("<Button-1>", self.clickl298n)

        joystick = tk.PhotoImage(file="joystick.png")
        self.labeljoystick = tk.Label(janela, image=joystick)
        self.labeljoystick.joystick = joystick
        self.labeljoystick.place(x=670,y=200)
        self.labeljoystick.bind("<Enter>", self.infojoystick)
        self.labeljoystick.bind("<Leave>", self.fecharjoystick)
        self.labeljoystick.bind("<Button-1>", self.clickjoystick)

        ultrasonico = tk.PhotoImage(file="ultrasonico.png")
        self.labelultrasonico = tk.Label(janela, image=ultrasonico)
        self.labelultrasonico.ultrasonico = ultrasonico
        self.labelultrasonico.place(x=880,y=200)
        self.labelultrasonico.bind("<Enter>", self.infoultrasonico)
        self.labelultrasonico.bind("<Leave>", self.fecharultrasonico)
        self.labelultrasonico.bind("<Button-1>", self.clickultrasonico)

        rele = tk.PhotoImage(file="rele.png")
        self.labelrele = tk.Label(janela, image=rele)
        self.labelrele.rele = rele
        self.labelrele.place(x=40,y=400)
        self.labelrele.bind("<Enter>", self.inforele)
        self.labelrele.bind("<Leave>", self.fecharrele)
        self.labelrele.bind("<Button-1>", self.clickrele)

        lcd = tk.PhotoImage(file="lcd.png")
        self.labellcd = tk.Label(janela, image=lcd)
        self.labellcd.lcd = lcd
        self.labellcd.place(x=250,y=400)
        self.labellcd.bind("<Enter>", self.infolcd)
        self.labellcd.bind("<Leave>", self.fecharlcd)
        self.labellcd.bind("<Button-1>", self.clicklcd)

    def infohc06(self, event):
        infoHc06 = tk.PhotoImage(file="infoHc06.png")
        self.labelhc062 = tk.Label(janela, image=infoHc06)
        self.labelhc062.infoHc06 = infoHc06
        self.labelhc062.place(x=40,y=325)

        self.hc06 = tk.Label(janela, text="Clique para saber preços")
        self.hc06["font"] = ("Arial", "12")
        self.hc06.config(bg="green", foreground="white")
        self.hc06.place(x=40,y=170)

        self.labelhc06.config(bg="green")

        janela.config(cursor="hand2")

    

    def fecharinfohc06(self, event):
   
        self.labelhc062.place(x=1800,y=320)
        self.hc06.place(x=1800,y=320)
        self.labelhc06.config(bg="white")
        janela.config(cursor="")

    def clickhc06(self, event):


        janela2 = tk.Tk()

        janela_hc06 = tk.PhotoImage(master=janela2, file="janela_hc06.png")
        labeljanela_hc06 = tk.Label(janela2, image=janela_hc06)
        labeljanela_hc06.place(x=50,y=30)

        janela2.resizable(width=False, height=False)
        janela2.geometry("1000x600+100+20")
        janela2.title("MÓDULO BLUETOOTH - HC06")
        janela2.mainloop()



        #link = "https://www.google.com/search?q=intext%3Ahc06+intext%3Apre%C3%A7o"
        #os.system("start chrome "+link)

    def infoteclado(self, event):
        infoteclado = tk.PhotoImage(file="infoteclado.png")
        self.labelteclado2 = tk.Label(janela, image=infoteclado)
        self.labelteclado2.infoteclado = infoteclado
        self.labelteclado2.place(x=250,y=325)

        self.teclado = tk.Label(janela, text="Clique para saber preços")
        self.teclado["font"] = ("Arial", "12")
        self.teclado.config(bg="green", foreground="white")
        self.teclado.place(x=250,y=170)

        self.labelteclado.config(bg="green")

        janela.config(cursor="hand2")

    def fecharteclado(self, event):
   
        self.teclado.place(x=1800,y=320)
        self.labelteclado2.place(x=1800,y=320)
        self.labelteclado.config(bg="white")
        janela.config(cursor="")

    def clickteclado(self, event):


        janela3 = tk.Tk()

        janela_teclado = tk.PhotoImage(master=janela3, file="janela_teclado.png")
        labeljanela_teclado = tk.Label(janela3, image=janela_teclado)
        labeljanela_teclado.place(x=30,y=90)

        janela3.resizable(width=False, height=False)
        janela3.geometry("1000x600+100+20")
        janela3.title("TECLADO MATRICIAL 4X4")
        janela3.mainloop()

        
        #link = "https://www.google.com/search?q=intext%3Ateclado+matricial+intext%3Apre%C3%A7o"
        #os.system("start chrome "+link)

    

    def infol298n(self, event):
        infol298n = tk.PhotoImage(file="infol298n.png")
        self.labell298n2 = tk.Label(janela, image=infol298n)
        self.labell298n2.infol298n = infol298n
        self.labell298n2.place(x=450,y=325)

        self.l298n = tk.Label(janela, text="Clique para mais informações")
        self.l298n["font"] = ("Arial", "12")
        self.l298n.config(bg="green", foreground="white")
        self.l298n.place(x=450,y=170)

        self.labell298n.config(bg="green")

        janela.config(cursor="hand2")

    def fecharl298n(self, event):
   
        self.l298n.place(x=1800,y=320)
        self.labell298n2.place(x=1800,y=320)
        self.labell298n.config(bg="white")
        janela.config(cursor="")

    def clickl298n(self, event):

        janela4 = tk.Tk()

        janela_l298n = tk.PhotoImage(master=janela4, file="janela_l298n.png")
        labeljanela_l298n = tk.Label(janela4, image=janela_l298n)
        labeljanela_l298n.place(x=20,y=80)

        janela4.resizable(width=False, height=False)
        janela4.geometry("1000x600+100+20")
        janela4.title("PONTE H - L298N")
        janela4.mainloop()

        #link = "https://www.google.com/search?q=intext%3Al298n+intext%3Apre%C3%A7o"
        #os.system("start chrome "+link)

    def infojoystick(self, event):
        infojoystick = tk.PhotoImage(file="infojoystick.png")
        self.labeljoystick2 = tk.Label(janela, image=infojoystick)
        self.labeljoystick2.infojoystick = infojoystick
        self.labeljoystick2.place(x=670,y=325)

        self.joystick = tk.Label(janela, text="Clique para mais informações")
        self.joystick["font"] = ("Arial", "12")
        self.joystick.config(bg="green", foreground="white")
        self.joystick.place(x=670,y=170)

        self.labeljoystick.config(bg="green")

        janela.config(cursor="hand2")

    def fecharjoystick(self, event):
   
        self.joystick.place(x=1800,y=320)
        self.labeljoystick2.place(x=1800,y=320)
        self.labeljoystick.config(bg="white")
        janela.config(cursor="")

    def clickjoystick(self, event):

        janela5 = tk.Tk()

        janela_joystick = tk.PhotoImage(master=janela5, file="janela_joystick.png")
        labeljanela_joystick = tk.Label(janela5, image=janela_joystick)
        labeljanela_joystick.place(x=100,y=80)

        janela5.resizable(width=False, height=False)
        janela5.geometry("1000x600+100+20")
        janela5.title("JOYSTICK")
        janela5.mainloop()

    def infoultrasonico(self, event):
        infoultrasonico = tk.PhotoImage(file="infoultrasonico.png")
        self.labelultrasonico2 = tk.Label(janela, image=infoultrasonico)
        self.labelultrasonico2.infoultrasonico = infoultrasonico
        self.labelultrasonico2.place(x=880,y=325)

        self.ultrasonico = tk.Label(janela, text="Clique para mais informações")
        self.ultrasonico["font"] = ("Arial", "12")
        self.ultrasonico.config(bg="green", foreground="white")
        self.ultrasonico.place(x=880,y=170)

        self.labelultrasonico.config(bg="green")

        janela.config(cursor="hand2")

    def fecharultrasonico(self, event):
   
        self.ultrasonico.place(x=1800,y=320)
        self.labelultrasonico2.place(x=1800,y=320)
        self.labelultrasonico.config(bg="white")
        janela.config(cursor="")

    def clickultrasonico(self, event):

        janela6 = tk.Tk()

        janela_ultrasonico = tk.PhotoImage(master=janela6, file="janela_ultrasonico.png")
        labeljanela_ultrasonico = tk.Label(janela6, image=janela_ultrasonico)
        labeljanela_ultrasonico.place(x=30,y=80)

        janela6.resizable(width=False, height=False)
        janela6.geometry("1000x600+100+20")
        janela6.title("JOYSTICK")
        janela6.mainloop()

    def inforele(self, event):
        inforele = tk.PhotoImage(file="inforele.png")
        self.labelrele2 = tk.Label(janela, image=inforele)
        self.labelrele2.inforele = inforele
        self.labelrele2.place(x=40,y=80)

        self.rele = tk.Label(janela, text="Clique para saber mais informações")
        self.rele["font"] = ("Arial", "12")
        self.rele.config(bg="green", foreground="white")
        self.rele.place(x=100,y=60)

        self.labelrele.config(bg="green")

        janela.config(cursor="hand2")
    
    def fecharrele(self, event):
   
        
        self.rele.place(x=1800,y=320)
        self.labelrele2.place(x=1800,y=320)
        self.labelrele.config(bg="white")
        janela.config(cursor="")

    def clickrele(self, event):


        janela7 = tk.Tk()

        janela_rele = tk.PhotoImage(master=janela7, file="janela_rele.png")
        labeljanela_rele = tk.Label(janela7, image=janela_rele)
        labeljanela_rele.place(x=50,y=30)

        janela7.resizable(width=False, height=False)
        janela7.geometry("1000x600+100+20")
        janela7.title("RELAY")
        janela7.mainloop()

    def infolcd(self, event):
        infolcd = tk.PhotoImage(file="infolcd.png")
        self.labellcd2 = tk.Label(janela, image=infolcd)
        self.labellcd2.infolcd = infolcd
        self.labellcd2.place(x=250,y=80)

        self.lcd = tk.Label(janela, text="Clique para saber mais informações")
        self.lcd["font"] = ("Arial", "12")
        self.lcd.config(bg="green", foreground="white")
        self.lcd.place(x=350,y=54)

        self.labellcd.config(bg="green")

        janela.config(cursor="hand2")
    
    def fecharlcd(self, event):
   
        
        self.lcd.place(x=1800,y=320)
        self.labellcd2.place(x=1800,y=320)
        self.labellcd.config(bg="white")
        janela.config(cursor="")

    def clicklcd(self, event):


        janela7 = tk.Tk()

        janela_lcd = tk.PhotoImage(master=janela7, file="janela_lcd.png")
        labeljanela_lcd = tk.Label(janela7, image=janela_lcd)
        labeljanela_lcd.place(x=10,y=30)

        janela7.resizable(width=False, height=False)
        janela7.geometry("1000x600+100+20")
        janela7.title("RELAY")
        janela7.mainloop()


janela = tk.Tk()
Tela(janela)

janela.config(bg="white")
janela.geometry("1255x800+10+2")
janela.title("Componentes de Automação Residencial")
janela.resizable(width=False, height=False)
janela.mainloop()
