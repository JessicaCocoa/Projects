def get_words_from_file(filename):
    with open(filename) as file: ##Open the file in read mode
        text = file.read()

    text = text.replace("\n", "") #Takes out all white space
    text = text. replace(",", "") # takes out all commas
    text = text. replace(".", "") #takes out all periods
    text = text.lower() # converts to lower case

    words = text.split(" ") #turn it into individual words
    return words

def count_words(words):
    word_count = {} # creates the dictionary
    for word in words:
        if word in word_count:
            word_count[word] +=1 # if the word is there it adds one to it's count
        else:
            word_count[word] = 1 # if word is not there it adds it to the dictionary
    return word_count

def display_word_count(word_count):
    words = list(word_count.keys()) #makes the keys into a list
    words.sort(key=str.lower) #sorts the list alphabetically
    for word in words:
        count = word_count[word] # this allows you to access the key and give it a variable
        print(word, "=", count)

def main():
    print("The Word Counter Program") ##prompts user to enter text file
    filename = input("Enter file name .txt")

    words = get_words_from_file(filename)
    word_count = count_words(words)
    display_word_count(word_count)

if __name__ =="__main__":
    main()

