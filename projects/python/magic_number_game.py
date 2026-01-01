import random

print("🪄 Welcome to the Magic Number Game! 🪄")
print("Guess the number I'm thinking of between 1 and 20.")

magic_number = random.randint(1, 20)
attempts = 0

while True:
    guess = input("Your guess: ")
    attempts += 1
    
    if not guess.isdigit():
        print("⚠️ Please enter a number!")
        continue
    
    guess = int(guess)
    
    if guess < magic_number:
        print("⬆️ Too low, try again!")
    elif guess > magic_number:
        print("⬇️ Too high, try again!")
    else:
        print(f"✨ Congrats! You guessed the magic number {magic_number} in {attempts} tries!")
        break
