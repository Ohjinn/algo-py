package 자바기초;

import java.util.Scanner;

public class 문자와_문자열_27866 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String word = in.next();
        int count = in.nextInt();

        System.out.println(word.charAt(count - 1));
    }
}
