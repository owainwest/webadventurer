# Have fun going to random webpages! 
# You never know how many working sites you get will exist, or what they will be!
# Pick how many tabs you'd like to try. I suggest 10!
# Let the serendipity begin!
import webbrowser
import string
string.letters = 'aiesotcdmnlpbfyr'
import random
numwindows = input('Number of random windows: ')
try:
	numwindows = int(numwindows)
except ValueError:
	print("Number of windows has to be a number")

x = 0
while x < numwindows:
	numchars = random.randint(3,7)

	def stringconcat(numchars):
		if numchars == 0:
			return ""
		else:
			return random.choice(string.letters) + stringconcat(numchars-1)

	webbrowser.open_new_tab("http://" + stringconcat(numchars) + ".com")
	x += 1


