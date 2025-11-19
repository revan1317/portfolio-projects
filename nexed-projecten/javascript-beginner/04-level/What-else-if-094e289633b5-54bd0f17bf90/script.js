const inwoners = parseInt(process.argv[2]);

if (inwoners > 10000) {
    console.log("Megastad");
} else if (inwoners > 25) {
    console.log("Stad");
} else {
    console.log("dorp");
}