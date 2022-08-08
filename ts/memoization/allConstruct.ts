function allConstruct(
    target: string,
    wordBank: string[],
    memo: Record<string, string[][] | null> = {}
): string[][] | null {
    if (target in memo) return memo[target];
    if (target === '') return [[]];

    var solution: string[][] | null = null;
    for (const word of wordBank) {
        if (target.startsWith(word)) {
            const newTarget = target.slice(word.length);
            const res = allConstruct(newTarget, wordBank, memo);
            if (res !== null) {
                const solnArr = res.map(arr => [word, ...arr]);
                if (solution === null) solution = solnArr;
                else solution = solution.concat(solnArr);
            }
        }
    }
    memo[target] = solution;
    return solution;
}

const res = allConstruct('abcdef', ['ab', 'abc', 'def', 'abcd', 'cd', 'ef']);
console.log(res);