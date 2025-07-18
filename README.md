# vision-transformer

```bash
echo 'export PATH=/usr/local/cuda/bin:$PATH' >> ~/envs/internvl/bin/activate
echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH' >> ~/envs/internvl/bin/activate

```

```bash
python check-cuda.py 
CUDA Available: True
PyTorch Version: 2.7.1+cu128
Device Name: NVIDIA GeForce RTX 5090
Device Index: 0
CUDA Capability: 12.0
Compiled CUDA Architectures: ['sm_75', 'sm_80', 'sm_86', 'sm_90', 'sm_100', 'sm_120', 'compute_120']


```

```bash
python -m bitsandbytes
=================== bitsandbytes v0.46.1 ===================
Platform: Linux-6.11.0-17-generic-x86_64-with-glibc2.39
  libc: glibc-2.39
Python: 3.12.3
PyTorch: 2.7.1+cu128
  CUDA: 12.8
  HIP: N/A
  XPU: N/A
Related packages:
  accelerate: 0.34.2
  diffusers: 0.34.0
  numpy: 1.26.4
  pip: 24.0
  peft: 0.16.0
  safetensors: 0.5.3
  transformers: 4.37.2
  triton: 3.3.1
  trl: not found
============================================================
PyTorch settings found: CUDA_VERSION=128, Highest Compute Capability: (12, 0).
Checking that the library is importable and CUDA is callable...
SUCCESS!
```

```bash
python check-transformers.py 
<class 'transformers.cache_utils.EncoderDecoderCache'>
```
