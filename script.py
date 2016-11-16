import shlex
import random
import statistics
import my_other_script

def is_odd_or_even(words):
	return (len(words) % 2 == 0)

def find_if_odd(words):
	for i in words:
		answer = is_odd_or_even(i.get('name'))
		i.update({'answer':'odd'})
	return words

if __name__ == "__main__":
    users = [
    		{'name':'guinsly', 'age':35, 'marks': [89,75,92], 'fav_quotes': "like he said 'hello'!"},
    		{'name':'Matthew', 'age':29, 'marks': [82,79,85], 'fav_quotes': "like he said 'hello'!"},
    		{'name':'Thomas', 'age':39, 'marks': [], 'fav_quotes': "like he said 'hello'!"}
    		]
    users = find_if_odd(users)
    print(users)
    linecache.getline(statistics.__file__, 8)
