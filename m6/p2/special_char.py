'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    for i in len(str_input):
    	if str_input[i] >= "!" and str_input[i]  <= "*":
    	    str_input[i] = " "
    	else:
    	    str_input[i] == str_input[i]
    print(str_input)
if __name__ == "__main__":
    main()
