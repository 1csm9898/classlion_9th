from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")

def result(request):
    sentence=request.GET["sentence"]
    wordList=sentence.split()
    wordDict={}
    oneUse=[]
    for word in wordList:
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word] = 1
    for word1 in wordDict:
        if wordDict[word1]==1:
            oneUse.append(word1)
    return render(request,"result.html",{'fulltext':sentence,'count':len(wordList),'wordDict':wordDict.items,'oneUse':oneUse})