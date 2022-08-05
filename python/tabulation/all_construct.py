from typing import List


def all_construct(word: str, word_dict: List[str]) -> List[List[str]]:
    reference = [word[:i] for i in range(len(word)+1)]
    res = [None]*(len(word)+1)
    res[0] = [[]]
    for ind in range(len(res)):
        if res[ind] is not None:
            for wrd in word_dict:
                new_wrd = reference[ind] + wrd
                new_word_dict = [each_dict+[wrd] for each_dict in res[ind]]
                try:
                    if word.index(new_wrd) == 0 and new_wrd != '':
                        if res[len(new_wrd)] is None:
                            res[len(new_wrd)] = new_word_dict
                        else:
                            res[len(new_wrd)].extend(new_word_dict)
                except ValueError:
                    pass
    return res[-1]


if __name__ == "__main__":
    word = "apple"
    word_dict = "ap app le p l e".split()
    res = all_construct(word, word_dict)
    print(f"Res: {res}")
