function voegToe(arr) {
    arr.push(4);
}

function vervangArray(arr) {
    arr = [1, 2, 3, 4];
}

let mijnArray = [1, 2, 3];

console.log("Voor de push: ", mijnArray);
voegToe(mijnArray);
console.log("Na de push: ", mijnArray);

console.log("Voor de toewijzing: ", mijnArray);
vervangArray(mijnArray);
console.log("Na de toewijzing: ", mijnArray);