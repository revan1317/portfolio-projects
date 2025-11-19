<?php

$operator = readline("Welke operatie wil je uitvoeren? (+, -, %): ");
if (!in_array($operator, ['+', '-', '%'])) {
    echo "Fout: geen geldige operatie.\n";
    exit;
}

$getal1 = readline("Eerste getal? ");
if (!is_numeric($getal1)) {
    echo "Fout: geen getal.\n";
    exit;
}

$getal2 = readline("Tweede getal? ");
if (!is_numeric($getal2)) {
    echo "Fout: geen getal.\n";
    exit;
}

$getal1 = floatval($getal1);
$getal2 = floatval($getal2);

if ($operator == "+") {
    $resultaat = $getal1 + $getal2;
    echo "Het resultaat van $getal1 + $getal2 is: $resultaat\n";
} elseif ($operator == "-") {
    $resultaat = $getal1 - $getal2;
    echo "Het resultaat van $getal1 - $getal2 is: $resultaat\n";
} elseif ($operator == "%") {
    if ($getal2 == 0) {
        echo "Fout: Modulo met nul is niet toegestaan.\n";
        exit;
    }
    $resultaat = $getal1 % $getal2;
    echo "Het resultaat van $getal1 % $getal2 is: $resultaat\n";
}

?>