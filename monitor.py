import subprocess
import sys
from datetime import datetime
cmd = "iwconfig wlx909f33eab5fa | grep Signal"
#subprocess.call(cmd.split())
f = open('output.txt','w')
try:
    while True:
        #p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=f)
        line = subprocess.check_output(cmd, shell=True)
        rst = ''+str(datetime.now())+' '+ line.strip()+'\n'
        print rst
        f.write(rst)
        #out = p.stderr.read(1)
        #if out == '' and p.poll() != None:
        #    pass
        #if out != '':
        #    f.write(out)
        #    sys.stdout.write(out)
        #    sys.stdout.flush()
except KeyboardInterrupt:
    print 'close'
    f.close()

#while True:
#    out = p.stderr.read(1)
#    if out == '' and p.poll() != None:
#        break
#    if out != '':
#        sys.stdout.write(out)
#        sys.stdout.flush()
