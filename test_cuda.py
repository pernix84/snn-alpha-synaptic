from __future__ import print_function
import torch
import sys

x = torch.rand(5, 3)
print(x)

print("=============>")
print("Is cuda enabled? {0}".format(torch.cuda.is_available()))

sys.stdout.flush()
