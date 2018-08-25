'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''
# def dictionary_1(dictionary):
#     for word in dictionary.keys():
#     	dictionary[word] = n
#     	s = '#'
#     	print(n*s)
	 
def frequency_graph(dictionary):
    for word in dictionary.keys():
    	print(word, '-', dictionary[word]*"#")


def main():
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
