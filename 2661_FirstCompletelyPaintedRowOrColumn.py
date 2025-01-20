class Solution:
    def firstCompleteIndex(self, arr, mat):
        mat_num_to_index = [None]*(len(arr)+1)

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                mat_num_to_index[mat[i][j]]= (i,j)

        set_rows = set([i for i in range(len(mat))])
        set_cols = set([i for i in range(len(mat[0]))])

        i=len(arr)-1
        while i>=0 and (len(set_rows)>0 or len(set_cols)>0):
            if mat_num_to_index[arr[i]][0] in set_rows:
                set_rows.remove(mat_num_to_index[arr[i]][0])
            if mat_num_to_index[arr[i]][1] in set_cols:
                set_cols.remove(mat_num_to_index[arr[i]][1])
            i-=1

        return i+1

# This sol has too the same time and storage complexity.    
# can also be solved using arr_num_to_index and checking which row or col gets filled first by using a counter, but need little extra space too like the above one.
# (or)
# can also be solved using arr_num_to_index and checking each element in mat one row-wise and once col-wise to check which row or col has the min of the max index in arr.
