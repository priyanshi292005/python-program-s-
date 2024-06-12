row1 = [1,1,1]
row2 = [1,1,1]
row3 = [1,1,1]
matris = [row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')
position = input("Enter the poisition where you want to hide money :")

row_number = int(position[0])
column_number = int(position[1])
row_selected = matris[row_number-1]
row_selected [column_number-1]='x'
print(f'{row1}\n{row2}\n{row3}')