import random
def random_sentence(names, verbs, adverbs):
    name = random.choice(names)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)
    print(f"{name} {verb} {adverb}")

n = (input("Please enter a list of names :"))
names = list(n.split(" "))
v = input("Please enter a list of verbs :")
verbs = list(v.split(" "))
a = input("Please enter a list of adverbs :")
adverbs = list(a.split(" "))
random_sentence(names, verbs, adverbs)