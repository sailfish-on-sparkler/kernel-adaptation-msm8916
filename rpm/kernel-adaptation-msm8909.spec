# Device details
%define device msm8909

# Kernel target architecture
%define kernel_arch arm

# Crossbuild toolchain to use
%define crossbuild armv7hl

# RPM target architecture, remove to leave it unaffected
# You should have a good reason to change the target architecture
# (like building on aarch64 targeting an armv7hl repository)
%define device_target_cpu armv7hl

# Defconfig to pick-up
%define defconfig msm8909_defconfig

# Linux kernel source directory
%define source_directory linux/

# Build modules
%define build_modules 1

# Build Image
##define build_Image 1

# Apply Patches
##define apply_patches 1

# Build uImage
##define build_uImage 1

# Build zImage
%define build_zImage 1

# Build and pick-up the following devicetrees
%define devicetrees qcom/qcom-msm8909-nokia-sparkler.dtb qcom/qcom-msm8909-nokia-leo.dtb

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc
