import subprocess


def run(cmd):
    """
    Execute a command and return STDOUT
    """
    try:
        p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        stdout, stderr = p.communicate()
    except OSError, e:
        raise RuntimeError("Unable to execute command '%s' - error: %s" % (cmd, e))
    return stdout


def call_gmetric(name, value, type='float', units="", debug=False):
    """
    Submit a metric
    """
    cmd = "gmetric --type %s --name %s --value %s --units='%s'" % (type, name, value, units)
    if debug:
        print cmd
    else:
        run(cmd)
