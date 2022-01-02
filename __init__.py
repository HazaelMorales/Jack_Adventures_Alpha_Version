#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# ==============LIBRERIAS=================
import pygame
import time
import sys
import random
from pygame.locals import *
from pygame.constants import RLEACCEL, K_q
from builtins import *
from pygame.pypm import FALSE
from tkinter import PhotoImage

pygame.init()

# ==============CONSTANTES=================
black = (0,0,0)
cafe= (130, 34, 13)
cafeclaro= (225, 120, 97)
WIDTH = 800
HEIGHT = 600
MposX =300
MposY=498
gameDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
cont=6
direc=True
i=0
xixf={}#xinicial y xfinal
Rxixf={}
salto=False 
salto_T=False

# ==============IMAGEN=================
def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error.message:
                raise SystemExit.message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image


def hola(imagen1,imagen2):
        pygame.init()    
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        jack = imagen(imagen1,True)
        fondo = imagen(imagen2)      
        fondo = pygame.transform.scale(fondo,(WIDTH, HEIGHT))
        jack = pygame.transform.scale(jack,(350, 150))
        screen.blit(fondo, (0, 0))
        screen.blit(jack, (210, 10))

def things_dodged(count,mensaje,posicionX,posicionY):
    font = pygame.font.SysFont(None, 25)
    text = font.render(mensaje+str(count), True, cafe)
    gameDisplay.blit(text,(posicionX,posicionY))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def botones(msg,x,y,w,h,ic,ac,accion = None):
    mouse = pygame.mouse.get_pos()
    click= pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse [1] > y :
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and accion != None:
            accion ()
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
        
    SmallText=pygame.font.Font('freesansbold.ttf',20)
    TextSurf,TextRect=text_objects(msg, SmallText)
    TextRect.center=(x+(w/2),(y+(h/2)))
    gameDisplay.blit (TextSurf, TextRect)

def pintar_imagen(ac,x,y,w,h):
    pygame.draw.rect(gameDisplay,ac,(x,y,w,h))


# ==============MENUS=================
def menu1():
    pygame.display.set_caption("menu")
    intro = True
    hola("resources/images/Logo.png","resources/images/fondo.png")
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        botones("Jugar",324,200,150,75,cafe,cafeclaro,menu2)
        botones("Configuracion",324,300,150,75,cafe,cafeclaro,quit)
        botones("Salir",324,400,150,75,cafe,cafeclaro,quit)
        pygame.display.update()
        clock.tick(60)
        pygame.display.flip()

def menu2():
    hola("resources/images/Logo.png","resources/images/fondo.png") 
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()     
        botones("Nivel 1",324,200,150,75,cafe,cafeclaro,nivel_1)
        botones("Nivel 2",324,300,150,75,cafe,cafeclaro,nivel_2)
        botones("Salir",324,400,150,75,cafe,cafeclaro,quit)
        
        pygame.display.update()
        clock.tick(60)
        pygame.display.flip()

 
# ==============TECLADO=================
def teclado(v):
    teclado = pygame.key.get_pressed()
     
    global MposX,MposY
    global cont, direc,salto,salto_T
   
    if teclado[K_SPACE] and teclado[K_RIGHT] and salto_T==False:
        salto_T=True
    
    elif teclado[K_SPACE] and teclado[K_LEFT] and salto_T==False and MposX > 2:
        salto_T=True
    
    if teclado[K_RIGHT] and salto==False and salto_T==False:
        MposX+=v
        cont+=1
        direc=True
    elif teclado[K_LEFT] and MposX > 2 and salto==False and salto_T==False:
        MposX-=v
        cont+=1
        direc=False
    elif teclado[K_SPACE] and salto==False and salto_T==False: 
        salto=True
    else: 
        cont = 6
    return
  #salto = True
        #SALTO
    #else :
         #cont=
    
 
# ==============SPRITE=================
def sprite():
    global cont
 
    xixf[0]=(7,2,30,49)
    xixf[1]=(58,1,30,49)
    xixf[2]=(107,2,33,49)
    xixf[3]=(8,49,29,52)
    xixf[4]=(58,51,30,48)
    xixf[5]=(7,99,30,48)
 
    Rxixf[0]=(10,104,32,48)
    Rxixf[1]=(60,54,31,48)
    Rxixf[2]=(8,50,40,48)
    Rxixf[3]=(107,3,40,49)
    Rxixf[4]=(59,3,40,49)
    Rxixf[5]=(7,3,40,49)
   
    p=6
    global i
       
    if cont==p:
        i=0
    if cont==p*2:
        i=1
    if cont==p*3:
        i=2
    if cont==p*4:
        i=3
    if cont==p*5:
        i=4
    if cont==p*6:
        i=5
        cont=0
    return
 
def message_display1(text):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (400,360)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)

def crash():
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    TextRect.center = ((WIDTH/2),(HEIGHT/2))
    gameDisplay.blit(TextSurf, TextRect)
    hola("resources/images/Logo.png","resources/images/aviso1.jpg")

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()       
        #gameDisplay.fill(white)
        botones("volver Al menu",1,450,200,50,cafe,cafeclaro,menu1)
        botones("Salir",600,450,200,50,cafe,cafeclaro,quit)

        pygame.display.update()
        clock.tick(15) 

# ==============NIVEL_1=================
def nivel_1():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Nivel 1")
    fondo = imagen("resources/images/fondo1.jpg")
    vida=imagen("resources/images/vida.png", True)  
    jack = imagen("resources/images/jack3.png",True)  
    jack_inv=pygame.transform.flip(jack,True,False)
    xd = pygame.transform.scale(jack,(150, 200))
    xd_inv = pygame.transform.scale(jack_inv,(150, 200))
    carro=imagen("resources/images/carro.png",True)
    carro_reversa=pygame.transform.flip(carro,True,False);
    basura=imagen("resources/images/basura.png",True)
    posY=0
    velocidad1=3
    velocidad=3
    derecha=True
    velocidad_jack=0.001
    posX=600
    thing_startx=0
    dodged = 3
    puntos=0
    clock = pygame.time.Clock()
    v=6
    while True:
        # ==============PINTAR IMAGENES=================
        fondo = pygame.transform.scale(fondo, (800, 600))
        pintar_imagen(cafe,thing_startx, posY, 40, 40)
        screen.blit(fondo, (0, 0))
        # ==============BASURA=================
        if posY > HEIGHT: 
            thing_startx = random.randrange(0,500)
            posY=0-HEIGHT
            dodged-=1
        if dodged<1:
            crash()
        if thing_startx!=posX:
            screen.blit(basura, ( thing_startx, posY))
            posY+=velocidad1+1
        if posY>360:
            posY+=160
            if MposX>thing_startx and MposX < thing_startx +40 or MposX +20 > thing_startx and MposX+20 < thing_startx +40 :
                posY=0-HEIGHT
                thing_startx = random.randrange(0,500)
                puntos+=1

       # ==============VELOCIDAD DE OBJETOS=================
        if thing_startx %1 ==0:
            posY+=3
            v+=0.001
        
        # ==============PUNTAJE=================
        things_dodged(puntos, "Puntos  ",75 ,345)
       
        # ==============CONTADOR DE VIDAS=================
        if dodged==1:
            screen.blit(vida, (35, 295))
        if dodged==2:
            screen.blit(vida, (65, 295))
            screen.blit(vida, (95, 295))
        if dodged==3:
            screen.blit(vida, (68, 295))
            screen.blit(vida, (98, 295))
            screen.blit(vida, (128, 295))
        if MposX>800:
            nivel_2()

        # ==============CARRO=================
        if derecha==True:
                screen.blit(carro, ( posX, 2))
                
                
                if posX<900:
                    posX+= velocidad
                else    :
                    derecha=False
                  
        if derecha==False:
                screen.blit(carro_reversa, ( posX, 100))
                if posX>-100:
                    posX-=velocidad
                  
                else    :
                    derecha=True    
        sprite()
        teclado(v)
        # ==============JACK=================
        if direc==True:
            screen.blit(xd, ( MposX, 390),(xixf[i]))
   
        if direc==False:
            screen.blit(xd_inv, ( MposX, 390),(Rxixf[i]))
            
        
        clock.tick(60)
        pygame.display.flip()
        
        # ==============CERRAR VENTANA=================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    return 0


# ==============NIVEL_2=================
def nivel_2():
    global salto_T
    bajada=False
    bajada_T=False
   
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Nivel 2")
   
    fondo1 = imagen("resources/images/Completa1.png")
    jack = imagen("resources/images/jack3.png",True)  
    jack_inv=pygame.transform.flip(jack,True,False)
    xd = pygame.transform.scale(jack,(150, 200))
    xd_inv = pygame.transform.scale(jack_inv,(150, 200))
    v=3
    while True: 
        screen.blit(fondo1, (0, 0))    
        fondo1 = pygame.transform.scale(fondo1, (800, 600))
        
        sprite()
        teclado(v)
        
        global MposX,MposY,salto,direc
        
        if direc==True:
            screen.blit(xd, ( MposX, MposY),(xixf[i]))
   
        if direc==False:
            screen.blit(xd_inv, ( MposX, MposY),(Rxixf[i]))
        
        # ==============SALTO NORMAL=================
        if salto==True:
            if bajada==False:
                MposY-=4
                
            if bajada==True:
                MposY+=4
                
            if MposY==390:
                bajada=True
                
            if MposY==498:
                bajada=False 
                salto=False
        
        # ==============SALTO CON MOVIMIENTO=================  
        if salto_T==True and direc==True:
            if bajada_T==False:
                MposY-=3
                MposX+=2
               
            if bajada_T==True:
                MposY+=3
                MposX+=2
           
            if MposY==390:
                bajada_T=True
           
            if MposY==498:
                bajada_T=False
                salto_T=False
                
        elif salto_T==True and direc==False:                
            if bajada_T==False:
                MposY-=3
                MposX-=2
               
            if bajada_T==True:
                MposY+=3
                MposX-=2
           
            if MposY==390:
                bajada_T=True
           
            if MposY==498:
                bajada_T=False
                salto_T=False 
        if MposX>800:
             escena_1()
        
        pygame.display.flip()
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

# ==============MOSTRAR SEGUNDO ESCENARIO DEL NIVEL 4=================                 
def escena_1 ():
    global salto_T
    bajada=False
    bajada_T=False
   
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Nivel 4")
    
    fondo1 = imagen("resources/images/Completa2.png")
    jack = imagen("resources/images/jack3.png",True)  
    jack_inv=pygame.transform.flip(jack,True,False)
    xd = pygame.transform.scale(jack,(150, 200))
    xd_inv = pygame.transform.scale(jack_inv,(150, 200))
    v=3
    Z=0

    while True: 
        
        screen.blit(fondo1, (0, 0))    
        fondo1 = pygame.transform.scale(fondo1, (800, 600))
        
        sprite()
        teclado(v)
       
        global MposX,MposY,salto,direc
        Z= MposX - WIDTH
        if direc==True:
            screen.blit(xd, (Z, MposY),(xixf[i]))
   
        if direc==False:
            screen.blit(xd_inv, (Z, MposY),(Rxixf[i]))
        if Z<-2:
            nivel_2()
        
        # ==============SALTO NORMAL================= 
        if salto==True:
            if bajada==False:
                MposY-=4
                
            if bajada==True:
                MposY+=4
                
            if MposY==390:
                bajada=True
                
            if MposY==498:
                bajada=False 
                salto=False
        
        # ==============SALTO CON MOVIMIENTO=================    
        if salto_T==True and direc==True:
            if bajada_T==False:
                MposY-=3
                MposX+=2
               
            if bajada_T==True:
                MposY+=3
                MposX+=2
           
            if MposY==390:
                bajada_T=True
           
            if MposY==498:
                bajada_T=False
                salto_T=False
                
        elif salto_T==True and direc==False:                
            if bajada_T==False:
                MposY-=3
                MposX-=2
               
            if bajada_T==True:
                MposY+=3
                MposX-=2
           
            if MposY==390:
                bajada_T=True
           
            if MposY==498:
                bajada_T=False
                salto_T=False 
        
        pygame.display.flip()
        clock.tick(60)
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()      
menu1()
menu2() 