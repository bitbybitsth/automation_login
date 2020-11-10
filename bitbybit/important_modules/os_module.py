import os
from datetime import datetime as dt
# to interact with underlying operating system


cwd = os.getcwd()
print("current working Directory:", cwd)

# cd = os.chdir("C:\\3B\\recordings")

print("current working Directory:", os.getcwd())

list_current_dir = os.listdir("C:\\3B\\recordings")
print(list_current_dir)

# os.mkdir("modules_eg")

# os.makedirs("assigment/advanced/interview")
# os.makedirs("interview/examples")

# os.rmdir("interview")
# os.removedirs("interview/examples")


# os.rename('timedelta_&_operations.py','timedelta_and_operations.py')

stat = os.stat('random_module.py')
print(stat)
print("size of file", stat.st_size)
print("modified time", dt.fromtimestamp(stat.st_mtime))
# print("")

print(os.environ)
if 'win' in os.environ.get('OS').lower():
    print("Welcome Windows user")

print(os.environ.get("computerame"))

# os.chdir(os.environ.get("homepath"))
# print(os.getcwd())


tree = os.walk("c:\\3B\\pycharm\\bitbybit")
# print(tree)

# for path, dirs, files in tree:
#     print("path:", path)
#     print("dirs", dirs)
#     print("files", files)


print(os.path.basename("c:\\3B\\pycharm\\bitbybit\\adavanced_concepts\\decorators.py"))
print(os.path.dirname("c:\\3B\\pycharm\\bitbybit\\adavanced_concepts\\decorators.py"))
# print(os.path.isfile("c:\\3B\\pycharm\\bitbybit\\adavanced_concepts\\decorators.py"))
# print(os.path.isdir("c:\\3B\\pycharm\\bitbybit\\adavanced_concepts"))
# print(os.path.exists("c:\\3B\\pycharm\\bitbybit\\adavanced_concepts\\decorators.py"))


f = os.path.join("c:\\3B\\pycharm", "examples\j2")
print(f)

# print(os.path.isdir(f))


print(os.environ)












