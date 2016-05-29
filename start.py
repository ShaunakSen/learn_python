name = "Shona"

if name is "Mini":
    print("Hi little mini")
elif name is "Shona":
    print("hi budhhu")

foods = ["bacon", "tuna", "sausages", "veggies", "paneer"]
for f in foods:
    print(f)
    print(len(f))

for f in foods[:2]:
    print(f)
    print(len(f))

for x in range(5, 12):
    print(x)

# 3rd argument specifies the increment
for x in range(5, 40, 5):
    print(x)


def mini():
    print("Running function in python")


mini()

def getGender(sex="unknown"):
    if sex is 'm':
        sex = "Male"
    elif sex is 'f':
        sex = "Female"
    print(sex)


getGender('m')
getGender()
