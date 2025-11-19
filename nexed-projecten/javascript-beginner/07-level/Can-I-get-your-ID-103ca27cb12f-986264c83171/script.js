const leeftijdLeonie = parseInt(document.getElementById('leeftijdLeonie').textContent);
const leeftijdMustafa = parseInt(document.getElementById('leeftijdMustafa').textContent);

const naamLeonie = document.getElementById('naamLeonie');
const naamMustafa = document.getElementById('naamMustafa');

if (leeftijdLeonie >= 17) {
    naamLeonie.textContent = "Leonie mag beginnen met rijlessen!";
} else {
    naamLeonie.textContent = "Leonie moet nog even wachten!";
}

if (leeftijdMustafa >= 17) {
    naamMustafa.textContent = "Mustafa mag beginnen met rijlessen!";
} else {
    naamMustafa.textContent = "Mustafa moet nog even wachten!";
}