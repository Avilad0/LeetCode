from typing import List,Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while students:
            if sandwiches[0]==students[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                if sandwiches[0] in students:
                    students.append(students.pop(0))
                else:
                    break    
        return len(students)

        # l = len(students)
        # skip_counter = 0
        # while l>0 and skip_counter!=l:
        #     if sandwiches[0]==students[0]:
        #         students.pop(0)
        #         sandwiches.pop(0)
        #         skip_counter=0
        #         l-=1
        #     else:
        #         students.append(students.pop(0))
        #         skip_counter+=1
        
        # return l


print(Solution().countStudents([1,1,0,0], [0,1,0,1])) #0

print(Solution().countStudents([1,1,1,0,0,1], [1,0,0,0,1,1])) #3
