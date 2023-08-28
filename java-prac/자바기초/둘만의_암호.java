package 자바기초;

public class 둘만의_암호 {
    private String solution(String s, String skip, int index) {
        String alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz";
        StringBuilder answer = new StringBuilder();
        for(int i = 0; i < skip.length(); i++) {
            alphabet = alphabet.replace(Character.toString(skip.charAt(i)), "");
        }
        for(int i = 0; i < s.length(); i++) {
            int now = alphabet.indexOf(s.charAt(i));
            answer.append(alphabet.charAt(now + index));
        }
        return answer.toString();
    }

    public static void main(String[] args) {
        둘만의_암호 T = new 둘만의_암호();
        System.out.println(T.solution("aukks", "wbqd", 5));
    }
}
