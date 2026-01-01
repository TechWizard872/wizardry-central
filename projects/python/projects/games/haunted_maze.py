import random

print("👻 Welcome to the Haunted Maze!")
print("Escape by choosing directions: N, S, E, W")

exit_path = random.choice(["N", "S", "E", "W"])

while True:
    move = input("Move (N/S/E/W): ").upper()
    if move == exit_path:
        print("🎉 You escaped the haunted maze!")
        break
    else:
        print("💀 Dead end! Try another direction.")
