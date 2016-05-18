def fib(n):
	global count
	count += 1
	print 'fib called with', n
	if n <= 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

count = 0
n = 6
result = fib(n)
print 'fib of', n, '=', result, 'number of calls =', count



#memoization:recaord the value the first time we calculate it, look it up subsequently (when we need it);
def fib1(n):
    memo = {1:1, 0:1}
    return fast_fib(n, memo)

def fast_fib(n, memo):
    global num_call
    num_call += 1
    if not n in memo:
        memo[n] = fast_fib(n-1, memo) + fast_fib(n-2, memo)
    return memo[n]

num_call = 0
n = 6
result = fib1(n)
print 'fib1 of', n, '=', result, 'number of calls =', num_call

#dynamic programming: table lookup

#optial substructure: Global optimal solution can be constructed from optimal solution to sub-problems
#Decision tree

def maxVal(w, v, i, a_w):
	global num_calls
	num_calls += 1
	if i == 0:
		if w[i] <= a_w: return v[i]
		else: return 0
	without_i = maxVal(w, v, i-1, a_w)
	if w[i] > a_w:
		return without_i
	else:
		with_i = v[i] + maxVal(w, v, i-1, a_w-w[i])
	return max(with_i, without_i)

weights = [1, 5, 3, 4]
vals = [15, 10, 9, 5]
result = maxVal(weights, vals, len(vals) - 1, 8)

def maxVal0(w, v, i, a_w):
	m = {}
	return fast_maxVal(w, v, i, a_w, m)

def fast_maxVal(w, v, i, a_w, m):
	global numCalls
	numCalls += 1
	try: return m[(i, aw)]
	except KeyError:
		if i == 0:
			if w[i] <= a_w:
				m[(i, a_w)] = v[i]
				return v[i]
			else:
				m[(i, a_w)] = 0
				return 0
		without_i = fast_maxVal(w, v, i-1, a_w, m)

		if w[i] > a_w:
			m[(i, a_w)] = without_i
			return without_i
		else:
			with_i = v[i] + fast_maxVal(w, v, i-1, a_w-w[i], m)
		result = max(with_i, without_i)
		m[(i, a_w)] = result
		return result

# Trading time for space.
# Don't be intimidated by exponential problem.
# Dynamic programming is broadly useful.
# Problem reduction.
