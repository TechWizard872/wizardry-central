print("🔮 Welcome to Guess the Spell!")
word = "abracadabra"
display = ["_" for _ in word]
attempts = 6

while attempts > 0 and "_" in display:
    print(" ".join(display))
    guess = input("Guess a letter: ").lower()
    if guess in word:
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = guess
        print("✅ Good guess!")
    else:
        attempts -= 1
        print(f"❌ Wrong! {attempts} attempts left.")

if "_" not in display:
    print("🎉 You guessed the spell!")
else:
    print(f"💀 You failed. The spell was {word}")
