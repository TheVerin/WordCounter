from django.shortcuts import render
from counter.models import WoCount
import matplotlib.pyplot as plt
import re


def word_changer(text='') -> list:
    words_only = re.findall(r"[\w']+", text)
    words = []
    for i in words_only:
        temp = []
        for ch in i:
            temp.append(ch.lower())
        words.append(''.join(temp))
    return words


def word_dict(words: list):
    found = {}
    words_set = set(words)
    for i in words:
        if i in words_set:
            found.setdefault(i, 0)
            found[i] += 1
    return found


def plot_maker(found: dict):
    plt.bar(range(len(found)), found.values(), align='center')
    plt.xticks(range(len(found)), list(found.keys()))
    return plt.show()


def final(request):
    title = ''
    text = ''
    result = ''

    if request.GET.get('title'):
        title = request.GET.get('title')
        if request.GET.get('text'):
            text = request.GET.get('text')
            a = word_changer(text)
            b = word_dict(a)
            result = plot_maker(b)

    obj = WoCount.objects.create(title=title, text=text)
    obj.save()

    return render(
        request,
        'index.html',
        {
            'title': title,
            'text': text,
            'result': result
        }
    )
