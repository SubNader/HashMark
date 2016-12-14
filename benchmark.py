import time
import hashlib
import matplotlib.pyplot as plot

# Variables
string = "The brown fox jumps over the lazy dog"
algo = ['MD5', 'SHA-1', 'SHA-224', 'SHA-256', 'SHA-384', 'SHA-512']
colors = ['b', 'c', 'y', 'm', 'r', 'k']
results = {}

# Fetch iterations and step from user
iterations = int(raw_input("Iterations: "))
step = int(raw_input("Step: "))
print "\nBenchmarking in progress..\n"

# MD5
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.md5(string)
    results[0,(i+1)*step] = (time.time() - Start)
print "\nCompleted MD5 benchmarking.\n"

# SHA-1
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.sha1(string)
    results[1, (i+1)*step] = (time.time() - Start)
print "\nCompleted SHA-1 benchmarking.\n"

# SHA-224
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.sha224(string)
    results[2, (i+1)*step] = (time.time() - Start)
print "\nCompleted SHA-224 benchmarking.\n"

# SHA-256
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.sha256(string)
    results[3, (i+1)*step] = (time.time() - Start)
print "\nCompleted SHA-256 benchmarking.\n"

# SHA-384
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.sha384(string)
    results[4, (i+1)*step] = (time.time() - Start)
print "\nCompleted SHA-384 benchmarking.\n"

# SHA-512
Start = time.time()
for i in range (iterations):
    for j in range ((i+1)*step):
        hashlib.sha512(string)
    results[5, (i+1)*step] = (time.time() - Start)
print "\nCompleted SHA-512 benchmarking.\n"

# Generate plot and print results
print "\n---------- Report ----------\n"
for i in range(6):
    print algo[i]
    for j in range (iterations):
        print (j+1)*step, 'iterations in', results[i,(j+1)*step]*pow(10,3), 'ms'
        plot.plot((j+1)*step, results[i,(j+1)*step]*pow(10,3),colors[i]+'.', label=str(algo[i]) if j == 0 else "")
    print '\n'
plot.xlabel('Iterations')
plot.ylabel('Time execution time in milliseconds')
plot.title('Hash functions benchmark',fontsize=20,color='blue')
plot.legend(loc=2)
plot.grid(True)
plot.show()