words = []
while True:
    try:
        words = words + input().split()
    except:
        break
        
def sort_(items):
    
    #Sort by lexicographic
    items.sort(reverse = False)
    
    #Sort by number of occurences
    tmp_value = [(int(v), k) for k,v in items]
    tmp_value.sort(key = lambda x: x[0], reverse = True)
    sorted_ = [k for (v, k) in tmp_value]
    
    return sorted_

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1
    
items = list(counts.items())
print(*sort_(items), sep = '\n')