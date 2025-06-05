contacts = [
    {
            "name": "Marťas",
    "email": "m@email.com",
    "phone": "888 888 888"
    },
    {
            "name": "Bartoloměj",
    "email": "b@email.com",
    "phone": "111 888 222"
    }
]

# vypsat cely 1. kontakt 
print(contacts[0])
print(contacts[1])

#vypsat hodnotu klíče "name" v položce na indexu 0 
print(contacts[0]["name"])

# přidáme kontakt
name = "Martin"
email = "mar@mail.com"
phone = ""
contact = {
    "name": name,
    "email": email,
    "phone": phone
}

# přidat contact do contacts
contacts.append(contact)

print(contacts)