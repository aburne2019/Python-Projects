# Descriptive Sequencing
## Used to describe a number

# create a function as def total_list(list,value)
#                           list.append(value)
# this can be used to keep a running tab of the final values found

# create an option at beginnging to either have user input their own number and print full results or user selects to view all final outputs and total number
#   create a function that does the iterations, call the function for both user input and all values

def ds(number):
    
    number_string = str(number) # convert to string for easier use
    index1 = range(1,10) # sets range of values 1 to 9 for counting
    ds_string = "" # sets up a blank string
    print(number_string) # prints initial value in the sequence

    total_list = []
    
    c = 1
    list_counter = 0
    while c != 0:

        for i in index1:
            i_string = str(i) # convert index value to string
            num_count = number_string.count(i_string) # count number of appearances of number i
            if num_count >= 1:
                ds_string = ds_string + str(num_count) + str(i) # adds count value and number to output string
            #print(i)
        print(ds_string)

        if ds_string == number_string: # check to see if new value equals old value: i.e. and ends sequence
            print('This is a hard value sequence.')
            c = 0
        elif ds_string in total_list: # checks for repearing values: i.e. 1 then 2 then 1 then 2 and so on and ends sequence
            print('This is a repeating value sequence.')
            c = 0
        else:
            number_string = ds_string
            ds_string = ""
            total_list.append(number_string)
            list_counter += 1
            
    return ds_string

number = int(input("Please enter a number for descriptive sequencing: "))
if number < 1 or number > 999999999:
    print('You have entered an invalid number. Please enter a number between 1 and 999,999,999.')
elif '0' in str(number): # add a statement here for if the number contains a 0 print out an error
    print('Please enter an integer that does not contain a 0.')
else:
    ds(number)

# now I need to add a loop that keeps doing this process as long as the number does not equal the number before it