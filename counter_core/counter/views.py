from django.shortcuts import render
from counter.models import WoCount
import matplotlib.pyplot as plt
import seaborn as sns
import re
import pandas as pd


def word_changer(text='') -> list:
    words_only = re.findall(r"[\w']+", text)
    words = []
    for i in words_only:
        temp = []
        for ch in i:
            temp.append(ch.lower())
        words.append(''.join(temp))
    return words


def word_df(words: list):
    found = {}
    words_set = set(words)
    for i in words:
        if i in words_set:
            found.setdefault(i, 0)
            found[i] += 1

    words_list = []
    values_list = []
    for key in found:
        words_list.append(key)
        values_list.append(found[key])

    found_df = pd.DataFrame({'word': words_list, 'value': values_list})
    found_df = found_df.sort_index(by=['value'], ascending=False)
    return found_df


def plot_maker(found_df):
    plt.bar(data=found_df, x='word', height='value')
    return plt.show()


def final(request):
    title = ''
    text = ''
    result_pre = 'Wait a second ;)'

    if request.GET.get('title'):
        title = request.GET.get('title')
        if request.GET.get('text'):
            text = request.GET.get('text')
            a = word_changer(text)
            b = word_df(a)
            result = plot_maker(b)

    obj = WoCount.objects.create(title=title, text=text)
    obj.save()

    return render(
        request,
        'index.html',
        {
            'title': title,
            'text': text,
            'result': result_pre
        }
    )
