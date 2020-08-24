# class Solution:
#def shortestWay(self, source: str, target: str) -> int:
#Example: 1
# source = "abc" target = "abcbc"
# 1. break down target into smaller subsequences that we could find directly with the source
# 2. or source -> target
# - break down target to be subsequences of length(source)
# - target -> abc bc
# - compare to source and chcek if subsequences are in source
# - compare(target(abc) with source(abc)) == true
# - compare(target(ab) with suorce(ab)) == true
#return min = 2
#Example:2
#Input: source = "xyz", target = "xzyxz"
# - break down target = xzy, xz
# - compare to source and check 
# - compare(target(xzy) to source(xyz)) == false
# - compare(target(xz) to source(xyz)) == false
# - iterate through target then iterate through source (double for loop)

#Brute Force:
#double iteration through target first then through source, compare one value by one value...
# source = "abc" target = "abcbc"
#example 1:
	#iter 1:
	#posAns = "a"
	#iter 2:
	#posAns = "ab"
	#iter 3:
	#posAns = "abc" if 1 <= length(posAns) <= length(source)
	#listposAns = [a, ab, abc]
#example 2:
source = "xyz"
target = "xzyxz"
#iter 1:			iter 2:				iter3:
#	posAns = "x"		posAns = "x"		posAns = "xz"
#	listposAns = []
notConcat = False
posAns = ""
ans = 0
listposAns = []
count = 0
for itar in target:
	for jsource in source:
		count += 1
		if 1 <= len(posAns) <= len(source) and notConcat:
			listposAns.append(posAns)
		elif itar == jsource and count == len(source):
			count = 0
			posAns = ""
		elif itar == jsource:
			posAns += jsource
			notConcat = True
			source = source[count:]					
			break
		else:
			notConcat = False

# Solution sol
# sol.shortestWay( source = "abc" , target = "abcbc")