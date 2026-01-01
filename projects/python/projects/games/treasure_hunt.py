import random

print("🗺️ Welcome to Treasure Hunt!")
print("Find the hidden treasure by choosing directions.")

treasure = random.choice(["north", "south", "east", "west"])

while True:
    move = input("Choose your move (north/south/east/west): ").lower()
    if move == treasure:
        print("🏆 You found the treasure! Congrats!")
        break
    else:
        print("❌ No treasure here. Keep looking!")
