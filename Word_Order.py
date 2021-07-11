#You are given n words. Some words may repeat. For each word, output its number of occurrences.
# The output order should correspond with the input order of appearance of the word.
"""
**Sample Input**
4
bcdef
abcdefg
bcde
bcdef

**Sample Output**
3
2 1 1
"""

if __name__ == "__main__":
    words = {}
    for _ in range(int(input("Please enter number of words: "))):
        word = input("Please enter the word")
        if word in words.keys():
            words[word] += 1
        else:
            words.update({word: 1})

    print(len(words.keys()))
    print(*words.values())

