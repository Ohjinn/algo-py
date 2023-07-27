package 자바기초;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 문자열_반복_2675 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] counter = new String[]{};

        int number = Integer.parseInt(br.readLine());

        for(int i = 0; i < number; i++) {
            String[] line = br.readLine().split(" ");

            int repeat_times = Integer.parseInt(line[0]);

            for(int j = 0; j < line[1].length(); j++) {
                for(int k = 0; k < repeat_times; k++) {
                    System.out.print(line[1].charAt(j));
                }
            }
            System.out.println();
        }

    }
}
