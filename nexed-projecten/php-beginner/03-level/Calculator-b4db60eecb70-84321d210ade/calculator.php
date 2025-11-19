<?php

$operator = readline("Welke operatie wil je uitvoeren? (+ of -): ");
$getal1 = readline("Voer het eerste getal in: ");
$getal2 = readline("Voer het tweede getal in: ");

if ($operator == "+") {
    $resultaat = $getal1 + $getal2;
    echo "Het resultaat van $getal1 + $getal2 is: $resultaat";
} elseif ($operator == "-") {
    $resultaat = $getal1 - $getal2;
    echo "Het resultaat van $getal1 - $getal2 is: $resultaat";
} else {
    echo "Ongeldige operator. Kies alleen + of -.";
}

?>