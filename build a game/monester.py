player = {
    "name": "gemy",
    "attack": 18,
    "heal": 30,
    "health": 100
}
monester = {
    "name": "zombi",
    "attack": 30,
    "health": 100
}


print("please select action")
print("1) attack")
print("2) heal")

action = int(input())

if action == 1:
    print("attacking")
    print(monester["health"])
    monester["health"] = monester["health"] - player["attack"]
    print(monester["health"])
elif action == 2:
    print("healthing")
