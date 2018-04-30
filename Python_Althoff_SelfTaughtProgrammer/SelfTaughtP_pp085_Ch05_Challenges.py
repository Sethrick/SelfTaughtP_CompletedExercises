
# 1) Create a list of your favorite musicians.
band_list = ["TSFH", "Evancho", "Thomas", "Piano Guys"]
print(band_list)

# 2) Create a list of tuples, with each tuple containing the longitude
#    and latitude of somewhere you've lived or visited.
Ft_Riley = (39.1101, 96.8100)
Gimli_Peak = (49.7661, 117.6469)
Keystone_CO = (39.5792, 105.9347)
places = [Ft_Riley, Gimli_Peak, Keystone_CO]
print(places)

# 3) Create a dictionary that contains different attributes about you:
#    height, favorite color, favorite author, etc.
my_dict = {"height": "6'1",
           "favorite color": "yes",
           "favorite author": "LordsFire"}

print(my_dict)
my_height = my_dict["height"]
print(my_height)

# 4) Write a program that lets the user ask your height, favorite color,
#    or favorite author, and returns the result from the dictionary you
#    created in the previous challenge.
user_ask = input("Query \"height\", \"favorite color\", or \"favorite author\": ")

result = my_dict[user_ask]   
print(result)

# 5) Create a dictionary mapping your favorite musicians to a list of your
#    favorite songs by them.
music_dir = {"TSFH": "El Dorado",
             "Evancho": "Nella Fantasia",
             "Thomas": "Illumination"}

print(music_dir["Evancho"])

# 6) Lists, tuples, and dictionaries are just a few of the containers
#    built into Python. Research Python sets (a type of container).
#    When would you use a set?
"""
Sets are lists without duplicate entries. They use brackets like lists, but
are instantiated by using the "set()" method. One example of how a set might
be used is on a sign-in roster at a gym. Many people might be regulars, and
enter their name frequently. A set would tell us how many different people
use the gym. For example:
"""
print(set("Jordan Josh Eric Adam Eric Seth Isaac Clara Seth".split()))
