const args = process.argv.slice(2);

const gemiddeldeTemperatuur = parseInt(args[0]);
const totaleNeerslag = parseInt(args[1]);
const laagsteTemperatuur = parseInt(args[2]);

console.log(
    `gemiddelde temperatuur: ${gemiddeldeTemperatuur}°C, ` +
    `neerslag: ${totaleNeerslag} mm, ` +
    `laagste temperatuur: ${laagsteTemperatuur}°C`,
);

function isWarmLand(gemiddeldeTemp, neerslag, laagsteTemp) {
    const voldoetAanCriteria1 = gemiddeldeTemp > 20 && neerslag < 750;
    const voldoetAanCriteria2 = laagsteTemp >= 10 || gemiddeldeTemp >= 25;
    return voldoetAanCriteria1 || voldoetAanCriteria2;
}

const isLandWarm = isWarmLand(
    gemiddeldeTemperatuur,
    totaleNeerslag,
    laagsteTemperatuur,
);
console.log(`Het land is een warm land: ${isLandWarm}`);