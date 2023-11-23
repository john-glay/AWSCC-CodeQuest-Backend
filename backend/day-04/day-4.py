print("\n--- OPTIONS ---")
print("  [1] Rock")
print("  [2] Paper")
print("  [3] Scissors\n")

p1 = int(input("PLAYER #1: "))
p2 = int(input("PLAYER #2: "))

if (p1 >= 1 and p1 <= 3) and (p2 >= 1 and p2 <= 3): 

    if not p1 == p2:
        if (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or (p1 == 3 and p2 == 2):
            print("\nPlayer #1 Wins!\n")
        else:
            print("\nPlayer #2 Wins!\n")
    else:
        print("\nIt's a draw!\n")

else:
    print("\nInputs must be 1, 2, or 3 only\n")
