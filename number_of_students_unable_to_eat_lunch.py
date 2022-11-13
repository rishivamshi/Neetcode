class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = 0
        l = len(students)
        while(1):
            sandwich = sandwiches.pop(0)
            # print("looop")
            if sandwich not in students:
                return len(students)
            if(students[0] == sandwich):
                students.pop(0)
                # print('match')
                # print(students)

                # print(sandwiches)
            else:
                student = students.pop(0)
                students.append(student)
                temp = [sandwich] + sandwiches
                sandwiches = temp
                # print('misss')
                # print(students)

                # print(sandwiches)
                
                count+=1
            if (len(sandwiches) == 0):
                return len(students)
        return len(students)
