package 자바기초;

import java.math.BigInteger;
import java.util.Scanner;

public class 숫자의합_11720 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int count = in.nextInt();
        String number = in.next();
        in.close();

        int sum = 0;

        for(int i = 0; i < count; i++) {
            sum += Character.getNumericValue(number.charAt(i));
        }
        System.out.println(sum);
    }
}
