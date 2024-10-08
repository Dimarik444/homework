import random
key_pas = []
def decoding():
    var = random.choice(list(range(3, 21)))
    for i in range(var):
        a = i + 1
        for j in range(var):
            b = j + 1
            if var % (a + b) == 0 and a < b:
                key_pas.append(a)
                key_pas.append(b)
            continue
    print(var)
    print(*key_pas)
    return key_pas
decoding()