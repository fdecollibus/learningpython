import sys
import operator

print ('Now proceeding with split...')
wordCount = {}
if len(sys.argv)==2:
    original_text = sys.argv[1]

    textFile=open(sys.argv[1],"r")
    for i in textFile:
        for word in i.split():
            if word.lower() in wordCount.keys():
                wordCount[word.lower()]+=1
            else:
                wordCount[word.lower()]=1
    newFileName = sys.argv[1][:-4] +"_count" + sys.argv[1][-4:]
    textFile.close()
    textCountFile=open(newFileName, "w")

    sortedWordCount = sorted(wordCount.items(),key=operator.itemgetter(1), reverse=True)
    totalNumberOfWords=0
    totalWords=0
    for occurrence in sortedWordCount:
            totalNumberOfWords+=occurrence[1]
            totalWords+=1
    textCountFile.write("Number of words: {} \n".format(totalWords))
    textCountFile.write("Total occurrence of words: {} \n".format(totalNumberOfWords))
    textCountFile.write("{}: {} \n".format(occurrence[0],occurrence[1]))
    for occurrence in sortedWordCount:
        textCountFile.write("{}: {} \n".format(occurrence[0],occurrence[1]))
else:
    print("Argument number invalid")
