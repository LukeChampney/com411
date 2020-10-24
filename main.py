import basics.output.simple_message as simple_message
import basics.output.multiline_message as multiline_message
import basics.output.ascii_art as ascii_art
import basics.output.escape_characters as escape_characters

import basics.input.ascii_robot as ascii_robot
import basics.input.data_types as data_types
import basics.input.review as review1
import basics.input.string_operators as string_operators
import basics.input.user_input as user_input

import basics.decisions.nested_decision.nestception as nestception
import basics.decisions.nested_decision.nested1 as nested1
import basics.decisions.operator.and_operator as and_operator
import basics.decisions.operator.or_operator as or_operator
import basics.decisions.simple_decision.comparison_operators as comparison_operators
import basics.decisions.simple_decision.counter as counter
import basics.decisions.simple_decision.if_elif_else as if_elif_else
import basics.decisions.simple_decision.if_else as if_else
import basics.decisions.simple_decision.if_ as if_
import basics.decisions.simple_decision.modulo_operator as modulo_operator

import basics.functions.ascii_character as ascii_character
import basics.functions.ascii_code as ascii_code
import basics.functions.function_calls as function_calls
import basics.functions.function_with_loop as function_with_loop
import basics.functions.function_with_nesting as function_with_nesting
import basics.functions.function_with_parameter as function_with_parameter
import basics.functions.function_with_parameters as function_with_parameters
import basics.functions.multiple_functions as multiple_functions
import basics.functions.return_values as return_values
import basics.functions.simple_function as simple_function

import basics.modules.guess_the_number as guess_the_number

import basics.repetitions.for_loop.characters as characters
import basics.repetitions.for_loop.count_down as count_down
import basics.repetitions.for_loop.membership_operators as membership_operators
import basics.repetitions.for_loop.range_ as range_
import basics.repetitions.for_loop.reverse as reverse
import basics.repetitions.for_loop.simple1 as simple1
import basics.repetitions.nested_loop.nested2 as nested2
import basics.repetitions.nested_loop.nesting as nesting
import basics.repetitions.while_loop.ascii_ as ascii_
import basics.repetitions.while_loop.count as count
import basics.repetitions.while_loop.factorial as factorial
import basics.repetitions.while_loop.len_ as len_
import basics.repetitions.while_loop.simple2 as simple2
import basics.repetitions.while_loop.sum_100 as sum_100
import basics.repetitions.while_loop.sum_user_numbers as sum_user_numbers

import data.lists.simple_list as simple_list
import data.lists.index_list as index_list


def run_blocks():

    is_running = True
    while (is_running):
        print()
        print("Which block do you wish to open?")
        print()
        print("1) Block A: Basics")
        print("2) Block B: Data")
        print("3) Block C: Visualisation")
        print("4) Block D: Objects")
        print("5) Quit")
        response = input()
        print()

        if (response == "1"):
            run_block_a()
        elif (response == "2"):
            run_block_b()
        elif (response == "3"):
            run_block_c()
        elif (response == "4"):
            run_block_d()
        elif (response == "5"):
            break
        else:
            print("Error")


def run_block_a():
    print()
    print("Which folder in 'Block A: Basics' do you wish to open?")
    print()
    print("1) Output")
    print("2) Input")
    print("3) Decisions")
    print("4) Repetitions")
    print("5) Functions")
    print("6) Modules")
    print("7) Go back")
    response = input()
    print()

    if (response == "1"):
        run_block_a_output()

    elif (response == "2"):
        run_block_a_input()

    elif (response == "3"):
        run_block_a_decisions()

    elif (response == "4"):
        run_block_a_repetitions()

    elif (response == "5"):
        run_block_a_functions()

    elif (response == "6"):
        run_block_a_modules()

    elif (response == "7"):
        run_blocks()

    else:
        print("Error! Please try again")
        run_block_a()


def run_block_a_output():
    print("")
    print("Which program in 'Output' do you wish to run?")
    print()
    print("1) ascii_art")
    print("2) escape_characters")
    print("3) multiline_message")
    print("4) simple_message")
    print("5) Go back")
    response = input()
    print()

    if (response == "1"):
        ascii_art.run()
        print("")
        run_block_a_output()

    elif (response == "2"):
        escape_characters.run()
        print("")
        run_block_a_output()

    elif (response == "3"):
        multiline_message.run()
        print("")
        run_block_a_output()

    elif (response == "4"):
        simple_message.run()
        print("")
        run_block_a_output()

    elif (response == "5"):
        run_block_a()

    else:
        print("Error! Please try again")
        run_block_a_output()


def run_block_a_input():
    print("")
    print("Which program in 'Input' do you wish to run?")
    print()
    print("1) ascii_robot")
    print("2) review")
    print("3) data_types")
    print("4) string_operators")
    print("5) user_input")
    print("6) Go back")
    response = input()
    print()

    if (response == "1"):
        ascii_robot.run()
        print("")
        run_block_a_input()

    elif (response == "2"):
        review1.run()
        print("")
        run_block_a_input()

    elif (response == "3"):
        data_types.run()
        print("")
        run_block_a_input()

    elif (response == "4"):
        string_operators.run()
        print("")
        run_block_a_input()

    elif (response == "5"):
        user_input.run()
        print("")
        run_block_a_input()

    elif (response == "6"):
        run_block_a()

    else:
        print("Error! Please try again")
        run_block_a_input()


def run_block_a_decisions():
    print("")
    print("Which folder in 'Decisions' do you wish to run?")
    print()
    print("1) nested_decision")
    print("2) operator")
    print("3) simple_decision")
    print("4) Go back")

    response = input()
    print()

    if (response == "1"):
        run_block_a_decisions_nested_decision()

    elif (response == "2"):
        run_block_a_decisions_operator()

    elif (response == "3"):
        run_block_a_decisions_simple_decision()

    elif (response == "4"):
        run_block_a()

    else:
        print("Error! Please try again")
        run_block_a_decisions()


def run_block_a_decisions_nested_decision():
    print("")
    print("Which program in 'Nested_Decision' do you wish to run?")
    print()
    print("1) nestception")
    print("2) nested")
    print("3) Go back")

    response = input()
    print()

    if (response == "1"):
        nestception.run()
        print("")
        run_block_a_decisions_nested_decision()

    elif (response == "2"):
        nested1.run()
        print("")
        run_block_a_decisions_nested_decision()

    elif (response == "3"):
        run_block_a_decisions()

    else:
        print("Error! Please try again")
        run_block_a_decisions_nested_decision()


def run_block_a_decisions_operator():
    print("")
    print("Which program in 'Operator' do you wish to run?")
    print()
    print("1) and_operator")
    print("2) or_operator")
    print("3) Go back")

    response = input()
    print()

    if (response == "1"):
        and_operator.run()
        print("")
        run_block_a_decisions_operator()

    elif (response == "2"):
        or_operator.run()
        print("")
        run_block_a_decisions_operator()

    elif (response == "3"):
        run_block_a_decisions()

    else:
        print("Error! Please try again")
        run_block_a_decisions_operator()


def run_block_a_decisions_simple_decision():
    print("")
    print("Which program in 'Simple_Decision' do you wish to run?")
    print()
    print("1) comparison_operators")
    print("2) counter")
    print("3) if_elif_else")
    print("4) if_else")
    print("5) if")
    print("6) modulo_operator")
    print("7) Go back")

    response = input()
    print()

    if (response == "1"):
        comparison_operators.run()
        print("")
        run_block_a_decisions_simple_decision()

    elif (response == "2"):
        counter.run()
        print("")
        run_block_a_decisions_simple_decision()

    elif (response == "3"):
        if_elif_else.run()
        print("")
        run_block_a_decisions_simple_decision()

    elif (response == "4"):
        if_else.run()
        print("")
        run_block_a_decisions_simple_decision()

    elif (response == "5"):
        if_.run()
        print("")
        run_block_a_decisions_simple_decision()

    elif (response == "6"):
        modulo_operator.run()
        print("")
        run_block_a_decisions_simple_decision()

    elif (response == "7"):
        run_block_a_decisions()

    else:
        print("Error! Please try again")
        run_block_a_decisions_simple_decision()


def run_block_a_repetitions():
    print("")
    print("Which folder in 'Repetitions' do you wish to run?")
    print()
    print("1) for_loop")
    print("2) nested_loop")
    print("3) while_loop")
    print("4) Go back")

    response = input()
    print()

    if (response == "1"):
        run_block_a_repetitions_for_loop()

    elif (response == "2"):
        run_block_a_repetitions_nested_loop()

    elif (response == "3"):
        run_block_a_repetitions_while_loop()()

    elif (response == "4"):
        run_block_a()

    else:
        print("Error! Please try again")
        run_block_a_repetitions()


def run_block_a_repetitions_for_loop():
    print("")
    print("Which program in 'For_Loop' do you wish to run?")
    print()
    print("1) characters")
    print("2) count_down")
    print("3) membership_operators")
    print("4) range")
    print("5) reverse")
    print("6) simple")
    print("7) Go back")

    response = input()
    print()

    if (response == "1"):
        characters.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "2"):
        count_down.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "3"):
        membership_operators.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "4"):
        range_.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "5"):
        reverse.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "6"):
        simple1.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "7"):
        run_block_a_decisions()

    else:
        print("Error! Please try again")
        run_block_a_repetitions_for_loop()


def run_block_a_repetitions_nested_loop():
    print("")
    print("Which program in 'Nested_Loop' do you wish to run?")
    print()
    print("1) nested")
    print("2) nesting")
    print("3) Go back")

    response = input()
    print()

    if (response == "1"):
        nested2.run()
        print("")
        run_block_a_repetitions_nested_loop()

    elif (response == "2"):
        nesting.run()
        print("")
        run_block_a_repetitions_nested_loop()

    elif (response == "3"):
        run_block_a_decisions()

    else:
        print("Error! Please try again")
        run_block_a_repetitions_nested_loop()


def run_block_a_repetitions_while_loop():
    print("")
    print("Which program in 'While_Loop' do you wish to run?")
    print()
    print("1) ascii")
    print("2) count")
    print("3) factorial")
    print("4) len")
    print("5) simple")
    print("6) sum_100")
    print("7) sum_user_numbers.py")
    print("8) Go back")

    response = input()
    print()

    if (response == "1"):
        ascii_.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "2"):
        count.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "3"):
        factorial.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "4"):
        len_.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "5"):
        simple2.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "6"):
        sum_100.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "7"):
        sum_user_numbers.run()
        print("")
        run_block_a_repetitions_for_loop()

    elif (response == "8"):
        run_block_a_repetitions()

    else:
        print("Error! Please try again")
        run_block_a_repetitions_while_loop()


def run_block_a_functions():
    print("")
    print("Which program in 'Functions' do you wish to run?")
    print()
    print("1) ascii_character")
    print("2) ascii_code")
    print("3) function_calls")
    print("4) function_with_loop")
    print("5) function_with_nesting")
    print("6) function_with_parameter")
    print("7) function_with_parameters")
    print("8) multiple_functions")
    print("9) return_values")
    print("10) simple_function")
    print("11) Go back")
    response = input()
    print()

    if (response == "1"):
        ascii_character.run()
        print("")
        run_block_a_functions()

    elif (response == "2"):
        ascii_code.run()
        print("")
        run_block_a_functions()

    elif (response == "3"):
        function_calls.run()
        print("")
        run_block_a_functions()

    elif (response == "4"):
        function_with_loop.run()
        print("")
        run_block_a_functions()

    elif (response == "5"):
        function_with_nesting.run()
        print("")
        run_block_a_functions()

    elif (response == "6"):
        function_with_parameter.run()
        print("")
        run_block_a_functions()

    elif (response == "7"):
        function_with_parameters.run()
        print("")
        run_block_a_functions()

    elif (response == "8"):
        multiple_functions.run()
        print("")
        run_block_a_functions()

    elif (response == "9"):
        return_values.run()
        print("")
        run_block_a_functions()

    elif (response == "10"):
        simple_function.run()
        print("")
        run_block_a_functions()

    elif (response == "11"):
        run_block_a()

    else:
        print("Error! Please try again")
        run_block_a_functions()


def run_block_a_modules():
    print("")
    print("Which program in 'Modules' do you wish to run?")
    print()
    print("1) guess_the_number")
    print("2) Go back")

    response = input()
    print()

    if (response == "1"):
        guess_the_number.run()
        print("")
        run_block_a_modules()

    elif (response == "2"):
        run_block_a()

    else:
        print("Error! Please try again")
        run_block_a_modules()


def run_block_b():
    print()
    print("Which folder in 'Block B: Data' do you wish to open?")
    print()
    print("1) Lists")
    print("2) Go back")
    response = input()
    print()

    if (response == "1"):
        run_block_b_lists()

    elif (response == "2"):
        run_blocks()

    else:
        print("Error! Please try again")
        run_block_b()


def run_block_b_lists():
    print("")
    print("Which program in 'Lists' do you wish to run?")
    print()
    print("1) simple_list")
    print("2) index_list")
    print("3) Go back")
    response = input()
    print()

    if (response == "1"):
        simple_list.run()
        print("")
        run_block_b_lists()

    elif (response == "2"):
        index_list.run()
        print("")
        run_block_b_lists()


    elif (response == "3"):
        run_block_b()

    else:
        print("Error! Please try again")
        run_block_b_lists()


def run_block_c():
    print("Folder system is not made yet")


def run_block_d():
    print("Folder system is not made yet")


run_blocks()