from __future__ import print_function
import torch
import sys

x = torch.rand(5, 3)
print(x)

is_cuda_available = torch.cuda.is_available()

print("=============>")
print("Is CUDA enabled? {0}".format(is_cuda_available))

sys.stdout.flush()

if not is_cuda_available:
    print("##teamcity[message text='CUDA is not avaiable' status='ERROR']")
