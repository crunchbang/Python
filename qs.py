def quicksort (lst):
	if lst == []:
		return []
	else:
		smallsorted = quicksort([x for x in lst[1:] if x <= lst[0]])
		bigsorted   = quicksort([x for x in lst[1:] if x >  lst[0]])
		return smallsorted + [lst[0]] + bigsorted
