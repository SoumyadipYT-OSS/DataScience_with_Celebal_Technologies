using System;

public class Calculator {
    public double Add(double a, double b) => a + b;
    public double Subtract(double a, double b) => a - b;
    public double Multiply(double a, double b) => a * b;
    public double Divide(double a, double b) => a / b;
    public double Modulo(double a, double b) => a % b;
    public double Power(double a, double b) => Math.Pow(a, b);
    public double SquareRoot(double a) => Math.Sqrt(a);
    
}