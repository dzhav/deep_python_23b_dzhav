class CustomList(list):
    def __str__(self):
        return f"{list(self)} ({sum(self)})"

    def __add__(self, other_list):
        if isinstance(other_list, list):
            other_list = CustomList(other_list)
        ans = CustomList()
        for i in range(0, max(len(self), len(other_list))):
            if i < len(self) and i < len(other_list):
                ans.append(self[i] + other_list[i])
            elif i < len(self):
                ans.append(self[i])
            else:
                ans.append(other_list[i])
        return ans

    def __radd__(self, other_list):
        return self + other_list

    def __sub__(self, other_list):
        if isinstance(other_list, list):
            other_list = CustomList(other_list)
        ans = CustomList()
        for i in range(0, max(len(self), len(other_list))):
            if i < len(self) and i < len(other_list):
                ans.append(self[i] - other_list[i])
            elif i < len(self):
                ans.append(self[i])
            else:
                ans.append(-other_list[i])
        return ans

    def __rsub__(self, other_list):
        if isinstance(other_list, list):
            other_list = CustomList(other_list)
        ans = CustomList()
        for i in range(0, max(len(self), len(other_list))):
            if i < len(self) and i < len(other_list):
                ans.append(other_list[i] - self[i])
            elif i < len(other_list):
                ans.append(other_list[i])
            else:
                ans.append(-self[i])
        return ans

    def __eq__(self, other_list):
        if isinstance(other_list, list):
            other_list = CustomList(other_list)
        return sum(self) == sum(other_list)

    def __ne__(self, other_list):
        if isinstance(other_list, list):
            other_list = CustomList(other_list)
        return sum(self) != sum(other_list)

    def __gt__(self, other_list):
        if isinstance(other_list, list):
            other_list = CustomList(other_list)
        return sum(self) > sum(other_list)

    def __ge__(self, other_list):
        if isinstance(other_list, list):
            other_list = CustomList(other_list)
        return sum(self) >= sum(other_list)

    def __lt__(self, other_list):
        if isinstance(other_list, list):
            other_list = CustomList(other_list)
        return sum(self) < sum(other_list)

    def __le__(self, other_list):
        if isinstance(other_list, list):
            other_list = CustomList(other_list)
        return sum(self) <= sum(other_list)
