import java.util.Scanner;
public class largestnum {
    public static void main(String[] args) {
    float a,b,c;
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the 1st number");
    a=sc.nextFloat();
    System.out.println("Enter the 2nd number");
    b=sc.nextFloat();
    System.out.println("Enter the 3rd number");
    c=sc.nextFloat();
    if(a>=b && a>=c)
    System.out.println(a+" is the largest number");
    else if(b>=a && b>=c)
    System.out.println(b+" is the largest number");
    else
    System.out.println(c+" is the largest number");
    }
}

