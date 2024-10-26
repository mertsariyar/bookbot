def main():
    path_to_file = "/home/mert/workspace/github.com/mertsariyar/bookbot/books/frankenstein.txt"

    with open(path_to_file) as f: #Dosyayı okuma modunda açtık
        file_contents = f.read() #Dosyayın tüm içeriğini okuduk
    
    def myCounter(file_contents):
        counter = 0
        x = file_contents.split()
        for i in x:
            counter += 1
        return counter
    total_words = myCounter(file_contents)
    print(f"{total_words} words found in the document")

    #takes the text from the book as a string # 
    #returns the number of times each char in the string#
    #convert any char to lowercase
    #no duplicates.
    #use dictionary string > integer
    #when you print out the dict it should look like this {'p': 6121, 'r': 20818, 'o': 25225, ...
    
    
    def charCounter(file_contents):
        x = file_contents.lower()
        dictCounter = {}

        for char in x:
            if char in dictCounter:
                dictCounter[char] += 1
            else:
                dictCounter[char] = 1    
            
        return dictCounter
    
    total_counts = charCounter(file_contents)
    for key, value in total_counts.items():
        print(f"The '{key}' character was found {value} times")
        

        



            
    
        



if __name__ == "__main__": #Programı çalıştırmak için ana fonksiyonu çağırdık
    main()