class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        one_c = sum(students)
        zero_c = len(students) - one_c

        fed_count = 0
        for i in range(len(sandwiches)):

            if sandwiches[i] == 1:
                if one_c > 0:
                    one_c -= 1
                    fed_count += 1
                else:
                    break

            elif sandwiches[i] == 0:
                if zero_c > 0:
                    zero_c -= 1
                    fed_count += 1
                else:
                    break
            
        return len(students) - fed_count