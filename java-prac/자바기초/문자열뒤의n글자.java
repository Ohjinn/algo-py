package 자바기초;

public class 문자열뒤의n글자 {
    public String solution(String my_string, int n) {
        String answer = my_string.substring(my_string.length() - n);
        return answer;
    }
}
