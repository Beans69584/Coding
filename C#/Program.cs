using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LogicGates
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("Enter a logic gate (AND, OR, XOR, NOT, NAND, NOR, XNOR)");
                string gate = Console.ReadLine().ToUpper();
                if (gate == "AND")
                {
                    Console.WriteLine("Enter the first input (1 or 0 or true or false or t or f)");
                    string input1 = Console.ReadLine().ToUpper();
                    Console.WriteLine("Enter the second input (1 or 0 or true or false or t or f)");
                    string input2 = Console.ReadLine().ToUpper();
                    if (input1 == "1" || input1 == "TRUE" || input1 == "T")
                    {
                        if (input2 == "1" || input2 == "TRUE" || input2 == "T")
                        {
                            Console.WriteLine("The output is 1");
                        }
                        else
                        {
                            Console.WriteLine("The output is 0");
                        }
                    }
                    else
                    {
                        Console.WriteLine("The output is 0");
                    }
                }
                else if (gate == "OR")
                {
                    Console.WriteLine("Enter the first input (1 or 0 or true or false or t or f)");
                    string input1 = Console.ReadLine().ToUpper();
                    Console.WriteLine("Enter the second input (1 or 0 or true or false or t or f)");
                    string input2 = Console.ReadLine().ToUpper();
                    if (input1 == "1" || input1 == "TRUE" || input1 == "T")
                    {
                        Console.WriteLine("The output is 1");
                    }
                    else
                    {
                        if (input2 == "1" || input2 == "TRUE" || input2 == "T")
                        {
                            Console.WriteLine("The output is 1");
                        }
                        else
                        {
                            Console.WriteLine("The output is 0");
                        }
                    }
                }
                else if (gate == "XOR")
                {
                    Console.WriteLine("Enter the first input (1 or 0 or true or false or t or f)");
                    string input1 = Console.ReadLine().ToUpper();
                    Console.WriteLine("Enter the second input (1 or 0 or true or false or t or f)");
                    string input2 = Console.ReadLine().ToUpper();
                    if (input1 == "1" || input1 == "TRUE" || input1 == "T")
                    {
                        if (input2 == "1" || input2 == "TRUE" || input2 == "T")
                        {
                            Console.WriteLine("The output is 0");
                        }
                        else
                        {
                            Console.WriteLine("The output is 1");
                        }
                    }
                    else
                    {
                        if (input2 == "1" || input2 == "TRUE" || input2 == "T")
                        {
                            Console.WriteLine("The output is 1");
                        }
                        else
                        {
                            Console.WriteLine("The output is 0");
                        }
                    }
                }
                else if (gate == "NOT")
                {
                    Console.WriteLine("Enter the input (1 or 0 or true or false or t or f)");
                    string input = Console.ReadLine().ToUpper();
                    if (input == "1" || input == "TRUE" || input == "T")
                    {
                        Console.WriteLine("The output is 0");
                    }
                    else
                    {
                        Console.WriteLine("The output is 1");
                    }
                }
                else if (gate == "NAND")
                {
                    Console.WriteLine("Enter the first input (1 or 0 or true or false or t or f)");
                    string input1 = Console.ReadLine().ToUpper();
                    Console.WriteLine("Enter the second input (1 or 0 or true or false or t or f)");
                    string input2 = Console.ReadLine().ToUpper();
                    if (input1 == "1" || input1 == "TRUE" || input1 == "T")
                    {
                        if (input2 == "1" || input2 == "TRUE" || input2 == "T")
                        {
                            Console.WriteLine("The output is 0");
                        }
                        else
                        {
                            Console.WriteLine("The output is 1");
                        }
                    }
                    else
                    {
                        Console.WriteLine("The output is 1");
                    }
                }
                else if (gate == "NOR")
                {
                    Console.WriteLine("Enter the first input (1 or 0 or true or false or t or f)");
                    string input1 = Console.ReadLine().ToUpper();
                    Console.WriteLine("Enter the second input (1 or 0 or true or false or t or f)");
                    string input2 = Console.ReadLine().ToUpper();
                    if (input1 == "1" || input1 == "TRUE" || input1 == "T")
                    {
                        Console.WriteLine("The output is 0");
                    }
                    else
                    {
                        if (input2 == "1" || input2 == "TRUE" || input2 == "T")
                        {
                            Console.WriteLine("The output is 0");
                        }
                        else
                        {
                            Console.WriteLine("The output is 1");
                        }
                    }
                }
                else if (gate == "XNOR")
                {
                    Console.WriteLine("Enter the first input (1 or 0 or true or false or t or f)");
                    string input1 = Console.ReadLine().ToUpper();
                    Console.WriteLine("Enter the second input (1 or 0 or true or false or t or f)");
                    string input2 = Console.ReadLine().ToUpper();
                    if (input1 == "1" || input1 == "TRUE" || input1 == "T")
                    {
                        if (input2 == "1" || input2 == "TRUE" || input2 == "T")
                        {
                            Console.WriteLine("The output is 1");
                        }
                        else
                        {
                            Console.WriteLine("The output is 0");
                        }
                    }
                    else
                    {
                        if (input2 == "1" || input2 == "TRUE" || input2 == "T")
                        {
                            Console.WriteLine("The output is 0");
                        }
                        else
                        {
                            Console.WriteLine("The output is 1");
                        }
                    }
                }
                else
                {
                    Console.WriteLine("Invalid gate");
                }
                Console.WriteLine("Do you want to continue? (y/n)");
                string cont = Console.ReadLine().ToUpper();
                if (cont == "Y")
                {
                    continue;
                }
                else
                {
                    break;
                }
            }
        }
    }
}