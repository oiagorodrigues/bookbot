# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

This is a simple exercise made in Python 3 that reads a text file and count the number of words and characters in it.

## Instructions

Clone the repo:

```
git clone https://github.com/oiagorodrigues/bookbot.git
cd bookbot
```

Run the project in the CLI using python3 interpreter:

```
// bookbot
python3 main.py my_book.txt
```

This will print a nice report of the amount of words and characters this text has:

```
============ BOOKBOT ============
Analyzing book found at books/mobydick.txt...
----------- Word Count ----------
Found 130410 total words
--------- Character Count -------
e: 74451
t: 50837
a: 44834
o: 43383
i: 41198
n: 40686
h: 36162
s: 35695
r: 35168
d: 23723
l: 23475
u: 16303
m: 15676
c: 14838
y: 13579
w: 13017
f: 12996
g: 11007
b: 9762
p: 9154
v: 6118
k: 3497
x: 1032
j: 1014
z: 971
q: 660
ê: 8
à: 4
é: 2
â: 1
œ: 1
============= END ===============
```

## Arguments

| Argument       | Description                                     |
| -------------- | ----------------------------------------------- |
| <path_to_book> | The path to text file you wanna the bot to read |

## Requirements

Python 3: [^3.13.x](https://www.python.org/downloads/release/python-3133/)
