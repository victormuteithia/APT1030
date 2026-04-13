public class Practice {
    public static void main(String[] args) {
        // System.out.println("Hello, World!");
        int score = 100;
        if (score >= 50) {
            System.out.println("Pass!");
        } else {
            System.out.println("Fail");
        }
        System.out.println(add(2, 4));
    }
    
    public static int add(int a, int b) {
        // System.out.println(a + b);
        return a + b;
    }
}