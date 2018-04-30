# Use syntax "new_iterable_name[start_index:end_index]" to "slice" out a
# section of an iterable into a new iterable.
aiel_oath = """
Till shade is gone, till water is gone,
into the shadow with teeth bared,
screaming defiance with the last breath,
To spit in Sightblinder's eye
on the last day."""

aiel_quote = aiel_oath[116:145]
print(aiel_quote)

# Leaving one end of the "slice" empty means we're defaulting to the start/end.
print(aiel_oath[:39])
print(aiel_oath[40:])
print(aiel_oath[:])




