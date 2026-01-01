import random

print("🐉 Welcome to Dragon Fight!")
player_health = 20
dragon_health = 25

while player_health > 0 and dragon_health > 0:
    attack = input("Attack with sword or magic? ").lower()
    if attack == "sword":
        damage = random.randint(2,5)
        dragon_health -= damage
        print(f"⚔️ You slash the dragon! Dragon loses {damage} health.")
    elif attack == "magic":
        damage = random.randint(3,6)
        dragon_health -= damage
        print(f"✨ Magic hits! Dragon loses {damage} health.")
    else:
        print("❌ Invalid move!")
    if dragon_health > 0:
        dragon_attack = random.randint(1,5)
        player_health -= dragon_attack
        print(f"🐲 Dragon attacks! You lose {dragon_attack} health.")

if player_health > 0:
    print("🎉 You defeated the dragon!")
else:
    print("💀 You were slain by the dragon...")
