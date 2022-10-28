def ShowSorted(text):
    text = text.replace(".", " ")
    text = text.replace(",", " ")

    allWords = text.split();
    allWordsSingle = {};
    for word in allWords:
        if len(word) > 3:
            allWordsSingle.update({word: allWords.count(word)})

    keysSorted = []
    for key in allWordsSingle: 
        keysSorted.append(key)

    keysSorted.sort();

    for key in keysSorted:
        print(key)

def ShowWordCount(text):
    text = text.replace(".", " ")
    text = text.replace(",", " ")

    allWords = text.split();
    allWordsSingle = {};

    for word in allWords:
        allWordsSingle.update({word: allWords.count(word)})

    keysSorted = []
    for key in allWordsSingle:
        keysSorted.append(key)
    keysSorted.sort()

    for key in keysSorted:
        print(f"{key} - {allWordsSingle[key]}")

def ShowTopFiveWords(text):
    allWords = text.split()
    allWordsSingle = {};

    for word in allWords:
        allWordsSingle.update({word: allWords.count(word)})

    wordsWithCount = {}
    for word in allWordsSingle:
        wordsWithCount.update( {word: allWords.count(word)} )

    iteration = 1
    for word in sorted(wordsWithCount.items(), key=lambda item: item[1], reverse=True):
        if iteration <= 5:
            print(f"Top {iteration} - {word[0]}: {word[1]} times")
            iteration += 1;
    print("\n")

def ShowTextLenght(text):
    print(len(text))

text = input("\n\nEnter a text: ")
while True:

    action = input("Select an action: \n1 - Show words sorted\n2 - Show words count\n3 - Show text lenght\n4 - Show top five words\nEnter your answer: ")
    if action == "1":
        ShowSorted(text);
    elif action == "2":
        ShowWordCount(text)
    elif action == "3":
        ShowTextLenght(text)
    elif action == "4":
        ShowTopFiveWords(text)
    else:
        print("Invalid action!")
