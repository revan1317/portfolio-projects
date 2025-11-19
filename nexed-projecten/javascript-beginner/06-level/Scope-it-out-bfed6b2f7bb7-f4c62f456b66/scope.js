let wachtwoord = "fout";
aanmelden(wachtwoord);

wachtwoord = "geheim";
aanmelden(wachtwoord);

function aanmelden(invoerWachtwoord) {
    let bericht = "Er is niemand thuis";

    if (invoerWachtwoord == "geheim") {
        bericht = "Welkom!";
    } else {
        bericht = "FOUT WACHTWOORD!";
    }
    console.log(bericht);
}