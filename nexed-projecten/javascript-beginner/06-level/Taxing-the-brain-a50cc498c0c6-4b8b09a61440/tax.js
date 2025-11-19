function calculateTax(income) {
    let tax = 0;

    if (income > 70000) {
        tax += (income - 70000) * 0.9;
        income = 70000;
    }
    if (income > 30000) {
        tax += (income - 30000) * 0.5;
        income = 30000;
    }
    if (income > 10000) {
        tax += (income - 10000) * 0.2;
        income = 10000;
    }

    return tax;
}

function calculatePercentageTax(income) {
    let tax = calculateTax(income);
    return (tax / income) * 100;
}

function findIncomeFor50PercentTax() {
    let income = 70000;
    while (calculatePercentageTax(income) < 50) {
        income++;
    }
    return income;
}

let inputIncome = process.argv[2];

if (inputIncome) {
    inputIncome = parseFloat(inputIncome);
    let percentageTax = calculatePercentageTax(inputIncome);
    console.log(percentageTax);
} else {
    console.log(findIncomeFor50PercentTax());
}