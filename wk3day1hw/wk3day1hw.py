

#  excercise 1 

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

place = list(filter(lambda x: len(x) > 2, places))

print(place)


# excercise 2 

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

author.sort(key=lambda person: person.split(" ")[-1].lower())
print(author)



# excercise 3

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

places = list(map(lambda place: (place[0], (9/5) * place[1] + 32), places))

print(places)


# excercise 4 

def TookHours(num):
    if num <= 1:
        return num #base case
    return(TookHours(num - 1) + TookHours(num - 2))  


print(TookHours(7))