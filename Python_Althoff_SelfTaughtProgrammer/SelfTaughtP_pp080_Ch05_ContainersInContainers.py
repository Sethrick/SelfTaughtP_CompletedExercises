
# You can store containers in other containers, such as a list inside a list.
lists = []
rap = ["Kanye West",
       "Jay Z",
       "Eminem",
       "Nas"]

rock = ["Bob Dylan",
        "The Beatles",
        "Led Zeppelin",]

djs = ["Zeds Dead",
       "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)

print(lists)

# You can access the sub-lists using their corresponding indices.
rock = lists[1]
print(rock)

# You can make changes to sub-lists the same way.
rap = lists[0]
rap.append("Kendrick Lamar")
print(lists)

# You can also store a tuple inside a list...
locations = []

la = (34.0522, 188.2437)
chicago = (41.8781, 87.6298)

locations.append(la)
locations.append(chicago)

print(locations)

# Or a list inside a tuple...
eights = ["Edgar Allen Poe",
          "Charles Dickens"]

nines = ["Hemingway",
         "Fitzgerald",
         "Orwell"]

authors = (eights, nines)
print(authors)

# Or a dictionary inside either...
bday = {"Hemingway": "7.21.1899",
        "Fitzgerald": "9.24.1896"}

bday["Hendrickson"] = "7.15.1998" # note syntax for appending to dictionary.

my_list = [bday]
print(my_list)
my_tuple = (bday,)
print(my_tuple)

# A list, tuple, or dictionary can also be a value in a dictionary:
ny = {"location": (40.7128, 74.0059),
      "celebrities": ["W. Allen", "Jay Z", "K. Bacon"],
      "facts": {"state": "NY", "country": "America"}
      }

print(ny)

# Again, we can access the individual items as follows:
my_facts = ny["facts"]
my_facts["planet"] = "Earth" # Again, appending to dictionary.
print(my_facts)
print(ny)


