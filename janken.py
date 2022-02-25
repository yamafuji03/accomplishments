import random


while(True):
    select = int(input("何出す？1:グー 2:チョキ 3:パー 終わり？:4"))

    list = {1:"グー", 2:"チョキ",3:"パー"}


    print("君は"+str(list[select])+"を出した")

    if select == 4:
        print("では、またまた。")
        break
    computer = random.randrange(1,4)

    print("computerは"+str(list[computer])+"を出した")

    win_or_lose=select-computer


    if win_or_lose ==0 :
        print("引き分け")
    elif win_or_lose ==-1 or win_or_lose==2:
        print("あなたの勝ち")
    else:
        print("負け")


