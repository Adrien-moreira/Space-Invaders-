from tkinter import *
import math, random



Mafenetre = Tk()
Mafenetre.title('Space Invaders')


widthCanevas = 550
heightCanevas = 400

Canevas = Canvas(Mafenetre, width = widthCanevas , height = heightCanevas)


Score = StringVar()
ScoreUtilisateur = Label( Mafenetre, textvariable = Score)
ScoreUtilisateur.grid(row = 0, column = 0)
Score.set('Score :')


Démarrer = Button(Mafenetre, text = "New Game")
Démarrer.grid(row = 5, column= 5)

BoutonQuitter = Button(Mafenetre,text='Quitter',command=Mafenetre.destroy)
BoutonQuitter.grid(row = 8)

HighScore = StringVar()
MeilleurScore = Button( Mafenetre, textvariable = HighScore)
MeilleurScore.grid(row = 2, column = 2)
HighScore.set('Highscore')

Options = StringVar()
OptionUtilisateur = Button( Mafenetre, textvariable = Options)
OptionUtilisateur.grid(row = 3, column = 2)
Options.set('Options')


Largeur = 30
Hauteur = 20

vitesse = random.uniform(1.8,2)*5
angle = 0

DX = vitesse*math.cos(angle)
DY = vitesse*math.sin(angle)

X=Largeur/2
Y=Hauteur/2

RayonX = Largeur/2
RayonY = Hauteur/2




def deplacement():
    
    global X, Y, DX, DY, Largeur, Hauteur, widthCanevas, heightCanevas

    if X + RayonX + DX > widthCanevas:
        X = X-DX
        DX = -DX

    if X - RayonX + DX < 0:
        X = X+DX
        DX = -DX

    if Y + RayonY + DY > heightCanevas:
        Y = Y-DY
        DY = -DY

    if Y - RayonY + DY < 0:
        Y = Y+DY
        DY = -DY

    X=X+DX
    Y=Y+DY

    Canevas.coords(Rectangle, X - RayonX, Y - RayonY, X + RayonX,Y + RayonY)
    Mafenetre.after(80, deplacement)




Rectangle = Canevas.create_rectangle(X-RayonX, Y-RayonY, X+RayonX, Y+RayonY, fill='red')
Canevas.grid()

deplacement()

PosX=300
PosY=350

Xtir=100
Ytir=100

angle2=90

DXtir = vitesse*math.cos(angle2)
DYtir = vitesse*math.sin(angle2)


def deplacementir():
    
    global PosX, PosY, widthCanevas, Xtir, Ytir, Oval
     
    Ytir=Ytir-DYtir
    Canevas.coords(Oval, Xtir-5, Ytir-5, Xtir+5, Ytir+5)
    

a=0

def Clavier(event):
    
    global PosX, PosY, widthCanevas, Xtir, Ytir, Oval, DXtir, DYtir, a 
    touche = event.keysym
    
    print(touche)
    


    if touche=="Right":
        PosX+=20
    if touche=="Left":
        PosX-=20


    if PosX+10>widthCanevas :
        PosX=widthCanevas-10


    if PosX-10<0:
         PosX=14      


    if touche=="space":
        
        Oval=Canevas.create_oval(Xtir-5, Ytir-5, Xtir+5, Ytir+5)
        deplacementir()
        Mafenetre.after(80, lambda : Clavier(event))

    Canevas.coords(Vaisseau, PosX-10, PosY-10, PosX +10, PosY +10)


Vaisseau = Canevas.create_rectangle(PosX-10, PosY-10, PosX+10, PosY+10, width=5, outline='black', fill='red')
Canevas.focus_set()
Canevas.bind('<Key>', Clavier)
Canevas.grid(padx=5, pady=5)

 
mainloop()







"""
import tkinter as tk

OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
] 

app = tk.Tk()

app.geometry('100x200')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

app.mainloop()
"""
