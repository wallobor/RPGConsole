import random
import os
import sys

def conClear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wConvert(percentage):
    percentage_ = 100 - percentage
    return wRand([1, 0], [percentage, percentage_])

def wRand(inpt, weight):
    arrRand = []
    for num in range(len(inpt)):
        for wgh in range(max(1, weight[num])):  
            arrRand.append(inpt[num])
    return arrRand[dRandom(1, len(arrRand))]

def Random(x, y):
  return random.randint(x,y - 1)

def dRandom(x,y):
  return random.randint(x,y)

def consoleCMD():
  cmd = input("Type /help to open help menu\n")
  if cmd == "/help":
    help()
  elif cmd == "/exit":
    exit()
  elif cmd == "/explore":
    explore()
  elif cmd == "/stats":
    stats()
  elif cmd == "/shop":
    shop()
  elif cmd == "/credits":
    credits()
  else:
    print()
    conClear()
    print("Invalid command")

    print()
    consoleCMD()
    
def credits():
    conClear()
    print(">-------------------------------------------<")
    print()
    print(" ---< RPGConsole v1 >---")
    print(" Code by Syauqi Aufa")
    print(" Created per 30 June 2024")
    
    print()
    print(" A Game about adventure in console form,")
    print(" Short and endless RPG themed console game,")
    print(" Fight monsters, gather coins, and survive,")
    print(" Unique items, stats, and monsters to find,")
    print(" All in one python script. Play it now!")
    
    print()
    print(">-------------------------------------------<")
    
    consoleCMD()

def shop():
  global coins, hp
  conClear()

  PLACE = ["Elderian", "Ancient", "Forgotten", "Lost", "The", "Hidden"]
  SHOP = ["Grotto", "Valley", "Town", "Village", "Aquatic", "Mountain"]

  shopName = f"{PLACE[Random(1, len(PLACE))]} {SHOP[Random(1, len(SHOP))]}"

  print(">-------------------------------------------<")
  print()
  print(f"--< Welcome to {shopName}'s shop >--")

  print()
  print(f" Your Purse : {coins}")
  print(" Select Items To Buy:")
  print(" 1 - Small Healing Potion (+100 HP)  [ 350 Coins ]")
  print(" 2 - Large Healing Potion (+500 HP)  [ 1000 Coins ]")
  print(" 3 - Giga Healing Potion (+2000 HP)  [ 2500 Coins ]")
  print(" 4 - Re-Roll Weapon  [ 2100 Coins ]")
  print(" 5 - Exit Shop")

  print()
  print(">-------------------------------------------<")

  shopItem = int(input())
  if shopItem == 1:
    conClear()
    if coins < 350:
      print(">-------------------------------------------<")
      print("You don't have enough coins")
      print(">-------------------------------------------<")
      consoleCMD()
    else:
      hp += 100
      coins -= 350

      print(">-------------------------------------------<")
      print("You bought a small healing potion for 350 coins")
      print(f"Your HP : {hp} (+100)")
      print(">-------------------------------------------<")
      consoleCMD()
  elif shopItem == 2:
    conClear()
    if coins < 1000:
      print(">-------------------------------------------<")
      print("You don't have enough coins")
      print(">-------------------------------------------<")
      consoleCMD()
    else:
      hp += 500
      coins -= 1000

      print(">-------------------------------------------<")
      print("You bought a large healing potion for 1000 coins")
      print(f"Your HP : {hp} (+500)")
      print(">-------------------------------------------<")
      consoleCMD()
  elif shopItem == 3:
    conClear()
    if coins < 2500:
      print(">-------------------------------------------<")
      print("You don't have enough coins")
      print(">-------------------------------------------<")
      consoleCMD()
    else:
      hp += 2000
      coins -= 2500

      print(">-------------------------------------------<")
      print("You bought a huge healing potion for 2500 coins")
      print(f"Your HP : {hp} (+2000)")
      print(">-------------------------------------------<")
      consoleCMD()
  elif shopItem == 4:
    conClear()
    if coins < 2100:
      print(">-------------------------------------------<")
      print("You don't have enough coins")
      print(">-------------------------------------------<")
      consoleCMD()
    else:
      coins -= 2100
      reRoll()
  elif shopItem == 5:
    conClear()
    consoleCMD()
  else:
    print()
    print("Invalid command")
    shop()

def startRPGC():
  conClear()
  print(">-------------------------------------------<")
  print("<< PRESS ENTER TO START YOUR JOURNEY >>")

  print(">-------------------------------------------<")
  input()

  startWeapon()
  consoleCMD()

def help():
  conClear()
  print(">-------------------------------------------<")
  print()
  print("--< Help Menu >--")
  print(" /exit - Stop your journey")
  print(" /help - Open this menu")
  print(" /explore - Explore the world")
  print(" /stats - Shows your stats")
  print(" /shop - Open shop menu")
  print(" /credits - Show game credits")
  
  print()
  print()
  print("        ! NOTICE !")
  print("  This Project is still WIP")
  print("  Game can crash anytime due to")
  print("  Bugs and incompleted code.")

  print()
  print(">-------------------------------------------<")
  consoleCMD()

def explore():
  global mnstr
  conClear()

  place = wConvert(90)
  if place == 1:
    mnstr = monster()
    attack()
  else:
    camp()

def camp():
  global hp, coins
  hp = round(hp)

  conClear()
  print(">-------------------------------------------<")

  print("You found a camp!")
  print("Choose your action: ")
  print(" 1 - Raid")
  print(" 2 - Heal")
  campAct = input()
  if campAct == "1":
    addRaid = dRandom(1500, 4000)
    coins += addRaid

    print()
    print(f" You raid the camp and got +{addRaid} coins!")
    print(">-------------------------------------------<")
    consoleCMD()

  elif campAct == "2":
    raidHP = round(hp / 1.5)
    hp += raidHP

    print()
    print(f" You found healing potion and heals +{raidHP}")
    print(f" Your HP : {hp}")
    print(">-------------------------------------------<")
    consoleCMD()

  print(">-------------------------------------------<")

def attack():
  global dmg, hp, dmg_e, hp_e, spd, spd_e, td, tdc, mnstr, cc, cd, coins, defense
  dmg = round(dmg)
  hp = round(hp)
  dmg_e = round(dmg_e)
  hp_e = round(hp_e)
  td = round(td)
  tdc = round(tdc)
  spd = round(spd)
  spd_e = round(spd_e)
  cc = round(cc)
  cd = round(cd)

  if hp_e > 0 and hp > 0:

    print(">-------------------------------------------<")
    print()
    print(f"--< {mnstr} >--")
    print(f" Monster HP : {hp_e}")
    print(f" Monster Damage : {dmg_e}")
    print(f" Monster Speed : {spd_e}")

    print()
    print(f" Your HP : {hp}")
    print(f" Total Damage : {td}")
    print(f" Speed : {spd}")

    print()
    print(">-------------------------------------------<")

    print("Choose your attack :")
    print(" 1 - Attack")
    print(f" 2 - Parry (75% success rate, returns 1/3 monster's damage)")
    print(" 3 - Run")


    atk = input()
    if atk == "1":

      dmgR = round(dmg_e - (dmg_e * defense / 100))

      conClear()
      if wConvert(cc) == 1:
        print(">-------------------------------------------<")
        print(f" You attacked the monster for -{tdc}! [CRITICAL]")
        print(f" Monster attacked you for -{dmgR}!")
        hp_e -= tdc
        hp -= dmg_e
        attack()

      else:
        print(">-------------------------------------------<")
        print(f" You attacked the monster for -{td}!")
        print(f" Monster attacked you for -{dmgR}!")
        hp_e -= td
        hp -= dmg_e
        attack()

    elif atk == "2":
      conClear()
      print()

      if not dRandom(1,4) == 1:
        pry = round(dmg_e / 3)
        hp_e -= pry

        print(">-------------------------------------------<")
        print(" You parried the attack")
        print(f" You returned -{pry} damage to monster")
      else:
        hp -= dmg_e

        print(" You failed to parry the attack")
        print(f" Monster attacked you for -{dmg_e}")
      attack()

    elif atk == "3":
      conClear()
      print(">-------------------------------------------<")
      runDmg = round((dmg_e / 1.5) - spd + spd_e)
      hp -= runDmg
      lost = dRandom(50,500)
      coins -= lost

      print()
      print(f" Monster hit you for -{runDmg} but you managed to ran away.")
      print(f" You lost -{lost} coins while running.")

      print()
      print(">-------------------------------------------<")
      consoleCMD()

    else:
      print()
      print("Invalid command")
      conClear()
      attack()

  elif hp_e <= 0 and hp > 0:
    reward = dRandom(500,800)
    coins += reward

    print()
    print(" You defeated the monster!")
    print(f" Purse: {coins} (+{reward})")

    if wConvert(5) == 1:
        healRWD = dRandom(100,200)
        hp =+ healRWD
        print(" You got healed for +{healRWD} HP")

    print(">-------------------------------------------<")

    consoleCMD()

  elif hp <= 0 and hp_e > 0:
    conClear()
    print(">-------------------------------------------<")

    print()
    print(" You died!")
    print(f" Coins gathered : {coins}")

    print()
    print(">-------------------------------------------<")

    restart = input("Press Enter to restart\n")
    startRPGC()

def exit():
  conClear()
  print()
  print('Exiting the game..')

  sys.exit()

def stats():
  conClear()
  print(">-------------------------------------------<")

  print()
  print("--< PURSE >--")
  print(f" Coins: {coins}")

  print()
  print("--< STATS >--")
  print(f" Damage : {dmg}")
  print(f" Strength : {strength}")
  print(f" Critical Damage : {cd}%")
  print(f" Critical Chance : {cc}%")
  print(f" Total Damage : {td}")
  print(f" Total Damage (Crit) : {tdc}")

  print()
  print(f" HP : {hp}")
  print(f" Damage Reduction : {defense}%")
  print(f" Speed : {spd}")

  print()
  print(">-------------------------------------------<")
  consoleCMD()

def monster():
  global dmg_e, hp_e, spd_e

  NAME = ["Flesh Eater", "Skin Ripper", "Undead", "Skeleton", "Zombie", "Scorpio", "Watcher", "Wall Crawler"]
  TYPE = ["The", "Legendary", "Supreme", "Gigantic", "Army Of", "Creepy", "Nightmare", "Insane", "Weak", "Tough"]

  dmg_e = Random(100, 500)
  hp_e = Random(700,1500)
  spd_e = Random(5,90)

  return f"{TYPE[Random(1, len(TYPE))]} {NAME[Random(1, len(NAME))]}"

def reRoll():
  global dmg, strength, cd, cc, td, tdc, hp, defense, spd, coins
  conClear()

  print(">-------------------------------------------<")
  print()
  print('You rerolled your weapon and got :')

  NAME = ["Crystal", "Expoding", "Wavy", "Destroyer", "Electrized", "Devourer"]
  TYPE = ["Sword", "Greatsword", "Bow", "Longbow", "Shortbow", "Longsword", "Dagger", "Knives", "Spear", "Whip"]
  ATTRIBUTE = ["Shiny", "The", "Rough", "Legendary", "Epic", "Broken", "Mythical", "Sharp", "Dull", "Glossy", "Strong", "Dual"]

  dmg = dRandom(1, 500)
  strength = dRandom(1,500)
  cd = dRandom(1,500)
  cc = dRandom(1,100)

  hp = dRandom(2400,6500)
  defense = dRandom(1,50)
  spd = dRandom(5,90)

  coins = 100

  result = f"{ATTRIBUTE[Random(1, len(ATTRIBUTE))]} {NAME[Random(1, len(NAME))]} {TYPE[Random(1, len(TYPE))]}"

  statDMG = f"Damage : {dmg}"
  statSTR = f"Strength : {strength}"
  statCD = f"Critical Damage : {cd}%"
  statCC = f"Critical Chance : {cc}%"
  td = dmg + (strength / 5)
  tdc = td + (dmg * cd / 100)
  statTD = f"Total Damage : {round(td)}"
  statTDC = f"Total Damage (Crit) : {round(tdc)}"
  statHP = f"HP : {hp}"
  statDEF = f"Damage Reduction : {defense}%"
  statSPD = f"Speed : {spd}"

  n = "\n"
  nn = "\n\n"

  print(result, nn, statDMG, n, statSTR, n, statCD, n, statCC, nn, statTD, n, statTDC, nn, statHP, n, statDEF, n, statSPD)
  print(f"{n} Your Coins: {coins}")

  print()
  print(">-------------------------------------------<")
  consoleCMD()

def startWeapon():
  global dmg, strength, cd, cc, td, tdc, hp, defense, spd, coins
  conClear()

  print(">-------------------------------------------<")
  print()
  print('You started your journey and given a weapon :')

  NAME = ["Crystal", "Expoding", "Wavy", "Destroyer", "Electrized", "Devourer"]
  TYPE = ["Sword", "Greatsword", "Bow", "Longbow", "Shortbow", "Longsword", "Dagger", "Knives", "Spear", "Whip"]
  ATTRIBUTE = ["Shiny", "The", "Rough", "Legendary", "Epic", "Broken", "Mythical", "Sharp", "Dull", "Glossy", "Strong", "Dual"]

  dmg = dRandom(1, 500)
  strength = dRandom(1,500)
  cd = dRandom(1,500)
  cc = dRandom(1,100)

  hp = dRandom(2400,6500)
  defense = dRandom(1,50)
  spd = dRandom(5,90)

  coins = 100

  result = f"{ATTRIBUTE[Random(1, len(ATTRIBUTE))]} {NAME[Random(1, len(NAME))]} {TYPE[Random(1, len(TYPE))]}"

  statDMG = f"Damage : {dmg}"
  statSTR = f"Strength : {strength}"
  statCD = f"Critical Damage : {cd}%"
  statCC = f"Critical Chance : {cc}%"
  td = dmg + (strength / 5)
  tdc = td + (dmg * cd / 100)
  statTD = f"Total Damage : {round(td)}"
  statTDC = f"Total Damage (Crit) : {round(tdc)}"
  statHP = f"HP : {hp}"
  statDEF = f"Damage Reduction : {defense}%"
  statSPD = f"Speed : {spd}"

  n = "\n"
  nn = "\n\n"

  print(result, nn, statDMG, n, statSTR, n, statCD, n, statCC, nn, statTD, n, statTDC, nn, statHP, n, statDEF, n, statSPD)
  print(f"{n} Your Coins: {coins}")

  print()
  print(">-------------------------------------------<")

startRPGC()