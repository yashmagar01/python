# 1) Write a Python script to sort (ascending and descending) a dictionary by value

interest = {
    "Food" : "Poha",
    "Music" : "Bollywood",
    "Subject" : "UID",
    "Movie" : "No Way Home",
    "Singer" : "Arijit Singh"
}

print("Ascending Order: ")
print(sorted(interest.items()))
print("Descending Order: ")
print(sorted((interest.items(), reversed = True)
             ))