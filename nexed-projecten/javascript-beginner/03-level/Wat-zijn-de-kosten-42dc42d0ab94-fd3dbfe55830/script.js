let administratie = parseInt(process.argv[2]);
let infrastructuur = parseInt(process.argv[3]);
let evenementen = parseInt(process.argv[4]);
let totaal = parseInt(process.argv[5]);

let administratieEnInfrastructuur = administratie + infrastructuur;
let overigeKosten = totaal - (administratieEnInfrastructuur + evenementen);
let percentageAdministratie = (administratie / totaal) * 100;

console.log("totaal uitgegeven aan administratie en infrastructuur " + administratieEnInfrastructuur + " miljoen");
console.log("overige kosten " + overigeKosten + " miljoen");
console.log("percentage administratiekosten van het totaal " + percentageAdministratie + "%");
