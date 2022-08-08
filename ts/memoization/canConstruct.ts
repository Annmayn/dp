function canConstruct(
    target: string, 
    wordBank: string[],
    memo: Record<string, boolean> = {},
): boolean {
    if (target in memo) return memo[target];
    if (target === '') return true;
    for (const [ind, word] of wordBank.entries()) {
        if (target.startsWith(word)) {
            const newTarget = target.slice(word.length);
            if (canConstruct(newTarget, wordBank, memo)) {
                memo[target] = true;
                return true;
            }
        }
    }
    memo[target] = false;
    return false;
}

const res = canConstruct('abcdef', ['ab', 'abc', 'def', 'abcd', 'cd']);
console.log(res);