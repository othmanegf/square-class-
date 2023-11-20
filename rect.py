class rectangle():
    
    def __init__(self,longeur,largeur):
        self.longeur = longeur
        self.largeur = largeur
    
    def perimetre(self):
        return(self.longeur + self.largeur )*2

    def air(self):
        return(self.longeur * self.largeur)

    def iscarre(self):
       if  self.longeur==self.largeur:
           return True
       else:
           return False
