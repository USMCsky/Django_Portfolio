age = 55
name = "USMCsky"

print("Hello my name is {} and I am {} years old".format(name, age))

if age > 16:
    print("You are old enough to drive.")
else:
    print("not quite there yet.")

if name == "USMCsky":
    print("time to retire!")


#DEFINE FUNCTIONS
def hello(name = "Chugs", age = 0):
    print("Hello {} you are {} years old".format(name, age))

hello("SKY", 55)

sentence = hello()
print(sentence)

def tripleprint():
    print("world " * 3)

tripleprint()


# LIST IS ARRAY BY ANOTHER NAME
dognames = ["Fido", "Bones", "Sally", "Doji", 42, True]
print(dognames)

dognames.insert(0, "Jane")
print(dognames[0])
print(dognames)
print(len(dognames))
del(dognames[0])
print(dognames)
print(len(dognames))

dognames[0] = "Sam"
print(dognames)

