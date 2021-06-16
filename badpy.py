import test
import os
try:
  os.system("echo 1")
except Exception as err:
  print("os.system errored with: {}".format(err))
else:
  print("No errors (test.py failed)")
