const woorden = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"];

function filterWoorden(woordenlijst, letter) {
    for (let woord of woordenlijst) {
        if (woord.includes(letter)) {
            console.log(`${woord} bevat de letter '${letter}'`);
        }
    }
}

filterWoorden(woorden, 'o');
filterWoorden(woorden, 'p');
filterWoorden(woorden, 'q');