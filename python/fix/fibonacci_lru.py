"""フィボナッチ数列 - functools.lru_cache版 パフォーマンス検証

メモ化（C実装のキャッシュ）を使うことで、再帰の重複計算を排除する。
純粋再帰版との差を見る。

注意: これはアルゴリズム改善（メモ化）であり、純粋な言語性能比較ではない。
しかし「Pythonでも適切な最適化手法を活用すれば桁違いに速くなる」ことの証明。
"""

import time
import sys
from functools import lru_cache

# 再帰上限を引き上げ
sys.setrecursionlimit(10000)


@lru_cache(maxsize=None)
def fibonacci_cached(n: int) -> int:
    """lru_cacheによるメモ化フィボナッチ"""
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


def fibonacci_naive(n: int) -> int:
    """素朴な再帰（比較用）"""
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def main() -> None:
    n = 40

    # --- 素朴な再帰 ---
    start = time.perf_counter()
    result_naive = fibonacci_naive(n)
    elapsed_naive = (time.perf_counter() - start) * 1000

    # --- lru_cache版 ---
    fibonacci_cached.cache_clear()
    start = time.perf_counter()
    result_cached = fibonacci_cached(n)
    elapsed_cached = (time.perf_counter() - start) * 1000

    # 結果出力
    print("=== フィボナッチ数列 - 純粋再帰 vs lru_cache ===")
    print(f"N: {n}")
    print(f"")
    print(f"[純粋再帰]")
    print(f"  結果: {result_naive}")
    print(f"  実行時間: {elapsed_naive:.2f} ms")
    print(f"")
    print(f"[lru_cache（メモ化）]")
    print(f"  結果: {result_cached}")
    print(f"  実行時間: {elapsed_cached:.4f} ms")
    print(f"")
    print(f"高速化倍率: {elapsed_naive / elapsed_cached:,.0f}x")


if __name__ == "__main__":
    main()
