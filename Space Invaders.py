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


Arc=PhotoImage(file='Laser.gif')


def deplacement():
    
    global X, Y, DX, DY, Largeur, Hauteur, widthCanevas, heightCanevas


    if X + 300 + RayonX + DX > widthCanevas:
        X = X-DX
        DX = -DX
        Y = Y+10

    if X - RayonX + DX < 0:
        X = X+DX
        DX = -DX
        Y = Y+10


    X=X+DX
    Y=Y+DY
    

    Canevas.coords(Rectangle, X - RayonX, Y - RayonY, X + RayonX,Y + RayonY)
    Canevas.coords(Rectangle2, X+100-RayonX, Y-RayonY, X+100+RayonX, Y+RayonY)
    Canevas.coords(Rectangle3, X+200-RayonX, Y-RayonY, X+200+RayonX, Y+RayonY)
    Canevas.coords(Rectangle4, X+300-RayonX, Y-RayonY, X+300+RayonX, Y+RayonY)

    Mafenetre.after(80, deplacement)




Rectangle = Canevas.create_rectangle(X-RayonX, Y-RayonY, X+RayonX, Y+RayonY, fill='red')
Rectangle2 = Canevas.create_rectangle(X+100-RayonX, Y-RayonY, X+100+RayonX, Y+RayonY, fill='green')
Rectangle3 = Canevas.create_rectangle(X+200-RayonX, Y-RayonY, X+200+RayonX, Y+RayonY, fill='purple')
Rectangle4 = Canevas.create_rectangle(X+300-RayonX, Y-RayonY, X+300+RayonX, Y+RayonY, fill='blue')

Canevas.grid()

deplacement()

PosX=300
PosY=350

a=0

angle2=90

DXtir = vitesse*math.cos(angle2)
DYtir = vitesse*math.sin(angle2)



def deplacementir(a):
    
    global PosX, PosY, widthCanevas, Xtir, Ytir, Laser, X, Y


    if a == 1:
        Ytir = Ytir - 10

    if Ytir < Y + RayonY  and Ytir > Y - RayonY and Xtir > X - RayonX - 30 and Xtir < X + RayonX + 30 :
        
        Canevas.delete(Laser)
        Canevas.delete(Rectangle)

    if Ytir < Y + RayonY  and Ytir > Y - RayonY and Xtir > X + 100 - RayonX - 30 and Xtir < X + 100 + RayonX + 30 :
        
        Canevas.delete(Laser)
        Canevas.delete(Rectangle2)

    if Ytir < Y + RayonY  and Ytir > Y - RayonY and Xtir > X + 200 - RayonX - 30 and Xtir < X + 200 + RayonX + 30 :
        
        Canevas.delete(Laser)
        Canevas.delete(Rectangle3)

    if Ytir < Y + RayonY  and Ytir > Y - RayonY and Xtir > X + 300 - RayonX - 30 and Xtir < X + 300 + RayonX + 30 :
        
        Canevas.delete(Laser)
        Canevas.delete(Rectangle4)


    elif Ytir<20:


        Canevas.delete(Laser)


    Canevas.coords(Laser, Xtir, Ytir)
    Mafenetre.after(80, lambda: deplacementir(a))

    

def Clavier(event):
    
    global PosX, PosY, widthCanevas, Xtir, Ytir, Laser, DXtir, DYtir, a 
    global touche 
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
        a+=1
        Xtir=PosX
        Ytir=PosY
        Laser=Canevas.create_image(Xtir,Ytir,image=Arc)
        deplacementir(a)
   
    
    Canevas.coords(Vaisseau, PosX - 10, PosY - 10, PosX + 10, PosY + 10)



def DetruireVaisseau():
    
    global X, Y, posX, posY
    
    
    if Y < PosY + 10  and Y > PosY - 10 and X < PosX + 40 and X > PosX - 40 :
        
        Canevas.delete(Vaisseau)
        print('La partie est perdue !')
        
    Mafenetre.after(80, DetruireVaisseau)
    


Vaisseau = Canevas.create_rectangle(PosX-10, PosY-10, PosX+10, PosY+10, width=5, outline='black', fill='red')
Canevas.focus_set()
Canevas.bind('<Key>', Clavier)
Canevas.grid(padx=5, pady=5)


DetruireVaisseau()

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
