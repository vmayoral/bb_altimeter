import subprocess

# Example showing how to read the register 0x0c at the i2c-1 device address
# 0x60.
p = subprocess.Popen(["i2cget", "1", "0x60", "0x0c"],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.stdin.write('Y\n')
print p.stdout.read().strip()

