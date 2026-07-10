class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        cycle_cnt = 1

        while cycle_cnt < len(students) + len(sandwiches):
            
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                cycle_cnt = 1
            else:
                students.append(students.pop(0))
                cycle_cnt += 1
        
        return len(students)


