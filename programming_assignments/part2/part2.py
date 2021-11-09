import sys
from bool_solver import *

sys.path.append("../part0")
from client_csv import *

'''

  [ Programming assignment: part two (2) ]
    For this assignment you will create a program that processes the dictionary
    from the programming assignment zero (0) and solves (evaluates) the boolean
    expression that is given in the dictionary.

    For example:
     For the example dictionary below:
     {'qid': 39, 
      'category': 2, 
       'level': 2, 
       'problem': 'C and (A or B)', 
       'description': 'A=0,B=1,C=1', 
       'todo': 'evaluate_bool'}

      Your program will have to find the truth value for the given problem 
      C and (A or B)  given that A=0, B=1 and C=1.


    Your code will have to inspect the following two dictionary keys in 
    order to be able to correctly evaluate the boolean expression: 
         i) 'problem'
                The value that is associated with this key specifies the
                actual boolean expression given to us as a string.

        ii) 'description'
                The value that is associated with this key specifies the
                truth values for each of our boolean expression variables.


     Note: all of the values that are associated with the 'problem' and
           'description' dictionary keys are strings.
   

    Submit on GitHub:
    Your final code submission should consist of a single bool_solver.py
    file that you will push into your cs260data repository on GitHub under the 
    programming_assignments/part2 directory.



    Specifications:
    * Your bool_solver.py should include the definition of the 
      BoolEvalSimple class such that:
      * The constructor of the BoolEvalSimple class:
        * Initializes the instance variable named row (self.row) to value None.
         
      * The set_row() method of the BoolEvalSimple class:
        * Has a parameter named row. 
        * Assigns the row parameter to self.row, meaning this method receives the
          dictionary from programming assignment part 0 as argument and then 
          assigns it to the self.row instance variable.

         
      * The bool_eval() method:
        * Inspects the dictionary under self.row and evaluates the boolean expression. 
          The correct result of the evaluation should be returned by the bool_eval() 
          method as a string consisting of either '0' or '1'.
        
        * Useful hints to consider:    
            * For the value that is associated with the 'problem' key of the dictionary:
              https://realpython.com/python-eval-function/

            * For the value that is associated with the 'description' key of the dictionary:
              https://www.pythonpool.com/python-string-to-variable-name

 
      * Finally, you can use the test cases below to check your work. Think about 
        additional test cases, but keep in mind that for simplicity we are using the 
        standard Python logical operators: not, and, or.



    *** prep-work***
    In order to obtain the boolean expression you will have to do the following
    outside of your class definition (as shown in the example below):
        1) Obtain the dictionary by using the get() method from the 
           programming  assignment zero (0), use category 2 and level 1
           or a specific qid. 
        2) Use the set_row() method of your BoolEvalSimple class to 
           make the dictionary available to the bool_solver() method.

        Note: Do not modify the dictionary, for this assignment all information is 
              already present in the dictionary.
 

'''

def print_result(td,result):
    print('Evaluating:',td['problem'] + ', with', td['description'], " yields: ", str(result))

# objects
bool_evaluator = BoolEvalSimple()
question = Questions(location = '../part0')


# 
td = question.get(qid = 34) # 34,2,1,A,"A=1",evaluate_bool
bool_evaluator.set_row(td)
correct_answer = '1'
result = bool_evaluator.bool_eval()
print_result(td,result)
assert(result == correct_answer), 'failed on ' + str(td['qid']) # indicate that it failed on specific qid

# 
td = question.get(qid = 35) # 35,2,1,A or B,"A=1,B=0",evaluate_bool
bool_evaluator.set_row(td)
correct_answer = '1'
result = bool_evaluator.bool_eval()
print_result(td,result)
assert(result == correct_answer), 'failed on ' + str(td['qid']) # indicate that it failed on specific qid

# 
td = question.get(qid = 36) # 36,2,1,A and B,"A=1,B=0",evaluate_bool
bool_evaluator.set_row(td)
correct_answer = '0'
result = bool_evaluator.bool_eval()
print_result(td,result)
assert(result == correct_answer), 'failed on ' + str(td['qid']) # indicate that it failed on specific qid

# 
td = question.get(qid = 37) # 37,2,1,not(A or B),"A=0,B=1",evaluate_bool
bool_evaluator.set_row(td)
correct_answer = '0'
result = bool_evaluator.bool_eval()
print_result(td,result)
assert(result == correct_answer), 'failed on ' + str(td['qid']) # indicate that it failed on specific qid


# 
td = question.get(qid = 38) # 38,2,1,w or x and y or (not z),"w=0,x=1,y=0,z=0",evaluate_bool
bool_evaluator.set_row(td)
correct_answer = '1'
result = bool_evaluator.bool_eval()
print_result(td,result)
assert(result == correct_answer), 'failed on ' + str(td['qid']) # indicate that it failed on specific qid


# 
td = question.get(qid = 39) # 39,2,1,C and (A or B),"A=0,B=1,C=1",evaluate_bool
bool_evaluator.set_row(td)
correct_answer = '1'
result = bool_evaluator.bool_eval()
print_result(td,result)
assert(result == correct_answer), 'failed on ' + str(td['qid']) # indicate that it failed on specific qid


# 
td = question.get(qid = 42) # 19,1,1,1110,bin,
bool_evaluator.set_row(td)
correct_answer = '1'
result = bool_evaluator.bool_eval()
print_result(td,result)
assert(result == correct_answer), 'failed on ' + str(td['qid']) # indicate that it failed on specific qid



