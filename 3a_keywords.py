import keyword

print("Python keywords:\n")

keywords = keyword.kwlist

for count, word in enumerate(keywords, start=1):
    print(word, end=" ")
    if count % 5 == 0:
        print()

print("\nPython soft keywords:")
print(keyword.softkwlist)
