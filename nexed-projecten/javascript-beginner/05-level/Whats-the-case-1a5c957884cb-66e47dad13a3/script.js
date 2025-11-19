function berekenKorting(totaalbedrag, dag) {
    let kortingPercentage;

    switch (dag) {
        case 0:
            kortingPercentage = 0;
            break;
        case 1:
            kortingPercentage = 2;
            break;
        case 2:
            kortingPercentage = 3;
            break;
        case 3:
            kortingPercentage = 4;
            break;
        case 4:
            kortingPercentage = 0.5;
            break;
        case 5:
            kortingPercentage = 1.5;
            break;
        case 6:
            kortingPercentage = 5;
            break;
        default:
            console.log("Ongeldige dag");
            return;
    }

    const kortingFactor = (100 - kortingPercentage) / 100;
    const totaalNaKorting = totaalbedrag * kortingFactor;

    console.log(`Totalbedrag is ${totaalNaKorting}`);
}

const args = process.argv.slice(2);

if (args.length !== 2) {
    console.log("Gebruik: node script.js <totaalbedrag> <dag>");
} else {
    const totaalbedrag = parseFloat(args[0]);
    const dag = parseInt(args[1], 10);

    berekenKorting(totaalbedrag, dag);
}