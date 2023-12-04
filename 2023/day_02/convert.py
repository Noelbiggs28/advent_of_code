import sys

text = sys.stdin.read()
# convers all : and ; to , to make it easier to work with
modified_text = text.replace(':', ',').replace(';',',')
sys.stdout.write(modified_text)
# python convert.py < input.txt > output.csv