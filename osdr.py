import pandas as pd
import sys
from tabulate import tabulate
#from bs4 import BeautifulSoup

# display formatting
pd.set_option('display.max_colwidth', None)

# open json data file
f = open('osdr_short.json')
osdr = pd.read_json(f)

# make a dataframe df from json
df = pd.DataFrame(osdr)
#len(df)

# make a subset dataframe df2 from df, just for names and index
df2 = df.drop(["description", "id"], axis="columns" )
#df3 = df2.style.set_properties(**{'text-align': 'left'})

#print(f"df2.size {df2.size}")

# index for listing the hw names
rangeint = 0

# show the next ten hardware items from the name list
def continuelist(rangeint):
    #print(f"continuelist {rangeint} {df2.size}")

    for rangeint in range(rangeint, rangeint+10, 10):
        #print(df2.iloc[rangeint:rangeint+10])
        df_set = df2.iloc[rangeint:rangeint+10]
        #df3 = df_set.style.set_properties(**{'text-align': 'left'})
        print(df_set)
    initial_osdr(rangeint)

# showing hardware item details by their index number
# also invalid commands are handled by this function
def show_hw_details(inputcommand):
    #print(f"show_hw_details {inputcommand}")
    try:
        hwnumber = int(inputcommand)
        #print(hwnumber)
        if hwnumber >= 0 and hwnumber <= df2.size-1:
            selected_df = pd.DataFrame(df.iloc[hwnumber])
            #styled_df = selected_df.style.set_properties(**{'text-align': 'left'})
            print(selected_df)
            #print( tabulate(selected_df, headers='keys', maxcolwidths=[25, 60]) )
            #display( tabulate(selected_df, headers='keys', maxcolwidths=[25, 60]) )
            initial_osdr(rangeint)
        else:
            print("Wrong number")
    except Exception as e:
        print("Invalid command:")
        print(e)
        initial_osdr(rangeint)
        continuelist(rangeint)
    return 1

# requesting input
def initial_osdr(rangeint):
    #clear_output()
    try:
        print(f"\nEnter a number (0-{df2.size-1}) for details\nPress Enter to continue list\na - show all\nq - quit application:")
        inputcommand = input("")
        #print(inputcommand)

        # if the user pressed Enter, the next set of ten hardware names are shown
        # after the whole list is shown, it is started back from the beginning (rangeind = 0)
        if inputcommand == "":
            rangeint = rangeint + 10
            if rangeint < df2.size-1:
                #print(f"alkuun {rangeint}")
                #os.system(cls)
                continuelist(rangeint)
            else:
                rangeint = 0
                #os.system(cls)
                continuelist(rangeint)
        # input 'q' quits the application
        elif inputcommand == "q":
            sys.exit("Quitting")
        # input 'a' shows the full hardware list with descriptions
        elif (inputcommand == "a"):
            print( tabulate(df, headers='keys', tablefmt='grid', maxcolwidths=[None, 8, 15, 40]) )
            #display(df)
            initial_osdr(rangeint)
        # other commands
        else:
            #print("other commands")
            show_hw_details(inputcommand)
    except Exception as e:
        print("We got error:")
        print(e)

print("NASA Open Science Data Repository Hardeware browser")
# show the first ten hardware items from the name list and the user prompt
continuelist(rangeint)
initial_osdr(rangeint)