Cross-Compilation exploits

    https://arrayfire.com/cross-compile-to-windows-from-linux/
 
sudo apt-get install mingw-w64
 
# C
i686-w64-mingw32-gcc hello.c -o hello32.exe      # 32-bit
x86_64-w64-mingw32-gcc hello.c -o hello64.exe    # 64-bit
 
# C++
i686-w64-mingw32-g++ hello.cc -o hello32.exe     # 32-bit
x86_64-w64-mingw32-g++ hello.cc -o hello64.exe   # 64-bit
