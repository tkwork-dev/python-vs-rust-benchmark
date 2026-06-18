"""素数計算（エラトステネスの篩） - NumPy版 パフォーマンス検証（Python + Cバインディング）"""

import time
import numpy as np


def sieve_of_eratosthenes_numpy(limit: int) -> np.ndarray:
    """NumPyを使ったエラトステネスの篩"""
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[0] = False
    is_prime[1] = False

    i = 2
    while i * i <= limit:
        if is_prime[i]:
            # i*iからlimitまでi刻みで一括False
            is_prime[i * i::i] = False
        i += 1

    primes = np.nonzero(is_prime)[0]
    return primes


def main() -> None:
    limit = 10_000_000  # 1000万

    # 計測開始
    start = time.perf_counter()
    primes = sieve_of_eratosthenes_numpy(limit)
    end = time.perf_counter()

    # 実行時間をミリ秒に変換
    elapsed_ms = (end - start) * 1000

    # 結果出力
    print("=== 素数計算（エラトステネスの篩） - NumPy版 ===")
    print(f"言語: Python (NumPy)")
    print(f"上限: {limit:,}")
    print(f"素数の個数: {len(primes)}")
    print(f"最大の素数: {primes[-1]}")
    print(f"実行時間: {elapsed_ms:.2f} ms")


if __name__ == "__main__":
    main()
