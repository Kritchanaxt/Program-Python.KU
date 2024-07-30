
#7.
def vowel_counter(sentence):
    count = 0
    for ind in sentence:
        if (ind.lower() in ['a', 'e', 'i', 'o', 'u']):
            count += 1

    return (count)

sent = "My name is Wave"
print(vowel_counter(sent))