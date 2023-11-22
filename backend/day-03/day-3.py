print("\n--OPTIONS--")
print("  [1] Yes")
print("  [0] No")

print("\n1.) Man Asking for Shelter")
q1 = int(input("Please input your response: "))

if q1 == 1:
    print("\n2.) Police arrived & Asked whether thief is inside")
    q2 = int(input("Please input your response: "))

    if q2 == 1:
        print("\nWIN\n")
    else:
        print("\nGame Over\n")

elif q1 == 0:
    print("\n2.) He attacked on you. Will you knock him down")
    q3 = int(input("Please input your response: ")) 

    if q3 == 1:
        print("\nWIN\n")
    else:
        print("\nGame Over\n")
        
else:
    print("\nGame Over\n")