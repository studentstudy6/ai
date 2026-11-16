def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Right"
    else:
        return "Left"

# Environment
rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

for i in range(5):
    status = rooms[location]
    action = vacuum_agent(location, status)

    print("Location:", location)
    print("Status:", status)
    print("Action:", action)

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Right":
        location = "B"
    elif action == "Left":
        location = "A"

print("Final Environment:", rooms)
