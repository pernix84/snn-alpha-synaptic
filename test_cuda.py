from __future__ import print_function
import torch
import sys

x = torch.rand(5, 3)
print(x)

is_cuda_available = torch.cuda.is_available()

print("=============>")
print("Is cuda enabled? {0}".format(is_cuda_available))

sys.stdout.flush()

if ((is_cuda_available)):
    sys.exit(0)
else:
    sys.exit(1)
