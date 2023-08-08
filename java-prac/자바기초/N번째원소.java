package 자바기초;

import java.util.Arrays;
class N번째원소 {
    public int[] solution(int[] num_list, int n) {
        return Arrays.copyOfRange(num_list, 0, n);
    }
}