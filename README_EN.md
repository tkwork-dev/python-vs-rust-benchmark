# Python vs Rust Performance Benchmark

A project that quantitatively verifies why "Python is slow" by comparing execution times of identical algorithms implemented in Python and Rust.

## Phases

| Phase | Topic | Status |
|-------|-------|--------|
| 1 | Fibonacci (Recursive) | ✅ Done |
| 2 | Sieve of Eratosthenes | ✅ Done |
| 3 | Matrix Multiplication (N×N) | ✅ Done |
| 4 | Palindrome Check | ✅ Done |

## Prerequisites

- Python 3.10+
- NumPy (required for fix/ benchmarks): `pip install numpy`
- Rust (via rustup): https://rustup.rs/
- Visual Studio Build Tools 2022 (MSVC linker)

## How to Run

### Run All (Recommended)

```powershell
# From PowerShell
powershell -ExecutionPolicy Bypass -File run_benchmark.ps1

# Or double-click run.bat
run.bat
```

### Run Individually

```bash
# Pure Python
python python/fibonacci.py
python python/sieve.py
python python/matrix.py
python python/palindrome.py

# Python + C Bindings (fix/)
pip install numpy
python python/fix/fibonacci_lru.py
python python/fix/sieve_numpy.py
python python/fix/matrix_numpy.py
python python/fix/palindrome_regex.py
python python/fix/comparison_all.py    # All-in-one comparison

# Rust (build required)
cd rust/fibonacci && cargo build --release && ./target/release/fibonacci.exe
cd rust/sieve && cargo build --release && ./target/release/sieve.exe
cd rust/matrix && cargo build --release && ./target/release/matrix.exe
cd rust/palindrome && cargo build --release && ./target/release/palindrome.exe
```

## Project Structure

```
python-vs-rust-benchmark/
├── docs/
│   └── 要件定義書.md              # Requirements (Japanese)
├── python/
│   ├── fibonacci.py               # Phase 1: Fibonacci (recursive)
│   ├── sieve.py                   # Phase 2: Sieve of Eratosthenes
│   ├── matrix.py                  # Phase 3: Matrix multiplication
│   ├── palindrome.py              # Phase 4: Palindrome check
│   └── fix/                       # C-binding accelerated versions
│       ├── comparison_all.py      # All-in-one comparison benchmark
│       ├── fibonacci_lru.py       # lru_cache version
│       ├── sieve_numpy.py         # NumPy version
│       ├── matrix_numpy.py        # NumPy version
│       └── palindrome_regex.py    # Slice version
├── rust/
│   ├── fibonacci/                 # Phase 1
│   ├── sieve/                     # Phase 2
│   ├── matrix/                    # Phase 3
│   └── palindrome/                # Phase 4
├── run_benchmark.ps1              # Benchmark runner (PowerShell)
├── run.bat                        # Double-click to run
└── README.md                      # Documentation (Japanese)
```

## Benchmark Descriptions

### Phase 1: Fibonacci (Recursive)

The Fibonacci sequence adds two previous numbers to produce the next (0, 1, 1, 2, 3, 5, 8, 13...).
We use naive recursion (no memoization) to compute fib(40), which triggers ~330 million function calls.

```
fib(5) = fib(4) + fib(3)
       = (fib(3) + fib(2)) + (fib(2) + fib(1))
       = ... calls explode exponentially
```

**What it measures**: Per-function-call overhead (frame object creation, stack operations)

---

### Phase 2: Sieve of Eratosthenes

Marks multiples of each prime as composite, efficiently finding all primes up to 10 million (664,579 primes). Heavy on loops and array access.

```
2 is prime → mark 4,6,8,10... as composite
3 is prime → mark 9,12,15,18... as composite
5 is prime → mark 25,30,35... as composite
... remaining unmarked numbers are prime
```

**What it measures**: Per-loop-iteration cost, array read/write performance

---

### Phase 3: Matrix Multiplication (N×N)

Multiplies two 200×200 matrices using a triple-nested loop (8,000,000 floating-point operations). The most CPU-intensive benchmark.

```
C[i][j] = A[i][0]*B[0][j] + A[i][1]*B[1][j] + ... + A[i][199]*B[199][j]
→ Computed for all 40,000 elements
```

**What it measures**: Raw numerical throughput, accumulated overhead in nested loops

---

### Phase 4: Palindrome Check

Checks whether 1 million 100-character strings are palindromes by comparing characters from both ends.

```
"abcba" → a==a, b==b → palindrome
"abcde" → a!=e → not a palindrome
```

**What it measures**: String object creation/access cost, GC (garbage collection) impact

---

## Results

### Full Comparison (3-way)

| Phase | Topic | Pure Python | Python + C | Rust | Pure vs Rust |
|-------|-------|-------------|-----------|------|--------------|
| 1 | Fibonacci (N=40) | 12,000 ms | 0.05 ms (lru_cache) | 216 ms | **55x** |
| 2 | Sieve (limit 10M) | 903 ms | 20 ms (NumPy) | 21 ms | **43x** |
| 3 | Matrix (200×200) | 478 ms | 0.77 ms (NumPy) | 6 ms | **84x** |
| 4 | Palindrome (1M) | 1,021 ms | 171 ms (slice) | 43 ms | **24x** |

### Analysis

#### Phase 1: Fibonacci (55x slower)
- **Root cause**: Function call overhead
- Python creates a frame object and performs dynamic type checks on every recursive call
- Rust completes function calls with stack operations alone

#### Phase 2: Sieve (43x slower)
- **Root cause**: Interpreter loop overhead
- Python pays a bytecode dispatch cost per instruction
- Array (list) access goes through object references in Python

#### Phase 3: Matrix (84x slower) — Largest gap
- **Root cause**: Accumulated cost in CPU-dense numerical computation
- 8,000,000 floating-point operations, each requiring type checks
- Rust compiler may apply auto-vectorization (SIMD)

#### Phase 4: Palindrome (24x slower) — Smallest gap
- **Root cause**: String access and object manipulation
- Python's string index access is relatively optimized at the C level
- Still 24x slower due to reference counting and GC overhead

### Conclusion

Pure Python is **24–84x slower** than Rust for identical logic. The gap grows with more loops and numerical computation.

This is an inherent characteristic of Python's dynamic typing and interpreter execution model — unavoidable without C bindings.

## Supplementary: Pure Python vs C-Binding Versions

Proof that "Python is slow" only applies to pure Python code. With C bindings (NumPy, lru_cache), performance improves dramatically.

### Results

| Topic | Pure Python | C-Binding | Speedup | Method Used |
|-------|-----------|---------|--------|-------------|
| Fibonacci | 11,809 ms | 0.03 ms | **468,595x** | functools.lru_cache |
| Sieve | 894 ms | 19 ms | **47x** | NumPy array slicing |
| Matrix | 465 ms | 12 ms | **39x** | numpy.matmul (BLAS) |
| Palindrome | 1,003 ms | 143 ms | **7x** | String slice `s[::-1]` |

### Rust vs Python+C Comparison

| Topic | Rust | Python+C | Gap |
|-------|------|----------|-----|
| Sieve | 19 ms | 19 ms | **Nearly identical** |
| Matrix | 6 ms | 0.77 ms | NumPy (BLAS) is faster |
| Palindrome | 43 ms | 143 ms | Rust 3x faster |

### Key Takeaway

- Pure Python is indeed slow (24–84x slower than Rust)
- With C bindings, **Python can match or even exceed Rust's naive implementation**
- NumPy's matrix operations call BLAS (C/Fortran) internally, rivaling optimized native code
- "Python is slow" really means **the Python interpreter is slow** — when used as a bridge to C libraries, performance is not an issue

---

## Environment

- OS: Windows
- Python: 3.13
- Rust: 1.96.0 (2026-05-25)
- Build: cargo build --release (optimized)
