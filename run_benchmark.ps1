# Python vs Rust Performance Benchmark - Full Comparison
# Pure Python / Python + C Bindings / Rust

[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'

# cargo PATH
$env:PATH = "$env:USERPROFILE\.cargo\bin;$env:PATH"

# MSVC environment setup
$vcvars = "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvars64.bat"

function Build-Rust {
    param([string]$Project)
    $dir = Join-Path $PSScriptRoot "rust\$Project"
    if (Test-Path $vcvars) {
        cmd /c "`"$vcvars`" x64 >nul 2>&1 & cd /d `"$dir`" & cargo build --release" 2>&1 | Out-Null
    } else {
        Push-Location $dir
        cargo build --release 2>&1 | Out-Null
        Pop-Location
    }
}

function Run-Rust {
    param([string]$Project)
    $exe = Join-Path $PSScriptRoot "rust\$Project\target\release\$Project.exe"
    if (Test-Path $exe) {
        & $exe
    } else {
        Write-Host "Error: $exe not found." -ForegroundColor Red
    }
}

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " Python vs Rust Performance Benchmark" -ForegroundColor Cyan
Write-Host " Pure Python / Python + C Bindings / Rust" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# =====================================================
# Phase 1: Fibonacci
# =====================================================
Write-Host "--- Phase 1: Fibonacci (N=40) ---" -ForegroundColor Green
Write-Host ""

Write-Host "[Pure Python]" -ForegroundColor Yellow
python python/fibonacci.py
Write-Host ""

Write-Host "[Python + lru_cache]" -ForegroundColor Yellow
python python/fix/fibonacci_lru.py
Write-Host ""

Write-Host "[Rust]" -ForegroundColor Yellow
Build-Rust "fibonacci"
Run-Rust "fibonacci"
Write-Host ""

# =====================================================
# Phase 2: Sieve of Eratosthenes
# =====================================================
Write-Host "--- Phase 2: Sieve of Eratosthenes (10M) ---" -ForegroundColor Green
Write-Host ""

Write-Host "[Pure Python]" -ForegroundColor Yellow
python python/sieve.py
Write-Host ""

Write-Host "[Python + NumPy]" -ForegroundColor Yellow
python python/fix/sieve_numpy.py
Write-Host ""

Write-Host "[Rust]" -ForegroundColor Yellow
Build-Rust "sieve"
Run-Rust "sieve"
Write-Host ""

# =====================================================
# Phase 3: Matrix Multiplication
# =====================================================
Write-Host "--- Phase 3: Matrix Multiply (200x200) ---" -ForegroundColor Green
Write-Host ""

Write-Host "[Pure Python]" -ForegroundColor Yellow
python python/matrix.py
Write-Host ""

Write-Host "[Python + NumPy]" -ForegroundColor Yellow
python python/fix/matrix_numpy.py
Write-Host ""

Write-Host "[Rust]" -ForegroundColor Yellow
Build-Rust "matrix"
Run-Rust "matrix"
Write-Host ""

# =====================================================
# Phase 4: Palindrome
# =====================================================
Write-Host "--- Phase 4: Palindrome (1M checks) ---" -ForegroundColor Green
Write-Host ""

Write-Host "[Pure Python]" -ForegroundColor Yellow
python python/palindrome.py
Write-Host ""

Write-Host "[Python + slice (C layer)]" -ForegroundColor Yellow
python python/fix/palindrome_regex.py
Write-Host ""

Write-Host "[Rust]" -ForegroundColor Yellow
Build-Rust "palindrome"
Run-Rust "palindrome"
Write-Host ""

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " All Benchmarks Complete" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
