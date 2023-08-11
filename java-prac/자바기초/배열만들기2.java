package 자바기초;

import java.util.ArrayList;
import java.util.Arrays;

public class 배열만들기2 {
    public int[] solution(int l, int r) {
        ArrayList<Integer> answer = new ArrayList();
        for(int i = l; i <= r; i++) {
            String tmp = Integer.toString(i);
            int count = 0;
            for (int j = 0; j < tmp.length(); j++) {
                if(tmp.charAt(j) == 48 || tmp.charAt(j) == 53) {
                    count ++;
                }
            }
            if(count == tmp.length()) {
                answer.add(i);
            }
        }
        int[] result = answer.stream().mapToInt(i -> i).toArray();
        int[] empty = new int[]{-1};
        if(result.length == 0) return empty;
        else return result;
    }
}
