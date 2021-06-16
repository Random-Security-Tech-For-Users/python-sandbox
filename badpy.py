import test
import os
try:
  os.system("echo \"do bad things\"")
except Exception as err:
  print("os.system errored with: {}".format(err))
else:
  print("No errors (test.py failed)")
