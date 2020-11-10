import random
from object_oriented_programming.cards import Students

x = random.random()
print(x)


x = random.randint(1, 10)
print(x)
discount = (5000 * x)/100
# print(disc)

x = random.randrange(1, 10)
print(x)

names = ["dayanand", "aditya", "sreenivas", "honagoud"]
last_names = ["jadhav", "bagali", "gosavi"]
domains = ["gmail", "yahoo", "outlook"]


print("*********************")
student_list = []
for _ in range(1,10):
    email = f"{random.choice(names)}.{random.choice(last_names)}@{random.choice(domains)}.com"
    s = Students(random.choice(names), random.choice(last_names), email=email)
    student_list.append(s)
    print(s)

print(student_list)
print("*********************")




print(f"{random.choice(names)}.{random.choice(last_names)}@{random.choice(domains)}.com")
print(f"{random.choice(names)}.{random.choice(last_names)}@{random.choice(domains)}.com")
print(f"{random.choice(names)}.{random.choice(last_names)}@{random.choice(domains)}.com")
print(f"{random.choice(names)}.{random.choice(last_names)}@{random.choice(domains)}.com")
print(f"{random.choice(names)}.{random.choice(last_names)}@{random.choice(domains)}.com")


cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13,1,2,3,4,5,6,7,8,9,10,11,12,13]
random.shuffle(cards)
print(cards)
random.shuffle(names)
print(names)

card_set1 = random.choices(cards, k=5)
card_set2 = random.choices(cards, k=6)
card_set3 = random.choices(cards, k=13)
card_set4 = random.choices(cards, k=13)
print(card_set1)
print(card_set2)
print(card_set3)
print(card_set4)



x = random.uniform(1,10)
print(x)
discount = (1000*x) /100
print(discount)

print("***************************************************")
random.seed(10)
y = random.random()
z = random.random()
print(random.random())
print(random.random())
random.seed(10)
q = random.random()
r = random.random()
print(random.random())
print(random.random())

print(y)
print(z)
print(q)
print(r)


