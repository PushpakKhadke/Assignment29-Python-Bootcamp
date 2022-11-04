# Assignment 29

# 1. Write a Python script to print the following status of a file:
'''
a. Whether a file is read only
b. Whether a file is closed or not
c. Which file opening mode is used
d. Name of the file
'''
f = open("myfile.txt", "w")           ### create a file with filename               
f.write("I Love Python Programming")  ### write in a file
f.read()                    ### read a file
f.close()                   ### file is close or not
# 2. Write a Python script to create a new file ‘myfile.txt’ and store user entered text.

f = open("myfile.txt", "w")
f.write("I Love Python Programming")
f.close()

# 3. Write a Python script to read the above created file ‘myfile.txt’ and display content on the console.

f = open("myfile.txt", "r")
print(f.read())


# 4. Write a Python script to store a list of city names in a file ‘cities.txt’

f = open("cities.txt", "w")
f.write("Delhi, Mumbai, Kolkata, Bihar")
f.close()

# 5. Write a Python script to append list of city names in a file ‘cities.txt’

f = open("cities.txt", "a")
f.write("Banglore, Hyderabad")
f.close()

# 6. Write a Python script to search whether a particular city is there in the file ‘cities.txt’ or not

with open(r'cities.txt', 'r') as fp:
    # read all lines using readline()
    lines = fp.readlines()
    for row in lines:
        # check if string present on a current line
        word = 'Hyderabad'
#         print(row.find(word))
        # find() method returns -1 if the value is not found,
        # if found it return 0
        if row.find(word) == 0:
            print('string exists in file')
        
         
# 7. Write a Python script to count the number of Python keywords occurring in a python source file.
# 8. Write a Python script to create a copy of a file.

with open('cities.txt','r') as firstfile, open('second.txt','w') as secondfile:
      
    # read content from first file
    for line in firstfile:
               
             # write content to second file
             secondfile.write(line)
             
# 9. Write a Python script to store book data in a file. Book data is in the form of a dictionary in which book name is the key and price is its value. Use pickle to store
#    data into a file (say bookfile)

import pickle

bookfile = {"Python":500,"DSA":450,"Java":750,"C++":450}
f = open('bookfile.txt', 'ab')
pickle.dump(bookfile,f)
f.close()

# 10. Write a Python script to extract book data from a bookfile using pickle. Also print extracted book data.

import pickle
f = open('bookfile.txt', 'rb')
s = pickle.load(f)
for key in s:
    print(key,'---',s[key])
f.close()
