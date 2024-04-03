import time

class Cellule:
  def __init__(self):
    self.__actuel= False
    self.__futur=False
    self.__voisins= []
    self._nbVoisinsVivants = 0
    
  def est_vivant(self): #renvoie un bool true ou false
    return self.__actuel
  
  def set__voisins(self, L): #stock le nombre de voisins vivants
    self.__voisins= L

  def get_voisins(self):  #renvoie les voisins vivants
    return self.__voisins
  
  def naitre(self): #fait naitre une cellule pour le prochain jour
    self.__futur=True

  def mourir (self): #fait mourir la cellule pour le prochain jour 
    self.__futur=False
  
  def get_futur(self):
    return self.__futur
  
  def actualiser(self): #actualise la cellule pour savoir si elle sera vivante ou non pour le nouveaux jour
    self.__actuel=self.__futur

 
  def nbVoisinsVivants(self): #renvoie un int du nombre de voisin vivant
    return len(self.get_voisins())
  
  
  def EtatFutur (self): #permet de savoir si la cellule va mourir le prochain jour
    if self.nbVoisinsVivants()== 2:
      if self.est_vivant() == True:
        self.__futur == True  
        return self.__futur
      else:
        self.__futur == False 
        return self.__futur

    elif self.nbVoisinsVivants() == 3:
      if self.est_vivant() == True :
        self.__futur = self.__actuel
        return self.__futur
      else:
        self.naitre()
        return self.__futur

    else:
      self.mourir()
      return self.__futur

 
  def __repr__(self):   #renvoie un print avec X si la cellule est vivante et . si elle est morte
    if self.__actuel :
      return "X"
    else:
      return "." 



class Grille:
  def __init__(self, x, y):
    self.__largeur = x
    self.__hauteur = y
    self.__jour = 0
    self.__tableau = [[Cellule() for largeur_cellule in range(self.__largeur)] for hauteur_cellule in range(self.__hauteur)] #crée une liste avec le nombre self.__hauteur de listes dedans avec dans ces listes là le nombre self.__largeur de cellules
  
  def get__tableau(self): #renvoie le tableau creer
    return self.__tableau
 
  def getXY(self, i , j): #renvoie la cellule des coordonnées i, j
    return self.__tableau[j][i]

  def creer_voisins(self, i, j): #toutes les conditions verifie si la cellule est sur un des bords ou non et renvoie donc une liste de ces voisins vivants seulement
    L= []
    L2 = [i,j]
    for x in range(i-1, i+1):
      for y in range (j-1, j+1):
        if i-x ==  1 or i-x == -1 or i-x == 0:
          if j-y == 1 or j-y == -1 or j-y == 0:
            if self.getXY(x,y).est_vivant() == True:
              L.append([x,y]) 
 
    for l in L:  # pour sortir les coordonné i,j de la liste
        if l == L2:
          L.remove(l)
    self.getXY(i,j).set__voisins(L)
    return L
 
  def actualiser_voisin(self): #permet de parcourir tout les cellule pour creer leur voisins
    for i in range(self.__largeur):
      for j in range(self.__hauteur):
        self.creer_voisins(i,j)
  
  def derouler_jour(self):
    jour = 'Combien de jour voulez vous que le jeu dure?'
    self.__jour = int(input(jour))
    for i in range(self.__jour):
     t = 'jour: {}'
     print(t.format(i+1))
     print(self)
     self.actualiser_voisin()   
     for i in range(self.__largeur):
      for j in range(self.__hauteur):
        self.getXY(i,j).EtatFutur()
     for i in range(self.__largeur):
      for j in range(self.__hauteur):
        self.getXY(i,j).actualiser()
     for i in range(self.__largeur):
       for j in range(self.__hauteur):
         self.creer_voisins(i,j)
     self.actualiser_voisin
     time.sleep(1)

  def __repr__(self): #renvoie les listes sous la forme d'un tableau
    values = '\n'.join([str(i) for i in self.__tableau])
    return values

  def Conway(self): #permet d'executer le jeux
    self.actualiser_voisin()
    print("Voici le tableau choisi")
    print(self)
    y = 'coordonné y de la cellule que vous voulait faire naitre? '
    x = 'coordonné x de la cellule que vous voulait faire naitre. '
    D = ''
    while D != "OUI":
      D = 'voici le tableau sur lequel le jeu va ce derouler.\ntappez OUI pour demarer sinon appuyer sur ENTRER '
      X = input(x)
      Y = input(y) 
      self.getXY(int(X),int(Y)).naitre()
      self.getXY(int(X),int(Y)).actualiser()
      print(self)
      D = str(input(D))
    self.derouler_jour()



AB = Grille(3,3)
print(AB)
AB.getXY(0,0).naitre()
AB.getXY(1,0).naitre()
AB.getXY(2,0).naitre()
AB.getXY(2,1).naitre()
AB.getXY(2,2).naitre()
AB.getXY(0,0).actualiser()
AB.getXY(1,0).actualiser()
AB.getXY(2,0).actualiser()
AB.getXY(2,1).actualiser()
AB.getXY(2,2).actualiser()
AB.actualiser_voisin()

print(AB.Conway())



