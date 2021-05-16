import sys
count = len(sys.argv)
sys.stdout.write('User specified '+str(count)+' arguments:'+'\n')
for i in sys.argv:
    sys.stdout.write(str(i)+'\n')