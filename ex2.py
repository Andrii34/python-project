from turtle import*


player = Turtle()

player.health = 100
player.mp = 30
player.atack = 25
player.name= "Gojo"

boss = Turtle()

boss.health = 100
boss.mp = 100
boss.atack = 100
boss.name = "sukuna"

def fight():
    while player.health>0 and boss.health>0:
        if player.mp>9:
           boss.health -= player.atack
           player.mp -=10

           print(f"{player.name} hit the boss.helth level:{boss.health }") 

        else:
            player.mp+=5
            print(f"{player.name} skips the atack.restocks mp.mp level:{player.mp}")
        
        
        
        
        if boss.mp>9:
           player.health -= boss.atack
           boss.mp -=10

           print(f"{boss.name} hit the {player.name}. health level:{player.health}")
        
        else:
            boss.mp+=5
            print(f"{boss.name} skips the atack.restocks mp.mp level:{boss.mp}")


    if player.health>0:

        print(f"{player.name} wins")

    else:
        print(f"{boss.name} wins")    
    

fight()