# Not running

from __future__ import with_statement
import re

# Initialize lists to store words and results
words = []
testword = []
ans = []

# Display menu
print("MENU")
print("-----------")
print(" 1 . Hash tag segmentation ")
print(" 2 . URL segmentation ")
print("Enter the input choice for performing word segmentation: ")

# Get user choice
choice = int(input())

# Process based on user choice
if choice == 1:
    text = "#whatismyname"
    print("input with HashTag", text)
    # Remove non-word characters
    pattern = re.compile("[^\w']")
    a = pattern.sub('', text)
elif choice == 2:
    text = "www.whatismyname.com"
    print("input with URL", text)
    # Split URL into components
    a = re.split('\s|(?<!\d),.', text)
    splitwords = ["www", "com", "in"]
    # Remove common URL parts
    a = "".join([each for each in a if each not in splitwords])
else:
    print("Wrong choice...try again")
    exit()

print(a)

# Convert the string into a list of characters
for each in a:
    testword.append(each)

test_length = len(testword)

# Read words from the corpus file
with open(r"C:\Users\vivek\PycharmProjects\Prac2\P2-words.txt", 'r') as f:
    lines = f.readlines()
    words = [e.strip() for e in lines]

# Function to segment the input string
def Seg(a, length):
    ans = []
    for k in range(0, length + 1):
        if a[0:k] in words:
            print(a[0:k], "-appears in the corpus")
            ans.append(a[0:k])
            break
    if ans != []:
        g = max(ans, key=len)
        return g
    return ""

test_tot_itr = 0
answer = []
Score = 0
N = 37

# Segment the input string
while test_tot_itr < test_length:
    ans_words = Seg(a, test_length)
    if ans_words != "":
        test_itr = len(ans_words)
        answer.append(ans_words)
        a = a[test_itr:test_length]
        test_tot_itr += test_itr

# Join the segmented words
Aft_Seg = " ".join([each for each in answer])

# Display the output
print("Output: ")
print("---------")
print("After segmentation: ", Aft_Seg)

# Calculate and display the score
C = len(answer)
score = C * N / N
print("Score: ", score)
