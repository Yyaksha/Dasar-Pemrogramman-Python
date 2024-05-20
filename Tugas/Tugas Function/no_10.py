def anagram(kata1, kata2):
    return sorted(kata1) == sorted(kata2)

print(anagram("listen", "silent"))