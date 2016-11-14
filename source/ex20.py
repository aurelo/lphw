from sys import argv


def print_all(f):
    print f.read()


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print line_count, f.readline(),  # comma at the end of print sp print doesn't print it's own \n
    # (readline will print it's own)


script, input_file = argv

current_file = open(input_file)

print_all(current_file)

rewind(current_file)

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

print_a_line(current_line + 1, current_file)
