def arithmetic_arranger(problems, answer=False):
    problems_list = []
    result_list = []
    counter = 0
    first_line = " "
    second_line = ""
    third_line = ""
    fourth_line = ""
    # Checks to see if the input has 5 or less problems.
    if len(problems) > 5:
        return print('Error: Too many problems.')
    # Reads the input and stores everything in a tuple.
    for items in problems:
        operand1, operator, operand2 = items.split(" ")
        # Checks to see if the operands are actual digits.
        try:
            int(operand1)
            int(operand2)
        except:
            return print('Error: Numbers must only contain digits.')

        # Checks to see if the length of the digits is less than four.
        try:
            len(operand1) <= 4
            len(operand2) <= 4
        except:
            return print('Error: Numbers cannot be more than four digits.')

        # Appends the list with tuples containing the two operators and the operand.
        if operator == "+":
            problems_list.append(
                (operand1, operand2, operator, (int(operand1) + int(operand2))))
        elif operator == "-":
            problems_list.append(
                (operand1, operand2, operator, (int(operand1) - int(operand2))))
        if operator == "+":
            result_list.append(int(operand1) + int(operand2))
        elif operator == "-":
            result_list.append(int(operand1) - int(operand2))
        else:
            return print("Error: Operator must be '+' or '-'.")
    
    for each_tuple in problems_list:
        first_operand = each_tuple[:-1][0]
        second_operand = each_tuple[:-1][1]
        operator = each_tuple[:-1][2]
        if len(first_operand) >= len(second_operand):
            first_operand_bigger = True
            second_operand_bigger = False
        elif len(second_operand) >= len(first_operand):
            first_operand_bigger = False
            second_operand_bigger = True
        # Deals with the first line.
        if first_operand_bigger:
            left_padding_first_line = "  "
            right_padding_first_line = "    "
        elif second_operand_bigger:
            left_padding_first_line = ((len(second_operand) - len(first_operand)) * " ") + "  "
            right_padding_first_line = "    "

        counter += 1
        if first_operand is problems_list[-1][0]:
            if counter == len(problems):
                right_padding_first_line = "\n"
        first_line += f"{left_padding_first_line}{first_operand}{right_padding_first_line}"
        
        # Deals with the second line.
        if first_operand_bigger:
            padding_between_operator_and_second_operand = ((len(first_operand) - len(second_operand)) * " ") + " "
        elif second_operand_bigger:
            padding_between_operator_and_second_operand = " "
        
        if second_operand == problems_list[-1][1]:
            right_padding_second_line = "\n"
        else:
            right_padding_second_line = "    "
        second_line += f"{operator}{padding_between_operator_and_second_operand}{second_operand}{right_padding_second_line}"

        # Deals with the third line.
        if first_operand_bigger:
            dash_math = len(first_operand) * "-" + "--"
        elif second_operand_bigger:
             dash_math = len(second_operand) * "-" + "--"
        
        if second_operand == problems_list[-1][1]:
            if answer:
                right_padding_third_line = "\n"
            else:
                right_padding_third_line = ""
        else:
            right_padding_third_line = "    "
        third_line += f"{dash_math}{right_padding_third_line}"

    # Deals with the potential fourth line.
    if answer:
        for result in result_list:
            if str(result).startswith("-"):
                left_padding_fourth_line = " "
            else:
                if len(str(result)) == len(second_operand):
                    left_padding_fourth_line = "  "
                elif first_operand_bigger:
                    left_padding_fourth_line = ((len(first_operand) + 2) - len(str(result))) * " "
                elif second_operand_bigger:
                    left_padding_fourth_line = ((len(second_operand) + 2) - len(str(result))) * " "
    
            if result == each_tuple[:-1][-1]:
                right_padding_fourth_line = ""
            else:
                right_padding_fourth_line = "    "
            fourth_line += f"{left_padding_fourth_line}{result}{right_padding_fourth_line}"
    else:
        fourth_line = ""
    #arranged_problems = first_line + second_line + third_line# + fourth_line
    #return arranged_problems
    return print(first_line,second_line, third_line, fourth_line)
    


arithmetic_arranger(['3801 - 2', '123 + 49'])
arithmetic_arranger(['1 + 2', '1 - 9380'])
arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'])
arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])
arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'])
arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'])
arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'])
arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'])
arithmetic_arranger(['3 + 855', '988 + 40'], True)
arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)
