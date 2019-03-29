#  Author : SNEH DESAI.
#  Description : This Code is Designed to
#                   generate and equivalent HTML code
#                   for the chosen CSV file.

# .csv TO HTML CONVERTER


myFile = open('example.csv', 'r')    # myFile is the Object of File

no_of_rows = myFile.read().splitlines()     # This no_of_rows variable will give the rows of .csv file

# print(no_of_rows)
print("<html>")
print("<head>")
print("<title> FILE NAME CAN BE PRINTED HERE  </title>")
print("</head>")
print("<body>")
print("<table border = '1' >")

for i in range(0, len(no_of_rows), 1):       # This loop is to show all the rows of the file
    print("<tr>")
    one_line = no_of_rows[i]                # This Variable would print one whole row
    no_cells = one_line.split(',')          # This variable would print the value of every individual cell

#   print(no_cells[0])          This would Print the value of the whole first column

    for j in range(0,len(no_cells),1):      # This Loop is to print the every individual value
        if i == 0:
            print("<th>")
            print(no_cells[j])
            print("</th>")
        else:
            print("<td>")
            print(no_cells[j])
            print("</td>")

    print("</tr>")

print("</table>")
print("</body>")
print("</html>")