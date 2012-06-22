import subprocess

def run(cmd):
    try:
        p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        stdout, stderr = p.communicate()
    except OSError, e:
        raise RuntimeError("Unable to execute command '%s' - error: %s" % (cmd, e))
    return stdout

def call_gmetric(name, value, type='float'):
    cmd = 'gmetric --type %s --name %s --value %s' % (type, name, value)
    print cmd
    #run(cmd)
