print("--- Pattern 1 ---")
for i in range(1, 5):
    print("*" * i)

print("\n--- Pattern 2 ---")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\n--- Pattern 3 ---")
for i in range(1, 6):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
print("\n--- Pattern 4 ---")
for i in range(1, 6):
    print("5" * i)
print("\n--- Pattern 5 ---")
for i in range(5, 0, -1):
    print("*" * i)