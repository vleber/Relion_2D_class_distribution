'''
Script to automatically extract class distribution % from .star file
'''

# Import the Regular Expresion (re) Module which allows to search for a pattern
import re

'''
function to extract the %, check them, sort if necesary and format
'''
def writedistri_1():

    # create an empty list for adding the distribution values from the .star file:
    distri_list = []


    # define the pattern to search for (number of iteration doesnt matter):
    pattern = re.compile(r'(run_it\d{3}_classes.mrcs\s+)(0.\d+)')

    # open, read and close .star file:
    # TODO: account for cases where user chose differnt number of iterations
    starfile = open('run_it025_model.star', 'r')
    text = starfile.read()
    starfile.close()


    # find all patterns and write into list:
    matches_list = re.findall(pattern, text)


    #extract only the % numbers and convert to floats
    for item in matches_list:
        distri_list.append(float(item[1]))


    #convert distribution into % by multiplying with 100
    perc_list = [i *100 for i in distri_list]



    # in-build test to see if it has grabbed the right numbers - calculates the sum which should
    # be almost 100 (it won't be exactly 100 because of floating points)
    sum_perc_list = sum(map(float, perc_list))

    if sum_perc_list < 99.9 or sum_perc_list > 100.1:
        print('Problem! Class distributions do not add up to 100. Something is wrong!')
        print(sum_perc_list)

    # ask user if classes are ordered
    order = ''
    while True:
        order = str(input('Are the classes ordered? (y/n)')).lower().strip()
        if order == 'y' or order == 'n':
            break

        print('Please answer either "y" or "n".')


    #order the distributions from biggest to smallest IF necessary:
    if order == 'y':
        perc_list.sort(reverse=True)


    #convert to one decimal:
    distribution = []
    for i in perc_list:
        distribution.append("{:.1f}".format(i))

    #add a % to each number
    final_list = []
    for i in distribution:
        final_list.append(i + '%')


    # print the list without quotes and comma to be used as it is
    print(*final_list, sep = ' ')


writedistri_1()
