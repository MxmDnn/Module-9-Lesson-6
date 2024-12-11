def all_variants(text) :
    value = len(text)
    for i in range(1, value + 1) :
        for j in range(value - i + 1) :
            yield text[j:j+i]

a = all_variants('abc')
for i in a :
    print(i)


