from django.shortcuts import render
from counter.models import WoCount
import matplotlib.pyplot as plt


def word_changer(text: str) -> list:
    dot = text.split('.')
    str_1 = ''.join(dot)
    pre_words = str_1.split(' ')
    words = []
    for i in pre_words:
        temp_list = []
        for ch in i:
            temp_list.append(ch.lower())
            words.append(''.join(temp_list))
    return words


def word_dict(words: list) -> dict:
    words = word_changer()
    found = {}
    words_set = set(words)
    for i in words:
        if i in words_set:
            found.setdefault(i, 0)
            found[i] += 1
    found = [(k, found[k]) for k in sorted(found, key=found.get, reverse=True)]
    return found


def plot_maker(found: dict):
    found = word_dict()
    plt.bar(range(len(found)), found.values(), align='center')
    plt.xticks(range(len(found)), list(found.keys()))
    return plt.show()


def final(request):
    title = ''
    text = ''

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