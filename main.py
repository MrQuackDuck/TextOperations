def ShowSorted(text):
    text = text.replace(".", " ")
    text = text.replace(",", " ")

    allWords = text.split();
    allWordsSingle = {};
    for word in allWords:
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

def ShowTextLenght(text):
    print(len(text))



text = input("\n\nEnter a text: ")
while True:

    action = input("Select an action: \n1 - Show words sorted\n2 - Show words count\n3 - Show text lenght\n")
    if action == "1":
        ShowSorted(text);
    elif action == "2":
        ShowWordCount(text)
    elif action == "3":
        ShowTextLenght(text)
    else:
        print("Invalid action!")