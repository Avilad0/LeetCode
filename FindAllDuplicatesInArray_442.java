import java.util.ArrayList;
import java.util.List;

public class FindAllDuplicatesInArray_442 {
    public static void main(String[] args) {
        System.out.println(new Solution2().findDuplicates(new int[]{39,31,8,14,14,38,5,15,29,49,18,6,30,47,8,35,2,17,6,10,29,46,41,48,1,36,5,28,46,39,7,47,18,42,17,11,36,45,21,33,24,10,24,50,25,16,9,12,11,25}));
    }
}

class Solution2 {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> r =  new ArrayList<Integer>();
        long b= 0b0;
        for(long n:nums){
            b=(b^(0b1<<n));
            if(((b>>n)&1) == 0){
                r.add((int)n);
            }
        }
        return r;
    }
}