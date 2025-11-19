let nederland = parseInt(process.argv[2]);
let duitsland = parseInt(process.argv[3]);
let frankrijk = parseInt(process.argv[4]);

console.log(
    "Nederland heeft minder inwoners dan Duitsland én Frankrijk: " +
    (nederland < duitsland && nederland < frankrijk));

console.log(
    "Nederland óf Frankrijk heeft meer inwoners dan Duitsland: " +
    (nederland > duitsland || frankrijk > duitsland));

console.log(
    "Het is niet waar dat Nederland meer inwoners heeft dan Duitsland: " +
    !(nederland > duitsland));