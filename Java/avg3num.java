import java.util.Scanner;
class avgnum {
    public static void main(String[] args) {
        int a,b,c;
        Scanner sc = new Scanner(System.in);
           System.out.println("enter the three numbers");
        a=sc.nextInt();
        b=sc.nextInt();
        c=sc.nextInt();
        
        float avg=((a+b+c)/3);
        System.out.println("the avg of three numbers is "+avg);
    }
}
