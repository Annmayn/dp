function countConstruct(
    target: string, 
    wordBank: string[],
    memo: Record<string, number> = {}
): number {
    if (target in memo) return memo[target];
    if (target === '') return 1;
    var allCount = 0;
    for (const word of wordBank) {
        if (target.startsWith(word)) {
            const newTarget = target.slice(word.length);
            const count = countConstruct(newTarget, wordBank, memo);
            allCount += count;
        }
    }
    memo[target] = allCount;
    return allCount;
}

const res = countConstruct('abcdef', ['ab', 'abc', 'def', 'abcd', 'cd', 'ef']);
console.log(res);