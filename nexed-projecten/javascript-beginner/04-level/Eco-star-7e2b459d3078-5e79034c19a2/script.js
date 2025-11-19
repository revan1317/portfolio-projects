const dieselVerboden = process.argv[2];
const afvalscheiding = process.argv[3];
const natuurgebied = parseInt(process.argv[4]);

let sterren = 0;

if (dieselVerboden === "ja") {
    sterren++;
}

if (afvalscheiding === "ja") {
    sterren++;
}

if (natuurgebied > 25) {
    sterren++;
}

if (sterren === 3) {
    console.log("Het is een milieuvriendelijke stad");
} else if (sterren === 0) {
    console.log("De stad moet omgevormd worden");
} else {
    console.log(`De stad heeft nog ${3 - sterren} ster(ren) nodig om milieuvriendelijk te zijn`);
}