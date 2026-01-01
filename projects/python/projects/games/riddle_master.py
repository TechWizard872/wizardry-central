print("🧩 Welcome to Riddle Master!")
riddles = {
    "I speak without a mouth and hear without ears. What am I?": "echo",
    "What has keys but can't open locks?": "piano",
    "What can travel around the world while staying in a corner?": "stamp"
}

score = 0
for question, answer in riddles.items():
    guess = input(question + " ").lower()
    if guess == answer:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The answer was {answer}")

print(f"🏆 You solved {score}/{len(riddles)} riddles!")
