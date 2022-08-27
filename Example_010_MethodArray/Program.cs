Console.WriteLine("Введите первое число: ");
int number1 = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите второе число: ");
int number2 = Convert.ToInt32(Console.ReadLine());
int maxnumber = 0;

if (number1 > number2)
{
    maxnumber = number1;
    Console.Write("Большее число = " + maxnumber);
}

else if (number1 == number2)
{
    Console.Write("Числа равны ");
}
else 
{
    maxnumber = number2;
    Console.Write("Большее число =" + maxnumber);
}
