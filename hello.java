import java.util.*;
class hello{
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);
        int num;
        System.out.print("Enter the number :");
        num=s.nextInt();
        System.out.println();
        for(int i=1;i<=num;i++){
            for(int space=num-i;space>0;space--){
                System.out.print(" ");
            }
            for(int j=1;j<=2*i-1;j++){
            System.out.print("*");
            }
            System.out.println();
        }
    }
}