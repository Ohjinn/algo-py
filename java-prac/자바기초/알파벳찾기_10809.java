package 자바기초;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class 알파벳찾기_10809 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] alphabetCounter = new int[26];

        String target = in.next();
        for(int i = 0; i < target.length(); i++){
            if(alphabetCounter[target.charAt(i) - 97] == 0) {
                alphabetCounter[target.charAt(i) - 97] = i + 1;
            }
        }

        for(int i = 0; i < alphabetCounter.length; i++) {
            if(alphabetCounter[i] == 0) System.out.print(-1 + " ");
            else System.out.print(alphabetCounter[i] - 1 + " ");
        }
    }
}
