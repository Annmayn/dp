function canSum(targetSum: number, numbers: number[], memo: Record<number, boolean> = {}): boolean {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return true;
    if (targetSum < 0) return false;
    for (const num of numbers) {
        const newTargetSum = targetSum - num;
        if (canSum(newTargetSum, numbers, memo)) {
            memo[targetSum] = true;
            return true;
        }
    }
    memo[targetSum] = false;
    return false;
}

const res = canSum(300, [7, 14]);
console.log(res);