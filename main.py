import json

with open("newsafr.json", encoding="utf-8") as f:
    j_data = json.load(f)
    news_list = j_data["rss"]["channel"]["items"]
full_set = set()
for news in news_list:
    full_set.add(news["description"])

def count_word(full_set):
    full_set = ', '.join(full_set)
    full_set = full_set.split(" ")
    word_value = {}
    for elements in full_set:
        if len(elements) > 6:
            if elements in word_value:
                word_value[elements] += 1
            else:
                word_value[elements] = 1
    return word_value

def sorted_w(word_value):
    sorted_words = sorted(word_value.items(), key=lambda x: x[1], reverse=True)
    return sorted_words

print(f'Топ-10 самых часто встречающихся в новостях слов: {sorted_w(count_word(full_set))[:10]}')
