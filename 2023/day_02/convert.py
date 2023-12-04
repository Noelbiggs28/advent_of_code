import sys

text = sys.stdin.read()
modified_text = text.replace(':', ',').replace(';',',')
sys.stdout.write(modified_text)
# python convert.py < input.txt > output.csv