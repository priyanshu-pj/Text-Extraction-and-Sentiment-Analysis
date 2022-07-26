import pandas as pd
file_name = "files/Output_Data_Structure.xlsx"


def _paste_output(variables):

    output = pd.read_excel(file_name)
    var_list = ['POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE', 'SUBJECTIVITY SCORE',
    'AVG SENTENCE LENGTH', 'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX', 'AVG NUMBER OF WORDS PER SENTENCE',
    'COMPLEX WORD COUNT', 'WORD COUNT', 'SYLLABLE PER WORD', 'PERSONAL PRONOUNS', 'AVG WORD LENGTH']


    for i in range(0, 170):
        output[str(var_list[0])][i]     =   variables[i][0]
        output[str(var_list[1])][i]     =   variables[i][1]
        output[str(var_list[2])][i]     =   variables[i][2]
        output[str(var_list[3])][i]     =   variables[i][3]
        output[str(var_list[4])][i]     =   variables[i][4]
        output[str(var_list[5])][i]     =   variables[i][5]
        output[str(var_list[6])][i]     =   variables[i][6]
        output[str(var_list[7])][i]     =   variables[i][7]
        output[str(var_list[8])][i]     =   variables[i][8]
        output[str(var_list[9])][i]     =   variables[i][9]
        output[str(var_list[10])][i]    =   variables[i][10]
        output[str(var_list[11])][i]    =   variables[i][11]
        output[str(var_list[12])][i]    =   variables[i][12]


    output.to_excel('Output_Data_Structure.xlsx')