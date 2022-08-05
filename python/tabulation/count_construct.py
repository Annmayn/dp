from typing import List


def count_construct(word: str, word_dict: List[str]) -> bool:
    reference = [word[:i] for i in range(len(word)+1)]
    res = [0]*(len(word)+1)
    res[0] = 1
    for ind in range(len(res)):
        if res[ind] != 0:
            for wrd in word_dict:
                new_wrd = reference[ind] + wrd
                try:
                    if word.index(new_wrd) == 0 and new_wrd != '':
                        res[len(new_wrd)] += res[ind]
                except ValueError:
                    pass
    print(res)
    return res[-1]


if __name__ == "__main__":
    word = "apple"
    word_dict = "ap app le p l e".split()
    res = count_construct(word, word_dict)
    print(f"Res: {res}")
