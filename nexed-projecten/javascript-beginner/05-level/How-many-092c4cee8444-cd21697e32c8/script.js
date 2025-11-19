const boodschappen = process.argv.slice(2);
let havermelkTeller = 0;

for (let i = 0; i < boodschappen.length; i++) {
    if (boodschappen[i] === "havermelk") {
        havermelkTeller++;
    }
}

console.log(`Aantal havermelk: ${havermelkTeller}`);