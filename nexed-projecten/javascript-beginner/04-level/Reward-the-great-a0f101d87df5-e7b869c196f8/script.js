function bepaalBeloning(rating, percentageNatuur, kmAutowegdek) {
    console.log(`rating: ${rating} sterren, natuurgebied: ${percentageNatuur}%, autowegdek: ${kmAutowegdek} km`);

    if (rating < 3) {
        if (kmAutowegdek > 200) {
            console.log("subsidie voor ombouwen autoweg naar fietsstraat");
        } else {
            console.log("subsidie voor afvalinzameling");
        }
    } else if (percentageNatuur > 25) {
        console.log("belastingkorting voor de inwoners");
    } else {
        console.log("subsidie voor aanleg van meer natuur");
    }
}

const args = process.argv.slice(2);

if (args.length !== 3) {
    console.log("Gebruik: node script.js <rating> <percentageNatuur> <kmAutowegdek>");
} else {
    const rating = parseInt(args[0], 10);
    const percentageNatuur = parseInt(args[1], 10);
    const kmAutowegdek = parseInt(args[2], 10);

    bepaalBeloning(rating, percentageNatuur, kmAutowegdek);
}