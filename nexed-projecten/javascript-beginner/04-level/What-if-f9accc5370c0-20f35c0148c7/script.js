const args = process.argv.slice(2);
const stad = args[0];

console.log(`De stad is ${stad}`);

if (stad === "Amsterdam") {
    console.log("Het is de hoofdstad van Nederland");
}