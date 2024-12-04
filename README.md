# binstats

Statistics from our binary transformation framework. All files in this repo are Win64 binaries. No source code was altered in order to achieve these statistics. Furthermore no debug information (PDB, Map file, etc) was used to aid in the coverage statistics. Binaries in this repo were compiled with a wide range of compiler options (/O2, /GL, etc).

### Layout

- `asn1_dsa_internal_test/` - An OpenSSL test, you can find source [here](https://gitlab.softgenetics.com/libs/openssl/-/blob/f510d614a7e981cbf69f11ae186c97d3fa00dda9/test/asn1_dsa_internal_test.c)
- `chrome` - Main module for chrome (chrome.dll). This is the same binary as this one [here in bintests](https://github.com/backengineering/bintests/blob/master/misc/chrome/win64-121.0.6167.85/chrome-win64/chrome.dll)
- `clang-repl` - clang's repl, [read more here](https://clang.llvm.org/docs/ClangRepl.html)
- `Discord` - 64bit [Discord](https://discord.com/) 1.0.9157
- `engine2` - Engine module from [Counter-Strike 2](https://www.counter-strike.net/cs2)
- `Fibonacci` - LLVM JIT example, [source here](https://github.com/llvm-mirror/llvm/blob/master/examples/Fibonacci/fibonacci.cpp)
- `hvix64` - Microsoft's Hyper-V Intel module
- `libcrypto-3-x64` - OpenSSL (3.1.0) shared library
- `LLJITWithOptimizingIRTransform` - LLVM JIT example with optimizations, [source here](https://gitlab.eecs.wsu.edu/44373/t/-/blob/59cd45e5ae2920f2287d2b9df4ec0dc94e48c39d/llvm/examples/OrcV2Examples/LLJITWithOptimizingIRTransform/LLJITWithOptimizingIRTransform.cpp)
- `mpengine` - Microsoft Windows Defender module. [Alexei Bulazel reverse engineering of it](https://www.youtube.com/watch?v=2NawGCUOYT4)
- `MultiWorldDemo` - Unreal Engine 5 demo game. Repo for the [source is here.](https://github.com/UNAmedia/ue5-multiworld-demo) This is the same file as [this one here](https://github.com/backengineering/bintests/blob/master/misc/MultiWorldDemo/MultiWorldDemo/Binaries/Win64/MultiWorldDemo.exe).
- `notepad++` - Main executable for notepad++ (8.4.8.0)
- `ntdll.dll` - ntdll version 10.0.19041.4522
- `ntoskrnl` - ntoskrnl version 10.0.10240.16384
- `nvlddmkm` - NVIDIA's GPU Driver 25.21.14.2591
- `OrcV2CBindingsIRTransforms` - Another LLVM JIT example, [source here](https://code.ornl.gov/llvm-doe/llvm-project/-/blob/f756d38abf2ec40ee06ee5aa668db444e5d6f485/llvm/examples/OrcV2Examples/OrcV2CBindingsIRTransforms/OrcV2CBindingsIRTransforms.c)
- `Signal` - [Signal](https://signal.org/) main executable, version 7.4.0.0
- `Telegram` - [Telegram](https://telegram.org/) main executable, version 5.7.2.0
- `x64dbg` - [mrexodia (Duncan Ogilvie)](https://github.com/mrexodia) x64dbg dll
- `x64gui` - [mrexodia (Duncan Ogilvie)](https://github.com/mrexodia) x64gui dll
- `xul` - [Tor (aka Firefox)](https://gitlab.torproject.org/tpo/applications/tor-browser) main dll xul, version 115.15.0.9012

Each folder contains the following files:

- `func-info.csv` - This is a CSV file that contains function and basic block information, including reference counts.
- `func-leaaf.csv` - Tells you the [leaf status](https://learn.microsoft.com/en-us/cpp/build/stack-usage?view=msvc-170#function-types) of every function we identified. 
- `results.png` - Statistic results for the binary.
- `[file name]-coverage.svg` - The coverage statistics. ***Any function within the "transformed" catagory of the piechart can be obfuscated.***
- `[file name]` - The binary file name, same as the folder name.

### Generating Results

***Requires python 3.x***

```bash
pip install -r requirements.txt
python script.py
```

### Special Thanks

Special thanks to [mrexodia (Duncan Ogilvie)](https://github.com/mrexodia) and the rest of the people who maintain [x64dbg](https://github.com/x64dbg/x64dbg). We have spent thousands of hours building this binary transformation framework, many of those hours we spent in x64dbg.

### TODO

- [ ] Size of the most referenced basic block
- [ ] Number of basic blocks in the largest function
- [ ] number of instructions in the largest function
- [ ] average function size
- [ ] add UEFI files (bootmgfw)
- [ ] Executable env column
- [ ] Extend data set and make visuals (1 and 2 var visuals)