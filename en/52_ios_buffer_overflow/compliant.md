
Usually the ipa file will be decrypted at runtime by the kernel's mach
loader. If the binary is encrypted or not is easily found using otool

An example where the binary is encrypted:

    # otool -l OTHER_BINARY | grep -A 4 LC_ENCRYPTION_INFO
           cmd LC_ENCRYPTION_INFO
       cmdsize 20
      cryptoff 16384
     cryptsize 10502144
     cryptid   1

- ASLR
    - Usually the binary is compiled using the `PIE` flag
- Stack Smashing Protection
    - iOS applications usually use `[stack canaries]()`
    - therefore you should find certain symbols inside the binary
        (like `_stack_chk_guard` and `_stack_chk_fail`)
- Automatic Reference Couting
    - this option can be enabled by activating the compiler option
      `Objective-C Automatic Reference Counting`
    - binaries built with this option should include symbols called
      `_objc_release`, `_obj_autorelease`, `_obj_storeStrong`,
      `_obj_retain`

