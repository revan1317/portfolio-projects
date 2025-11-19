document.addEventListener("DOMContentLoaded", function () {
    const ageElements = document.querySelectorAll("h2:nth-of-type(2) span");
    const nameElements = document.querySelectorAll("h1");
    const h2Elements = document.querySelectorAll("h2");
    const spanElements = document.querySelectorAll("span");

    ageElements.forEach((ageElement, index) => {
        const age = parseFloat(ageElement.textContent);

        if (age < 16.5) {
            nameElements[index].classList.add("wachten");
        } else {
            nameElements[index].classList.add("starten");
        }
    });

    nameElements.forEach(name => {
        name.style.textDecoration = "underline";
    });

    h2Elements.forEach(h2 => {
        h2.style.fontStyle = "italic";
    });

    spanElements.forEach(span => {
        span.style.fontSize = "32px";
    });
});