import java.util.Scanner;
class palindrome {
    public static void main(String[] args) {
        String s;
        int i=0;
        Scanner sc = new Scanner(System.in);
          s=sc.nextLine();
         String g="";
         for(int i=0;i<s.length();i++){
             g=s.charAt(i)+g;
         }
         if(s.equalsIgnoreCase(g)){
             System.out.println("Palindrome");
         }
         else{
             System.out.println("Not Palindrome");
         }
    }
}
