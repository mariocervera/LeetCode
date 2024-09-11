class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


def getImportance(employees, id):
    employee_dict = {emp.id: emp for emp in employees}

    def dfs(employee):
        res = employee.importance
        for subordinate in employee.subordinates:
            res += dfs(employee_dict[subordinate])
        return res

    return dfs(employee_dict[id])


print(getImportance(employees=[Employee(1, 5, [2, 3]),
                               Employee(2, 3, []),
                               Employee(3, 3, [])],
                    id=1))  # 11

print(getImportance(employees=[Employee(1,2,[5]),
                               Employee(5,-3,[])],
                    id=5))  # -3
