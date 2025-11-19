document.addEventListener("DOMContentLoaded", function () {
    const ageElements = document.querySelectorAll("h2:nth-of-type(2) span");
    const nameElements = document.querySelectorAll("h1");

    ageElements.forEach((ageElement, index) => {
        const age = parseFloat(ageElement.textContent);

        if (age < 16.5) {
            nameElements[index].classList.add("wachten");
        } else {
            nameElements[index].classList.add("starten");
        }
    });
});