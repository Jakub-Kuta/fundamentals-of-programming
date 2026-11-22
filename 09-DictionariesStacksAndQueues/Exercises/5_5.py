###
# Counts how many times each word appears in a paragraph
#
paragraph = "cat dog mouse cat rat cat mouse"

counts = {}
for word in paragraph.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

for word, count in counts.items():
    print(f'{word}: {count}')
