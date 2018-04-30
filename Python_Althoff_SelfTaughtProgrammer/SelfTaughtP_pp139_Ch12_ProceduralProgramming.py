
# Procedural programming is sequential: "Do this, then that".

x = 4
y = 5
z = 6
xyz = x*y*z
print(xyz)

# When you program procedurally, you store data in global variables and
# manipulate it with functions.

rock = []
country = []

def collect_songs():
    song = "Enter a song: "
    ask = "Type r or c, or q to quit: "

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "r":
            rk = input(song)
            rock.append(rk)

        elif genre == "c":
            cy = input(song)
            country.append(cy)

        else:
            print("Invalid Entry")

    print(rock)
    print(country)

collect_songs()
