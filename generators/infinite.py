def infinite_chai():
    count = 1
    while True:
        yield f" infinite {count} of refills"
        count += 1

stall = infinite_chai()
user1 = infinite_chai()

for _ in range(5): 
    print(next(stall))

for _ in range(3):
    print(next(user1))