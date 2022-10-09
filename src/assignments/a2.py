
def bubble_sort(l, step):
    print("Bubble sort method:")
    count = 0
    ok = 0
    while ok == 0:
        ok = 1
        for i in range(0, len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                ok = 0
                count += 1
                if count % step == 0:
                    print("Step "+str(count)+": ", end="")
                    print(l)
    print("Sorted list: " + str(l))

print("Generate a list of `n` random natural numbers. Generated numbers must be between `0` and `100`.")

"""
The algorithm store the list via console input.
"""
n = int(input("n="))
lst = []
for i in range(0, n):
    lst.append(int(input("element " + str(i + 1) + ": ")))
"""
The algorithm makes a copy of the list to use for the first sort, reads the step number for the first sorting algorithm,
sorts the list copy using the first sorting algorithm and at the same time prints the partially sorted list after every 
'step' swaps, after that it prints the final sorted list.
"""
lst1 = lst
print("The first sorting method is bubble sort! ", end="")
step = int(input("Insert bubble sort step: "))
bubble_sort(lst1, step)
print("")

"""
The algorithm reads the step number for the second sorting algorithm, sorts the original list using the second sorting
algorithm and at the same time prints the partially sorted list after every 'step' swaps, after that it prints the final
sorted list
"""
print("The first sorting method is comb sort! ", end="")
step = int(input("Insert comb sort step: "))
comb_sort(lst, step)