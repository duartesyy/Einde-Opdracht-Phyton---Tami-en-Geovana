player_class = input("Warrior, Mage, Archer, Rogue, Cleric, Druid. Choose your class:")

match player_class.lower():
    case "warrior":
        health = 150
        damage = 20
    case "mage":
        health = 80
        damage = 35
    case "archer":
        health = 100
        damage = 25
    case "rogue":
        health = 90
        damage = 30
    case "cleric":
        health = 100
        damage = 15
    case "druid":
        health = 70
        damage = 30
    case _:
        print("Unknown class.")

print(f"Your class is: {player_class}")
print(f"You have {health} hit points and your damage is {damage}. ")