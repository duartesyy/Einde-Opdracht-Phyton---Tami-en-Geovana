monster_health = 150
player_damage = 25
attack_count = 0

while monster_health > 0:
    print(f"Monster Health: {monster_health} || You dealt {player_damage} damage!")
    monster_health = monster_health - player_damage
    attack_count += 1  
else:
    monster_health = 0
    print(f"Monster Health: {monster_health}!")
    print(f"Monster defeated!")
    print(f"Attack Count: {attack_count}")

    monsters_health = [157, 47, 160]
    attack_count = 0
    monsters_count = len(monsters_health)

    for monsters_health in monsters_health:
        while monsters_health > 0:
            print(f"Monster Health: {monsters_health} ||  You dealt {player_damage} damage!")
            monsters_health -= player_damage
            attack_count += 1
        if monsters_health <= 0:
            monsters_count -= 1
            print(f"There are {monsters_count} monsters left.")
            print(f"Monster defeated!")
            print(f"Attack Count: {attack_count}")
        elif monsters_count == 0:
            print("All monsters are defeated!")
