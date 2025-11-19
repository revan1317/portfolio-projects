Console.WriteLine("Wat is het wachtwoord?");
string ingevoerdWachtwoord = Console.ReadLine();

if (ingevoerdWachtwoord == "baas")
{
    Console.WriteLine("Totale toegang");
}
else if (ingevoerdWachtwoord == "medewerker")
{
    Console.WriteLine("Gedeeltelijke toegang");
}
else
{
    Console.WriteLine("Geen toegang");
}