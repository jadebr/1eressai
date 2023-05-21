import time
import pygame 
from colorama import init, Fore, Style

pygame.init()
son = pygame.mixer.Sound("audio/onlymp3.to - Ori and the Blind Forest – Main Theme [Menu Music]-76qRF5-qvZM-256k-1657169721742.mp3")
son.play() 
init() # initialisation de colorama


# Présentation
color = Fore.YELLOW + Style.BRIGHT 

for char in "\nBonjour et bienvenue sur ce mini jeu interactif.\n\n":
            print(char, end='', flush=True)
            time.sleep(0.015)
           

# Création personnage par défaut 

class Personnage:
    def __init__(self, nom, niveau, exp, vie, viemax, force, magie, ruse, résistanceforce, résistancemagie, résistanceruse,):
        self.nom = nom
        self.niveau = niveau
        self.exp = exp
        self.vie = vie
        self.viemax = viemax
        self.force = force
        self.magie = magie
        self.ruse = ruse
        self.résistanceforce = résistanceforce
        self.résistancemagie = résistancemagie
        self.résistanceruse = résistanceruse
        

    def attaquer(self, cible):
        degats_force = round(self.force / cible.résistanceforce)
        degats_magie = round(self.magie / cible.résistancemagie)
        degats_ruse = round(self.ruse / cible.résistanceruse)
        degats_total = degats_force + degats_magie + degats_ruse
        cible.vie -= degats_total
        color = Fore.RED + Style.BRIGHT 
        print(self.nom, "attaque", cible.nom, "et lui inflige", degats_total, "points de dégâts.")
        print(Style.RESET_ALL)


    def se_soigner(self):
        soin = 10
        if self.vie + soin > self.max_pv:
            soin = self.viemax - self.vie
            self.vie = self.viemax
        else:
            self.vie += soin
        color = Fore.RED + Style.BRIGHT 
        print(self.nom, "se soigne et récupère", soin, "points de vie.")
        print(Style.RESET_ALL)

    
    def regenerer(self):
        pv_max = self.max_pv
        pv_perdus = pv_max - self.vie 
        pv_gagnes = int(pv_perdus * 0.25)  # calcul des points de vie à regagner en pourcentage
        self.vie += pv_gagnes
        if self.vie > pv_max:
            self.vie = pv_max  
        color = Fore.RED + Style.BRIGHT 
        print(self.nom, "se soigne et récupère", pv_gagnes, "points de vie.")
        print(Style.RESET_ALL)

         
    def victoire(self):
         if Ennemi.vie <=0:
            self.exp += 100
            color = Fore.RED + Style.BRIGHT 
            for char in "Bien joué tu as gagné !":
                 print(char, end='', flush=True)
                 time.sleep(0.015)
                 print(Style.RESET_ALL)

    
    def defaite(self):   
         if self.vie <=0:
            self.exp -= 50
            color = Fore.RED + Style.BRIGHT 
            for char in "Oh non c'est dommage...":
                print(char, end='', flush=True)
                time.sleep(0.015)
                print(Style.RESET_ALL)


    def gagner_exp(self, victoire,):
        if victoire :
            if self.exp >= 1000:
                self.niveau+=1
                self.exp -= 1000
                color = Fore.RED + Style.BRIGHT 
                for char in "Tu as gagné 1 niveau.":
                 print(char, end='', flush=True)
                 time.sleep(0.015)
                 print(Style.RESET_ALL)
    
    def perdre_exp(self, defaite,):
        if defaite :
             if self.exp < 0:
                self.niveau -= 1
                color = Fore.RED + Style.BRIGHT 
                for char in "Tu as perdu 1 niveau":
                     print(char, end='', flush=True)
                     time.sleep(0.015)
                     print(Style.RESET_ALL)
                     if joueur1.niveau <= 0:
                         color = Fore.RED + Style.BRIGHT 
                         for char in "Tu es mort. Retente ta chance.":
                          print(char, end='', flush=True)
                          time.sleep(0.015)
                          exit()
                          print(Style.RESET_ALL)

                

# Création ennemi par défaut
 
class Ennemi:
    def __init__(self, nom, vie, résistanceforce, résistancemagie, résistanceruse,  force, magie, ruse, viemax):
        self.nom = nom
        self.vie = vie
        self.résistanceforce = résistanceforce
        self.résistancemagie = résistancemagie
        self.résistanceruse = résistanceruse
        self.force = force
        self.magie = magie
        self.ruse = ruse
        self.max_pv = viemax

    def attaquer(self, cible):
        degats_force = round(self.force / joueur1.résistanceforce)
        degats_magie = round(self.magie / joueur1.résistancemagie)
        degats_ruse = round(self.ruse / joueur1.résistanceruse)
        degats_total = degats_force + degats_magie + degats_ruse
        cible.vie -= degats_total
        color = Fore.BLUE + Style.BRIGHT 
        print(self.nom, "passe à l'attaque et t'inflige", degats_total, "points de dégâts.")
        print(Style.RESET_ALL)

    def defaite(self):   
         if self.vie <=0:
            color = Fore.BLUE + Style.BRIGHT 
            for char in "J'ai était vaincu...":
                print(char, end='', flush=True)
                time.sleep(0.015)
                print(Style.RESET_ALL)


# Demander le nom
nom = input("Tout d'abord, il te faut un nom. \nComment souhaites-tu t'appeler ?\n")
joueur1 = Personnage(nom, 1, 0, 100,  100, 0, 0, 0, 10, 10, 10,)
ennemiG1 = Ennemi("Gluant de niveu 1", 100, 7, 5, 10,  10, 0, 0, 100)
ennemiG2 = Ennemi("Gluant de niveau 2", 100, 7, 5, 10,  10, 0, 0, 100)

while True:
    
    confirmation = input("Tu souhaites bien t'appeler " + nom + " ? Oui/Non ")

    if confirmation.lower() == 'oui':
        for char in "Alors passons à la suite " + nom + ".\n":
            print(char, end='', flush=True)
            time.sleep(0.015)
        break 
    elif confirmation.lower() == 'non':
        nom = input("Comment souhaites-tu t'appeler ?\n")
        joueur1.nom = nom
        continue 
    else:
        for char in "Je n'ai pas compris ta réponse. Il faut que tu répondes 'oui' ou 'non'.\n":
            print(char, end='', flush=True)
            time.sleep(0.015)

            
    print(Style.RESET_ALL)

# """ def rencontre(joueur1):
#     print("Un ennemi apparait : " + G1.nom)
#     while joueur1.vie > 0 and G1.vie > 0:
#         print(joueur1.nom + " : " + str(joueur1.vie) + "PV")
#         print(G1.nom + " : " + str(G1.vie) + "PV")
#         action = input("Que voulez-vous faire ? (attaquer / se soigner)")
#         if action == "attaquer":
#             joueur1.attaquer(G1)
#         elif action == "se soigner":
#             joueur1.se_soigner()
#         else:
#             print("Action invalide")
#         if G1.vie > 0:
#             G1.attaquer(joueur1)
#     if joueur1.vie <= 0:
#         joueur1.defaite()
#     elif G1.vie <= 0:
#         joueur1.victoire()
#         joueur1.gagner_exp(True)
#     else:
#         print("Erreur de combat")


# Fin

for char in "C'est ici que le programme s'achève merci d'être resté !\n\n":
        print(char, end='', flush=True)
        time.sleep(0.015)

son.stop()
pygame.quit()