import pandas as pd 
import argparse
import sys

fields = ['ID','forename','middle name', 'surname','department']

def generate_list_of_usernames(input_file):    
    df = pd.read_csv(input_file, sep=':', names=fields)
    usernames = []

    handle_empty = df['middle name'].isnull()

    for i in range(len(handle_empty)):       
        if handle_empty[i] == True:
            # GET FIRST CHAR FROM [forname] IF DONT CONTAIN [middle name]
            username = df['forename'][i][0] + df['surname'][i]                    
            username = username[:8].lower() 
            if username in usernames:
                username = username + '1'

            usernames.append(username)

        else:
            # GET FIRST CHAR FROM [forname] IF CONTAIN [middle name]
            username = df['forename'][i][0] + df['middle name'][i][0] + df['surname'][i]
            username = username[:8].lower()
            usernames.append(username)    
    return usernames        



if __name__ == '__main__': 
    try:   
        parser = argparse.ArgumentParser(description=''' Program for generate a list of usernames. The input data is stored in one or more text files with
        encoding utf-8. Each line in the input file is a record about one user and includes: ID, forename, middle
        name (optional), surname and department. Items in the line are separated by colons.
        There is only one output file with all records together. Each line in the output file is a record about one
        user and includes: ID, generated username, forename, middle name (optional), surname and department. ''')

        parser.add_argument('-o', '--output', nargs=2, metavar=('[output file]', '[input file]'))                   
        args=parser.parse_args()
        output, input = args.output        
    except:
        parser.print_help()
        sys.exit(0)      

    usernames = generate_list_of_usernames(input)

    df = pd.read_csv(input, sep=":", names=fields)
    df.insert(1, 'username', usernames)
    df.to_csv(output, sep=':', index=False)





    







