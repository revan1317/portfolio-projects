function collatzSequenceLength(n) {
    let steps = 0;
    while (n !== 1) {
        if (n % 2 === 0) {
            n /= 2;
        } else {
            n = n * 3 + 1;
        }
        steps++;
    }
    return steps;
}

const input = parseInt(process.argv[2]);
const firstResult = collatzSequenceLength(input);
const secondResult = collatzSequenceLength(firstResult);
const finalResult = collatzSequenceLength(secondResult);

console.log(finalResult);