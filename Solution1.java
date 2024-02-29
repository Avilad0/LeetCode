public class Solution1 {
    public static void main(String[] args){
        System.out.println(new Solution1().distributeCandies(3, 3));
    }
    
    public long distributeCandies(int n, int limit) {
        return rec(n, limit, 1,0);
    }

    private long rec(int n, int limit, int count, int sum){
        if (count==4){
            if(sum==n){
                return 1;
            } else {
                return 0;
            }
        }
        
        long r = 0;
        for (int i=0;i<=limit;i++){
            r+=rec(n,limit,count+1,sum+i);
        }

        return r;

    }


}