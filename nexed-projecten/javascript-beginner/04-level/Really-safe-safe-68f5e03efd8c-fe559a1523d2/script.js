function checkKluisToegang(fouten, pincode, functie, dag, tijd) {
    const correctePincode = 123752;
    const isBestuur = functie === "bestuur";
    const isAdmin = functie === "administratief medewerker";
    const isWerktijd = dag >= 0 && dag <= 4 && tijd >= 9 && tijd < 17;

    console.log(`#fouten: ${fouten}, pin: ${pincode}, functie: ${functie}, dag: ${dag}, tijd: ${tijd}`);

    if (fouten >= 5) {
        console.log("Kluis is geblokkeerd");
    } else if (pincode === correctePincode) {
        if (isBestuur || (isAdmin && isWerktijd)) {
            console.log("Kluis opent");
            if (!isBestuur) {
                console.log("Sms naar bestuur");
            }
        } else if (isWerktijd) {
            console.log("Alarm gaat af");
        } else {
            console.log("Stil alarm gaat af");
        }
    } else {
        console.log("Verkeerde pincode");
    }
}

const args = process.argv.slice(2);

if (args.length !== 5) {
    console.log("Gebruik: node script.js <fouten> <pincode> <functie> <dag> <tijd>");
} else {
    const fouten = parseInt(args[0], 10);
    const pincode = parseInt(args[1], 10);
    const functie = args[2];
    const dag = parseInt(args[3], 10);
    const tijd = parseInt(args[4], 10);

    checkKluisToegang(fouten, pincode, functie, dag, tijd);
}