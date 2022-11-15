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

print(f"Since {not_coming} can't make it, I'm inviting {new_person}")
guests.append(f"{new_person}")
print(f"{guests[0].title()}{invite}")
print(f"{guests[1].title()}{invite}")
print(f"{guests[2].title()}{invite}")
print(f"{guests[3].title()}{invite}")
print(f"{guests[4].title()}{invite}")

print(f"I found a bigger dinner table")
guests.insert(0, "Judy")
guests.insert(4, "Michael")
guests.append("Kaila")

print(f"{guests[0].title()}{invite}")
print(f"{guests[1].title()}{invite}")
print(f"{guests[2].title()}{invite}")
print(f"{guests[3].title()}{invite}")
print(f"{guests[4].title()}{invite}")
print(f"{guests[5].title()}{invite}")
print(f"{guests[6].title()}{invite}")
print(f"{guests[7].title()}{invite}")

print("Turns out I my new table won't arrive in time for the party. I'll have to make my guest list smaller. Sorry!")

removed_guest = guests.pop()
apology_message = f"{removed_guest.title()}, I'm sorry that I have to uninvite you from my party"
print(apology_message)
print(guests)

removed_guest = guests.pop()
apology_message = f"{removed_guest.title()}, I'm sorry that I have to uninvite you from my party"
print(apology_message)
print(guests)

removed_guest = guests.pop()
apology_message = f"{removed_guest.title()}, I'm sorry that I have to uninvite you from my party"
print(apology_message)
print(guests)

removed_guest = guests.pop()
apology_message = f"{removed_guest.title()}, I'm sorry that I have to uninvite you from my party"
print(apology_message)
print(guests)

removed_guest = guests.pop()
apology_message = f"{removed_guest.title()}, I'm sorry that I have to uninvite you from my party"
print(apology_message)
print(guests)

removed_guest = guests.pop()
apology_message = f"{removed_guest.title()}, I'm sorry that I have to uninvite you from my party"
print(apology_message)
print(guests)

print(f"{guests[0].title()}{invite}")
print(f"{guests[1].title()}{invite}")

del guests[0]
print(guests)
del guests[0]
print(guests)