let totaleKosten = parseInt(process.argv[2]);
let gemeenteBijdrage = Math.floor(totaleKosten / 3) * 3;
let stadBijdrage = totaleKosten - gemeenteBijdrage;

console.log(`In totaal is er ${totaleKosten} miljoen uitgegeven`);
console.log(`De stad betaalt ${stadBijdrage} miljoen`);
console.log(`De gemeente betaalt ${gemeenteBijdrage} miljoen`);