def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    if brackets_row == "":
        return True
    else:
        while "()" in brackets_row:
            brackets_row = brackets_row.replace("()", "")
        if brackets_row == "":
            return True
        else:
            return False
