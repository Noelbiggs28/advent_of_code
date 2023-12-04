import sys

text = sys.stdin.read()
no_dots = text.replace('.', '')
no_numbers = ''.join(filter(lambda x: x.isdigit()==False, no_dots))
unique_symbols = ''
for char in no_numbers:
    if char not in unique_symbols:
        unique_symbols += char
sys.stdout.write(unique_symbols)
# python check_symbols.py < input.txt > output.txt