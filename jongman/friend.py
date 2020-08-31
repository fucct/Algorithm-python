from typing import List


class SolutionFriend:
    def pairCount(self, students: List[int], relations: List[List[int]]) -> int:
        if len(students) == 0 or len(students) == 1:
            return 0
        if len(students) == 2:
            for relation in relations:
                if relation == students:
                    return 1
            return 0

        result = 0
        for relation in relations:
            if students[0] in relation:
                newStudents = students[:]
                if relation[0] is students[0]:
                    if relation[1] not in students:
                        continue
                    else:
                        newStudents.remove(relation[0])
                        newStudents.remove(relation[1])
                else:
                    if relation[0] not in students:
                        continue
                    else:
                        newStudents.remove(relation[0])
                        newStudents.remove(relation[1])

                result += self.pairCount(newStudents, relations)
        return result
