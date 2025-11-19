const pincode = parseInt(process.argv[2], 10);
const functie = process.argv[3];
const dag = parseInt(process.argv[4], 10);

const correctePincode = 123752;
const isWeekend = dag === 5 || dag === 6;
const heeftToegang = functie === "bestuur" || functie === "administratief medewerker";

if (Number.isNaN(pincode) || Number.isNaN(dag)) {
    console.log("Ongeldige invoer. Gebruik: node script.js <pincode> <functie> <dag>");
} else if (pincode === correctePincode && heeftToegang) {
    console.log("Toegang verleend");
} else if (!isWeekend) {
    console.log("Verkeerde pincode of je hebt niet de juiste rechten");
} else {
    console.log("Veiligheidsdiensten worden ingeschakeld");
}