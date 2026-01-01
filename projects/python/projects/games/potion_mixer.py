import random

print("🧪 Welcome to Potion Mixer!")
ingredients = ["eye of newt", "dragon scale", "unicorn hair", "phoenix feather"]
potion = random.sample(ingredients, 2)

print("Mix two ingredients to guess the secret potion!")

attempts = 0
while True:
    guess1 = input("First ingredient: ").lower()
    guess2 = input("Second ingredient: ").lower()
    attempts += 1
    if set([guess1, guess2]) == set(potion):
        print(f"✨ Correct! Potion created in {attempts} tries!")
        break
    else:
        print("❌ Wrong combination! Try again.")
