def load_paragraph():
    with open('C_code_sample.cpp', 'r') as file:
        code = file.read()
        return code
