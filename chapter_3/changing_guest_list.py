guests = ["pochita", "angela", "kelsey", "jacqui", "uma"]
invite = ", you're invited to my dinner!"
print(f"{guests[0].title()}{invite}")
print(f"{guests[1].title()}{invite}")
print(f"{guests[2].title()}{invite}")
print(f"{guests[3].title()}{invite}")
print(f"{guests[4].title()}{invite}")

print(f"uh oh. {guests[4]} can't make it")

not_coming = guests.pop()
new_person = "Amanda"

print(f"Since {not_coming} can't make it, I'm inviiting {new_person}")
guests.append(f"{new_person}")
print(f"{guests[0].title()}{invite}")
print(f"{guests[1].title()}{invite}")
print(f"{guests[2].title()}{invite}")
print(f"{guests[3].title()}{invite}")
print(f"{guests[4].title()}{invite}")