function gridTraveller(m: number, n: number, memo: Record<string, number> = {}): number {
    const key = `${m},${n}`;
    if (key in memo) return memo[key];
    if ((m === 1 && n === 2) || (m === 2 && n === 1) || (m === 1 && n === 1)) return 1;
    var totalWays = 0
    if (m - 1 > 0) totalWays += gridTraveller(m - 1, n, memo);
    if (n - 1 > 0) totalWays += gridTraveller(m, n - 1, memo);
    memo[key] = totalWays;
    return totalWays;
}

const res = gridTraveller(25, 25);
console.log(res);