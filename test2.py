
import subprocess
cmd = ['python', 'test.py']
output = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
output = str(output)

output = output.split("\\")
"".join(output)

output[0] = output[0][2:]
output[len(output) - 1] = output[len(output) - 1][:1]

out = [[]]
con = 0

for c, item in enumerate(output):
    if item == "n":
        con += 1
        out.append([])
    if not item == "r" and not item == "n":
        if not item == []:
            out[con].append(item)


print(output)
print(out)