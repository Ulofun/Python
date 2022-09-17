/// Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.

//Console.WriteLine("Введите трехзначное число: ");
//int number = Convert.ToInt32(Console.ReadLine());
//if(number >99 && number < 1000)
//{
//    int result = (number % 100) / 10;
//    Console.WriteLine("Вторая цифра данного числа равна: " + result);
//}
//else
//{
//    Console.WriteLine("Серега лох, введи трехзначное! ");
//}






int numfunction ( int num)
{
    int x = num * num;
    int result = x;
    return result;
}
Console.WriteLine("Введите трехзначное число: ");
int num = Convert.ToInt32(Console.ReadLine());
int result = numfunction(num);
if (num > 99 && num < 1000)
{
    Console.WriteLine("Результат равен " + result);
}
else
Console.WriteLine("Ошибка, введите трехзначное число!!!");