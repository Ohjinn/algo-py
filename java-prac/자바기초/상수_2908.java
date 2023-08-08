package 자바기초;

import java.util.Scanner;

import static java.lang.Integer.parseInt;

public class 상수_2908 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String line = in.nextLine();
        String[] numbers = line.split(" ");
        StringBuffer targetNumber1 = new StringBuffer(numbers[0]);
        StringBuffer targetNumber2 = new StringBuffer(numbers[1]);
        int first = Integer.parseInt(targetNumber1.reverse().toString());
        int second = Integer.parseInt(targetNumber2.reverse().toString());
        if(first > second) System.out.println(first);
        else System.out.println(second);
    }
}
