fixed_cost,variable_cost,sale_cost = map(int,input().split())

# income = sale_cost - variable_cost
# break_even_point=int((fixed_cost/int(income)))+1
if variable_cost >= sale_cost :
    print(-1)
else:
    break_even_point=fixed_cost//(sale_cost-variable_cost)+1
    print(break_even_point)
