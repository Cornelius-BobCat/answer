from itertools import permutations

def b(a):
    return list(set("".join(perm) for perm in permutations(a)))

a = "abcd"
resultat = b(a)
print("Tous les anagrammes possibles :", resultat)
