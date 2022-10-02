import requests
import json
import requests

#Exercise 4
def FileWiki(fl,url):
    txt = open(fl,"r")
    # frequent_word = ""
    # frequency = 0 
    words = []
    # Create an empty dictionary
    d = dict()
    # Loop through each line of the file
    for line in txt:
        # splits each line into
        # words and removing spaces
        # and punctuations from the input
        words = line.lower().replace(',','').replace('.','').replace('?','').replace(';','').split(" ")
        
        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

    #find the first most used word in dicionary
    chr1 = max(d, key=d.get)
    print("First most used word:",chr1, "Frequency:" ,d[chr1])
    del d[chr1]
    #find the second most used word in dicionary
    chr2 = max(d, key=d.get)
    print("Second most used word:",chr2, "Frequency:" ,d[chr2])
    txt.close()

    #searching the word chr1chr2 in the source of a web page
    the_word = chr1+chr2
    the_word_as_bytes = str.encode(the_word)
    url_response = requests.get(url)
    data = url_response.content
    count = data.count(the_word_as_bytes)
    print('\nUrl: {}\nContains {} of word: {}'.format(url, count, the_word))

    # Results Set on the  text file
    # First most used word: the Frequency: 6
    # Second most used word: lorem Frequency: 4
    # Results Set on the url
    # Url: https://www.example.org/
    # contains 0 of word: thelorem

#Exercise 7
def nag(lst):
    # Connect to an API
    response_API = requests.get("https://api.opap.gr/draws/v3.0/1100/last-result-and-active")
    # Get the data from API
    data = response_API.text
    # Parse the data into JSON format
    parse_json = json.loads(data)
    # Extract the data and print it
    winning_numbers = parse_json["last"]["winningNumbers"]["list"]
    print("Winning numbers",winning_numbers)
    print("Given numbers for comparison",lst)
    inBetweenNumbers = []
    counter = 0
    for wnum in winning_numbers:
        for num in lst:
            # calculate the difference
            diff = abs(wnum-num)
            if (diff == 1):
                counter = counter + 1   
                inBetweenNumbers.append(num)     
            elif(num == wnum):
                counter = counter + 1   
                inBetweenNumbers.append(num)     
    print("The total numbers that are in between (-1 < x < 1) or equal to the winning numbers:",counter)
    if(counter>0):
        print("The in between (-1 < x < 1) or equal numbers are: ",inBetweenNumbers)

    # Results Set:
    # Winning numbers [77, 17, 41, 66, 1, 36, 6, 12, 15, 71, 5, 24, 53, 45, 70, 38, 76, 25, 48, 80]
    # Given numbers for comparison [3, 59, 56, 23, 30, 43, 25, 76, 64, 19, 57, 12, 49, 15, 70, 67, 39, 28, 50, 33]
    # The total numbers that are in between (-1 < x < 1) or equal to the winning numbers: 12
    # The in between (-1 < x < 1) or equal numbers are:  [76, 67, 12, 15, 70, 23, 25, 70, 39, 76, 25, 49]

#Excercise10
def tril(lst):
    trils=0
    c=0
    listlen=len(lst)
    for i in range(listlen):
        if (i%4==0 or i%4-1==0):
            #horizontally
            if lst[i+1]==lst[i] and lst[i+2]==lst[i]:
                trils+=1
            #diagonaly for 1st and 2nd col
            if ((i<listlen-10 and lst[i]==lst[i+5]) and lst[i]==lst[i+10]):
                trils+=1
        #diagonaly for 3rd and 4th col
        if (i%4-2==0 or i%4-3==0):
            if ((i<listlen-8 and lst[i]==lst[i+3]) and lst[i]==lst[i+6]):
                trils+=1
        #vertically
        if ((i<listlen-8 and lst[i]==lst[i+4]) and lst[i]==lst[i+8]):
            trils+=1
    print(lst)
    print('There are',trils,'trilizes in the table')

    #Results Set:
    #[1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0]
    #There are 4 trilizes in the table


#Exercise13
def stats(lst,strng):

    statslist = []
    listlenth=len(lst)
    strlength=len(strng)

    for i in range (strlength):
        statslist.append(0)
        count=0
        for j in range (listlenth):
            if strng[i]==lst[j]:
                count+=1
        statslist[i]=str(round(count/listlenth*100, 2))+'%'

    print('The display rate of every letter is:')
    print(list(strng))
    print(statslist)
    #Results Set:
    #The display rate of every letter is:
    #['t', 'l', 'x', 's', 'r', 'n']
    #['13.51%', '5.41%', '0.0%', '13.51%', '5.41%', '2.7%']