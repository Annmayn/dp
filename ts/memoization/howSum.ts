function howSum(
    targetSum: number,
    numbers: number[],
    memo: Record<number, number[] | null> = {}
): number[] | null {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum < 0) return null;
    if (targetSum === 0) return []

    for (const num of numbers) {
        const newTargetSum = targetSum - num;
        const res = howSum(newTargetSum, numbers, memo);
        if (res !== null) {
            const soln = [num, ...res];
            memo[targetSum] = soln;
            return soln;
        }
    }
    memo[targetSum] = null;
    return null;
}

const res = howSum(300, [7, 14]);
console.log(res);