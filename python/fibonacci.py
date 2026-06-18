"""フィボナッチ数列 再帰計算 - パフォーマンス検証（Python）"""

import time


def fibonacci(n: int) -> int:
    """素朴な再帰によるフィボナッチ数計算（メモ化なし）"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    n = 40

    # 計測開始
    start = time.perf_counter()
    result = fibonacci(n)
    end = time.perf_counter()

    # 実行時間をミリ秒に変換
    elapsed_ms = (end - start) * 1000

    # 結果出力
    print("=== フィボナッチ数列 再帰計算 ===")
    print(f"言語: Python")
    print(f"N: {n}")
    print(f"結果: {result}")
    print(f"実行時間: {elapsed_ms:.2f} ms")


if __name__ == "__main__":
    main()
