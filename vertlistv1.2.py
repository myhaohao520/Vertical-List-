#Python Script for printing list of names verticially (Replace the names with yours) V1.2

#1. The list of names I will be using in this example
#list = Carlo Pineda, Eduardo Covarrubias, Ting-Yueh Liu, Matt Dulog, Jian Hao Tang, Son Tran

#2. Put the list on names in '', run the code to split all the names into individual ''
#list = 'Carlo Pineda, Eduardo Covarrubias, Ting-Yueh Liu, Matt Dulog, Jian Hao Tang, Son Tran'
list = input('Enter the list of names here: ')
print(list.split(','))

#3. Copy the output of the previous code and put the list into []
#new_list = ['Carlo Pineda', ' Eduardo Covarrubias', ' Ting-Yueh Liu', ' Matt Dulog', ' Jian Hao Tang', ' Son Tran']
new_list = list

#4. Run this code to print the list of names vertically
#vertical_list = input("Enter the list above here: ")
print('\n'.join(new_list))

#Changelog:
#Removed the list of my name list from step 3
#Create a new variable called new_list to update the list variable from step 2
