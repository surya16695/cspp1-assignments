'''
Given a  number int_input, find the product of all the digits
example: 
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    best_1 = str(int_input)
    pro_duct = 1
    i = 0
    if int_input <0:
        int_input = -1*(int_input)
    else:
        for  i in best_1:
    	    pro_duct = i *pro_duct
    print(pro_duct)
if __name__ == "__main__":
    main()
