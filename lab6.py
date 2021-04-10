from threading import Thread, Lock
import random

class team:
    def __init__(self, name, count):
        self.name = name
        self.count = count
    def Add(self, val):
        self.count = self.count + val
    def Kill(self, val):
        self.count = max(self.count - val, 0)

lock = Lock()

def action(we,enemy):
    while(True):
        x = random.randrange(5)
        y = random.randrange(10)
        lock.acquire()
        if (we.count == 0 or enemy == 0):
            break
        print(f"Поток {we.name}: \033[31m●\033[0m Блокировка \n",end="")
        try:
            print(f"Поток {we.name}: У команды {we.name} пополнение. {we.name}: {we.count} (\033[32m+{x}\033[0m) ► {we.count + x} \n",end="")
            we.Add(x)
            if (enemy.count <= y):
                enemy.Kill(y)
                print(f"Поток {we.name}: Команда {we.name} наносит последний удар! {enemy.name}: {enemy.count} (\033[31m-{enemy.count}\033[0m) ► 0 \n",end="")
                break
            print(f"Поток {we.name}: Команда {we.name} атакует. {enemy.name}: {enemy.count} (\033[31m-{x}\033[0m) ► {enemy.count - x} \n",end="")
            enemy.Kill(y)
        finally:
            print(f"Поток {we.name}: \033[32m●\033[0m Снятие блокировки \n",end="")
            lock.release()

def battle(team1, team2):
    print(f" Число бойцов команды {team1.name}: {team1.count}. Число бойцов команды {team2.name}: {team2.count}")
    print(f" ▄▀▄▀▄▀ Битва началась! ▄▀▄▀▄▀\n")
    thread1 = Thread(target=action, args=(team1, team2), name=team1.name)
    thread2 = Thread(target=action, args=(team2, team1), name=team2.name)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    return team1.name if team2.count == 0 else team2.name

if __name__ == '__main__':
    red = team("\033[31mRED\033[0m",1000)
    blue = team("\033[34mBLUE\033[0m",1000)
    winer = battle(red, blue)
    print(f"\n ▄▀▄▀▄▀ Команда {winer} победила! ▄▀▄▀▄▀\n")

