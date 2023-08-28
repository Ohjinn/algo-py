package 자바기초;

import java.util.Scanner;
import java.util.StringTokenizer;

public class 단어의개수_1152 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int count = 0;
        String nextString = in.nextLine();
        String[] strings = nextString.split(" ");
        if (strings.length == 0) System.out.println(1);
        else System.out.println(strings.length);

        String S = in.nextLine();
        in.close();

        // st 에 공백을 기준으로 나눈 토큰들을 st 에 저장한다
        StringTokenizer st = new StringTokenizer(S," ");

        // countTokens() 는 토큰의 개수를 반환한다
        System.out.println(st.countTokens());


    }
}

