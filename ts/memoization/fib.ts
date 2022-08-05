function fib(n: number, memo: Record<number, number> = {}): number {
    if (n in memo) {
        return memo[n];
    }
    if (n <= 2) return 1
    const newMemo = fib(n - 1, memo)
    const res = fib(n - 1, memo) + fib(n - 2, memo);
    memo[n] = res;
    return res;
}


console.log(fib(100));