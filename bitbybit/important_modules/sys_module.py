import sys

# print(sys.path)

arg = sys.argv

x = 0
sum=0
for item in arg:
    if x == 0:
        x=1
    else:
        sum += int(item)

# print(sum)

sys.stdout.write(str(sum))
print(sys.version)
if "3.7.8" in sys.version:
    print("you have a correct version")

print(sys.getsizeof(sum))
print(sys.platform)
print(sys.exit(0))
print("******************")

