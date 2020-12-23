#ghost game
from random import randint #библиотека randint
print("Ghost Game") #объявляем начало игры
feeling_brave = True  #если станет False,игра кончится
score = 0 #очки игрока
while feeling_brave:  #цикл
    ghost_door = randint(1,3) #randint генерирует число от 1 до 3-ех
    print ("Three doors ahead...")
    print ("A ghost behind one.")
    print ("which do you open?")
    door_num = int(input("1,2 or 3")) #выбор двери
    if door_num == ghost_door: #проверяем на совпадение ghost_door и door_num
        print("GHOST!")
        feeling_brave = False #конец игры
    else:
        print("No ghost!")
        print("You enter the next room>")
        score = score + 1 #добавляем 1 очко
        print(score) #очки игрока