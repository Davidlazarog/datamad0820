
# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack (self):  
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking


class Viking (Soldier):
    def __init__(self, name, health, strength,):
        super().__init__(health,strength)
        self.name = name
    
    def receiveDamage (self, damage):
        self.damage = damage
        self.health -= damage 
        a = self.health
        if a > 0:
            return(f"{self.name} has received {self.damage} points of damage")
        else: 
            return(f"{self.name} has died in act of combat")
        
    def battleCry(self):
            return "Odin Owns You All!"
 


# Saxon


class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
        self.health = health
        self.strength = strength
    def attack (self):  
        return self.strength
    def receiveDamage (self, damage):
        self.damage = damage
        self.health -= damage
        a = self.health
        if a > 0:
            return(f'A Saxon has received {damage} points of damage')
        else: 
            return(f'A Saxon has died in combat')
         
# War

class War ():

    vikingArmy = []
    saxonArmy = []

    def __init__():
        super().__init__(self)
        self.vikingArmy = vikingArmy
        self.saxonArmy = saxonArmy


    def addViking(self , Viking):
        self.vikingArmy.append(super(),name())

    def addSaxon(self, Saxon):
        self.saxonArmy.append(self.Saxon)
        
    def vikingAttack(self):
        self.Viking.health = self.Saxon.receiveDamage
        if self.Viking.health < 0 :
            vikingArmy.remove(self.Viking)
        return self.Saxon.receiveDamage(self.Viking.strength)

    def saxonAttack(self):
        elf.Saxon.health = self.Viking.receiveDamage
        if self.Saxon.health < 0 :
            saxonArmy.remove(self.Saxon)
        return self.Viking.receiveDamage(self.Saxon.strength)
 
    def showStatus(self):
        if vikingArmy <= 0:
            return "Saxons have fought for their lives and survive another day..."
        elif saxonArmy <= 0:
            return "Vikings have won the war of the century!"
        elif saxonArmy >= 0 and Viking >= 0:
            return "Vikings and Saxons are still in the thick of battle."


    