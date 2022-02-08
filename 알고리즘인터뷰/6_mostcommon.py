from typing import List
import collections
import re
def mostCommonWord(paragraph: str, banned: List[str]) -> None:
    words = [word for word in re.sub(r'[^\w]', " ", paragraph).lower().split() if word not in banned]
    # \w 단위 문자를 뜻함
    # ^ not을 의미함
    print(words)
    counts = collections.Counter(words)

    return counts.most_common(1)[0][0]


paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit'
banned = ['hit']

print(mostCommonWord(paragraph, banned))