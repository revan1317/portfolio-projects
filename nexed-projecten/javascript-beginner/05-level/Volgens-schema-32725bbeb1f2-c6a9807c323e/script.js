const [groenteInterval, broodInterval, vloerInterval] = process.argv.slice(2).map(Number);
const openuren = 8;
const dichturen = 20;
const totaaluren = dichturen - openuren;
const agenda = [];
let vrij = 0;

for (let hour = openuren; hour < dichturen; hour++) {
    const currentTasks = [];

    if ((hour - openuren) % groenteInterval === 0) {
        currentTasks.push("versheid van groenten en fruit checken");
    }
    if ((hour - openuren) % broodInterval === 0) {
        currentTasks.push("nieuw brood bakken");
    }
    if ((hour - openuren) % vloerInterval === 0) {
        currentTasks.push("vloer schoonmaken");
    }

    if (currentTasks.length === 0) {
        agenda.push(`${hour}:00 - vrij uur`);
        vrij++;
    } else {
        agenda.push(`${hour}:00 - ${currentTasks.join(", ")}`);
    }
}

console.log("Dagrooster:");
console.log("-------------------");
agenda.forEach(entry => console.log(entry));
console.log("-------------------");
console.log(`Aantal vrije uren: ${vrij}`);