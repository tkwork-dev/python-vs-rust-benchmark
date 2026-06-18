"""素数計算（エラトステネスの篩） - パフォーマンス検証（Python）"""

import time


def sieve_of_eratosthenes(limit: int) -> list[int]:
    """エラトステネスの篩で limit 以下の素数を列挙する"""
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    i = 2
    while i * i <= limit:
        if is_prime[i]:
            j = i * i
            while j <= limit:
                is_prime[j] = False
                j += i
        i += 1

    primes = []
    for i in range(2, limit + 1):
        if is_prime[i]:
            primes.append(i)
    return primes


def main() -> None:
    limit = 10_000_000  # 1000万

    # 計測開始
    start = time.perf_counter()
    primes = sieve_of_eratosthenes(limit)
    end = time.perf_counter()

    # 実行時間をミリ秒に変換
    elapsed_ms = (end - start) * 1000

    # 結果出力
    print("=== 素数計算（エラトステネスの篩） ===")
    print(f"言語: Python")
    print(f"上限: {limit:,}")
    print(f"素数の個数: {len(primes)}")
    print(f"最大の素数: {primes[-1]}")
    print(f"実行時間: {elapsed_ms:.2f} ms")


if __name__ == "__main__":
    main()
