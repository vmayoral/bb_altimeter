import subprocess
import os

def check(program):
    """ Checks wether a program exists or not. If it does so, it returns the path of the program
    otherwise it returns 0.
    """
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    # if not found
    return 0

def readI2C(register):
    """ uses i2c-tools to read the MPL register values.
            the parameters should be given as strings.
    """
    p = subprocess.Popen(["i2cget", bus, chip, register],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # confirm the warning message
    p.stdin.write('Y\n')
    #print p.stdout.read().strip()
    valor = p.stdout.read().strip()
    p.kill()
    return valor

def writeI2C(register, value):
    """ Write a value into a register of the MPL sensor using the Linux i2c-tools.
            the parameters should be given as strings.
    """
    p = subprocess.Popen(["i2cset", bus, chip, register, value],stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # confirm the warning message
    p.stdin.write('Y\n')
    #return p.stdout.read().strip()

def check_i2ctools()
	print ""
	print "Checking if i2c-tools are installed:"
	flag = 0
	if check("i2cget"):
	    print "     i2cget: YES"
	else:
	    print "     i2cget: NO"
	    flag = 1
	    
	if check("i2cset"):
	    print "     i2cset: YES"
	else:
	    print "     i2cset: NO"
	    flag = 1
	    
	if flag:
	    print ""
	    print "Linux i2c-tools doesn't seem to be correctly installed. Please install them before running."
	    raise SystemExit
	else:
	    print ""
	    print "Linux i2c-tools properly installed"

    
"""
The following lines should be used when using this library
##############################################
##############################################
bus = "1" 
chip = "0x60" # address of the MPL sensor
##############################################
##############################################
"""
