// Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
//456 -> 5
//782 -> 8
//918 -> 1

Console.WriteLine("Введите трехзначное число: ");
int nubmer = Convert.ToInt32(Console.ReadLine());
if (nubmer > 99 && nubmer < 1000)
{
    int result = (nubmer % 100) / 10;
    Console.WriteLine("Вторая цифра трехзначного числа получена и равна " + result);
}
else
{
    Console.WriteLine("Пожалуйста, введите трехзначное число!");
}
