import torch

# Check if CUDA is available
print("CUDA Available:", torch.cuda.is_available())
print("PyTorch Version:", torch.__version__)

if torch.cuda.is_available():
    # Get the current device
    device = torch.cuda.current_device()
    print("Device Name:", torch.cuda.get_device_name(device))
    print("Device Index:", device)

    # Get CUDA capability
    capability = torch.cuda.get_device_capability(device)
    print("CUDA Capability:", f"{capability[0]}.{capability[1]}")

    # Check PyTorch's compiled CUDA architectures
    print("Compiled CUDA Architectures:", torch.cuda.get_arch_list())
else:
    print("No CUDA-capable GPU detected.")
