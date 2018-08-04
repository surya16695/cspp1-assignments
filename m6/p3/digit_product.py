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
    if int_input <0:
        int_input = abs(int_input)
    else:
    pro_duct = 1
    for  i in int_input:
    	pro_duct = (int_input%10)*pro_duct
    	int_input = int_input//10
    print(pro_duct)
if __name__ == "__main__":
    main()
