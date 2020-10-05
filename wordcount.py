# put your code here.
def word_count(filename):
    test = open(filename) #open file
    #create dictionary 
    word_counts = {}
    #iterate through each line in the file
    for line in test:
    #we want to get a list of words
        words = line.split(" ")
    #iterate through each word 
        for word in words:
            #check to see if the word is in the dic; if not add 1
           word_counts[word] = word_counts.get(word, 0) + 1
    #return the dictionary
    return word_counts