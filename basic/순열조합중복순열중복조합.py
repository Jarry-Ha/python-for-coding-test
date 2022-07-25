from itertools import permutations, combinations, product, combinations_with_replacement
data = ['A','B','C']
순열 = list(permutations(data,2))
조합 = list(combinations(data,2))
중복순열 = list(product(data,repeat=2))
중복조합 = list(combinations_with_replacement(data,2))
print(순열,조합,중복순열,중복조합, sep='\n')
