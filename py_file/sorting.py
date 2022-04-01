class Sort:
    rec_n = 0

    def merge_sort(self, arr):
        arr_len = len(arr)
        if arr_len < 2:
            return arr

        mid_index = (arr_len + 1) // 2
        l_arr = self.merge_sort(arr[:mid_index])
        r_arr = self.merge_sort(arr[mid_index:])

        print(l_arr, r_arr)
        return self.merge(l_arr, r_arr)

    def merge_sort_3_partition(self, arr):
        arr_len = len(arr)
        if arr_len < 2:
            return arr

        arr_len_div_by_3 = arr_len // 3

        a1 = self.merge_sort_3_partition(arr[: arr_len_div_by_3])
        a2 = self.merge_sort_3_partition(
            arr[arr_len_div_by_3: 2 * arr_len_div_by_3])
        a3 = self.merge_sort_3_partition(
            arr[2 * arr_len_div_by_3:])

        print(a1, a2, a3)
        return self.merge_3_input(a1, a2, a3)

    def merge(self, l_arr, r_arr):
        l_n = len(l_arr)
        r_n = len(r_arr)
        n = l_n + r_n
        result = [0]*n

        i = j = 0
        for k in range(n):
            if i == l_n or j == r_n:
                break

            if l_arr[i] < r_arr[j]:
                result[k] = l_arr[i]
                i += 1
            else:
                result[k] = r_arr[j]
                j += 1

        if i < l_n:
            result[k:] = l_arr[i:]
        elif j < r_n:
            result[k:] = r_arr[j:]
        return result

    def merge_3_input(self, a, b, c):
        return self.merge(self.merge(a, b), c)


arr = list(map(int, input().split()))
a = Sort().merge_sort(arr)
print()
# [1, 3, 5, 8, 9], [0, 2, 4, 6, 7], [1, 9])
b = Sort().merge_sort_3_partition(arr)
print(b)
print(a)
