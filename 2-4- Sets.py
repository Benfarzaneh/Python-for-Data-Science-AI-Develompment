# Convert the list ['rap','house','electronic music', 'rap'] to a set:
set(['rap','house','electronic music','rap'])

# Consider the list A = [1, 2, 2, 1] and set B = set([1, 2, 2, 1]), does sum(A) == sum(B)?
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))

# Create a new set album_set3 that is the union of album_set1 and album_set2:
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
Un = album_set1.union(album_set2)
print(Un)

# Find out if album_set1 is a subset of album_set3:
set(album_set1).issuperset(album_set2)   
