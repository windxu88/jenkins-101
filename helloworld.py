import sys, os

print(sys.version)
print("Hello world")
print("Build job ID is: {0}\n Build URL is: {1}\n".format(os.environ['BUILD_ID'], os.environ['BUILD_URL']))
f = open('test.tx', 'w')
f.write('sssss')
