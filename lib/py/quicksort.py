import random

def partition_3way(a, l, r):
	p = random.randint(l, r)
	x = a[p]
	a[l], a[p] = a[p], a[l] 
	
	e = l
	g = l + 1
	for i in range(l + 1, r + 1):
		if a[i] > x:
			continue
		elif a[i] == x:
			a[i] = a[g]
			a[g] = x
			g += 1
		else:
			y = a[i]
			a[i] = a[g]
			a[g] = x
			a[e] = y
			g += 1
			e += 1
			
	return e - 1, g
    
def sort_3way(a, l=0, r=None):
	r = len(a) - 1 if r is None else r
	if l < r:
		p1, p2 = partition_3way(a, l, r)
		sort_3way(a, l, p1)
		sort_3way(a, p2, r)

######################################

def partition(a, l, r):
	p = l
	for i in range(l, r):
		if a[i] < a[r]:
			a[i], a[p] = a[p], a[i]
			p += 1
	a[p], a[r] = a[r], a[p]
	return p
    
def sort(a, l=0, r=None):
	r = len(a) - 1 if r is None else r
	if l < r:
		p = partition(a, l, r)
		sort(a, l, p - 1)
		sort(a, p + 1, r)
