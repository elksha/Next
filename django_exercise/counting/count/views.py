from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    firstcount=[]
    count=[]
    dummy=[]
    final=[]
    const=0
    text = request.GET['fulltext']
    textcount = len(text)
    divide = text.split()
    wordcount = len(divide)
    for i in divide:
        firstcount.append(divide.count(i))
    total = dict(zip(divide,firstcount))
    word = list(total)
    for j in word:
        count.append(total[j])
    for k in word:
        dummy.append(const)
        const+=1
    for i in dummy:
        final.append(word[i]+':'+str(count[i]))
    return render(request, 'result.html', {
        'text':text,
        'textcount':textcount,
        'word':word,
        'wordcount':wordcount,
        'count':count,
        'final':final,
    })