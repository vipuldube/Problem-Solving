def len_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = len_word(["abc", "Exercises", "Backend"])
print("\nLen: ",result[1])
print("Len: ",result[0])