function bestSum(
    targetSum: number, 
    numbers: number[], 
    memo: Record<number, number[]|null> = {}
): number[] | null {
    if (targetSum in memo) return memo[targetSum];
    if (targetSum === 0) return [];
    if (targetSum < 0) return null;
    var soln: number[] | null = null;

    for (const num of numbers) {
        const newTargetSum = targetSum - num;
        const res = bestSum(newTargetSum, numbers, memo)
        
        if (res !== null) {
            const tmpSoln = [num, ...res];
            if (soln === null || (soln !== null && soln.length > tmpSoln.length)) soln = tmpSoln;
        }
    }
    memo[targetSum] = soln;
    return soln;
}

const res = bestSum(1000, [2,3,4,5,6,1000]);
console.log(res);