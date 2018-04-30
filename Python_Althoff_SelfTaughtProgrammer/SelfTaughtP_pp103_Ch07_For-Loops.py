
# For-loops are used to iterate through an iterable.
iterableName = "iterableContent"
for eachItem in iterableName:
    print(eachItem)

# Iterating through a list.
tvShows = ["Agents", "Grimm", "Supergirl", "Gifted"]
for aShow in tvShows:
    thisShow = aShow.upper()
    print(thisShow)

# Iterating through a tuple.
agents = ("Skye", "Coulson", "May", "Fitz", "Simmons")
for operatives in agents:
    print(operatives)

# Iterating through a dictionary.
mainCharacters = {"Agents":"Coulson", "Gifted":"Struckers", "Grimm":"Nick"}
print(mainCharacters["Agents"])
print(mainCharacters["Gifted"])
print(mainCharacters["Grimm"])

for eachShow in mainCharacters:
    print(eachShow + "1")

# You can use a for-loop to change a mutable iterable.
libertarians = ["Mises", "Rothbard", "Boaz", "Friedman"]
i = 0

for people in libertarians:
    new = libertarians[i]
    new = new.lower()
    libertarians[i] = new
    i += 1

print(libertarians)

# Another way to use a for-loop to change a mutable iterable.
parties = ["Republican", "Democrat", "Libertarian"]

for i, show in enumerate(parties):
    new = parties[i]
    new = new.upper()
    parties[i] = new

print(parties)

# You can use for-loops to move data between mutable iterables.
books = ["Common Sense", "The Law", "The Libertarian Mind"]
courses = ["Coding Dojo", "MIT CIS", "INFO_1005"]
education = []

for item in books:
    item = item.upper()
    education.append(item)

for item in courses:
    item = item.upper()
    education.append(item)

print(education)

