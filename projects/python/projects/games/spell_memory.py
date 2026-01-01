import random
import time

print("🧠 Welcome to Spell Memory!")
spells = ["fire", "ice", "heal", "lightning", "shield"]

sequence = random.sample(spells, 3)
print("Memorize this spell sequence:")
print(sequence)
time.sleep(3)
print("\n" * 50)

guess = input("Enter the sequence separated by spaces: ").lower().split()

if guess == sequence:
    print("✨ Perfect! You remembered the sequence.")
else:
    print(f"❌ Wrong! The correct sequence was {sequence}")
