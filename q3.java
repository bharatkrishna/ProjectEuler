/*
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*/
class q3 {

    public static int largestPrimeFactor(long number) {
        int i;

        for (i = 2; i <= number; i++) {
            if (number % i == 0) {
                number /= i;
                i--;
            }
        }

        return i;
    }

    /**
     * @param args
     */
    public static void main(String[] args) {
        System.out.println(largestPrimeFactor(13195));
        System.out.println(largestPrimeFactor(600851475143L));
    }
}