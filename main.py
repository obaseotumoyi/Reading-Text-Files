# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(): 
    
    # [assignment] Add your code here 
    with open('story.txt', 'r') as openfile:
        readfile = openfile.read()
        print(readfile)
    return readfile        

readfile = read_file_content()




def count_words():
  
    text = read_file_content()
    
    split_txt = text.split()

    
    count = {}

    for word in split_txt:
        if word in count:
            count[word] += 1
        else :
            count[word] = 1

    return count

print(count_words())