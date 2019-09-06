#https://www.spoj.com/problems/ONP/
import string

for t in range(int(input())):
    expression = list(input())
    priority_dict = {'+':1,
                     '-':2,
                     '*':3,
                     '/':4,
                     '^':5}
    stack = []
    symbol_classifier = {"brackets":['(',')'],
                         "operator":['+','-','*','/','^'],
                         "operands": list(string.ascii_lowercase)}
    final_string = ""
    for symbol in expression:
        if(symbol_classifier.get("brackets").count(symbol) == 1):
            if(symbol == '('):
                stack.append(symbol)
            elif(symbol == ')'):
                temp = 'a'
                while(temp!='('):
                    temp = stack.pop()
                    if(symbol_classifier.get("brackets").count(temp) != 1):
                        final_string += temp
        elif(symbol_classifier.get("operator").count(symbol) == 1):
            top = stack[len(stack)-1]
            curr_sym_priority = priority_dict.get(symbol)
            top_sym_priority = priority_dict.get(top)
            if(symbol_classifier.get("brackets").count(top) == 1 or curr_sym_priority>top_sym_priority):
                stack.append(symbol)
            else:
                while(curr_sym_priority<top_sym_priority):
                    temp1 = stack.pop()
                    if(symbol_classifier.get("brackets").count(temp1) != 1):
                        final_string += temp1
                    top_sym_priority = priority_dict.get(stack[len(stack)-1])
        elif(symbol_classifier.get("operands").count(symbol) == 1):
            final_string += symbol
    print(final_string)
        
