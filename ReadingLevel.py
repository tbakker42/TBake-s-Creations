def readingLevel(inFile):
    fin = open(inFile,"r",encoding="latin1")
    contents = fin.read()
    fin.close()

#Sentence Count
    sentences = 0
    sentenceChars = ".?!"
    for i in range(len(contents)):
        character = contents[i]
        if character in sentenceChars:
            sentences = sentences + 1

#Word Count
    contents = contents.lower()
    chars = '.",;-_:()[]{}'
    for punc in chars:
        contents = contents.replace(punc, "")

    contents = contents.split()

    words = []
    for i in range(len(contents)):
        data = contents[i]
        words.append(data)

#Syllable Count
    wordList = []
    for i in range(len(words)):
        data = words[i]
        oneWord = [data]
        wordList.append(oneWord)

    vowel = "aeiouy"
    totalVow = 0

    for i in range(len(wordList)):
        data = wordList[i]
        word = data[0]
        last = len(word) - 1        
        for i in range(last):
            character = word[i]
            if character in vowel:
                totalVow = totalVow + 1
                after = word[i + 1]
                if after in vowel:
                    totalVow = totalVow - 1
        if word[last] == "a" or word[last] == "i" or word[last] == "o" or word[last] == "u" or word[last] == "y":
            totalVow = totalVow + 1
            if totalVow == 0:
                totalVow = totalVow + 1
        
    totalWords = len(wordList)
    level = round((0.39*(totalWords/sentences)) +
    (11.8*(totalVow/totalWords))-15.59,2)

    print(level)
    print(totalWords)
    print(sentences)
    print(totalVow)
##    print(vowelTotal)
##    print(words)
