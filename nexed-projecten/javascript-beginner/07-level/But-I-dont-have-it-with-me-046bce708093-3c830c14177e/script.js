const leeftijdLeonie = parseInt(document.querySelector('.leonie h2').textContent);
const leeftijdMustafa = parseInt(document.querySelector('.mustafa h2').textContent);

const naamLeonie = document.querySelector('.leonie h1');
const naamMustafa = document.querySelector('.mustafa h1');

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