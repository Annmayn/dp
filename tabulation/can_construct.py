from typing import List


def can_construct(word: str, word_dict: List[str]) -> bool:
    res = [None]*(len(word)+1)
    res[0] = ''
    for ind in range(len(res)):
        if res[ind] is not None:
            for wrd in word_dict:
                new_wrd = res[ind] + wrd
                try:
                    if word.index(new_wrd) == 0 and new_wrd != '':
                        res[len(new_wrd)] = new_wrd
                except ValueError:
                    pass
    print(res)
    return res[-1] is not None


if __name__ == "__main__":
    word = "apple"
    word_dict = "ap appl le p".split()
    res = can_construct(word, word_dict)
    print(f"Res: {res}")
