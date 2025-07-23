import random

# Step 1: Ask user for their name
name = input("Welcome agent. What's your real name? ")

# Step 3 & 4: Lists of adjectives and animals
adjectives = ['Sneaky', 'Invisible', 'Swift', 'Shadowy', 'Silent', 'Clever']
animals = ['Otter', 'Panther', 'Falcon', 'Fox', 'Raccoon', 'Python']

# Step 5: Generate codename
codename = f"{random.choice(adjectives)} {random.choice(animals)}"

# Step 6: Generate lucky number
lucky_number = random.randint(1, 99)

# Step 7: Final spy message
print(f"\n🕵️‍♂️ Welcome, Agent {name}.")
print(f"Your codename is: **{codename}**")
print(f"Your lucky number is: **{lucky_number}**")
