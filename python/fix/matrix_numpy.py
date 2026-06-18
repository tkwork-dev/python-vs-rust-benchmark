"""行列積（N×N） - NumPy版 パフォーマンス検証（Python + Cバインディング）"""

import time
import numpy as np


def create_matrix(n: int) -> np.ndarray:
    """テスト用の行列を生成する（要素 = (i * n + j + 1) % 100）"""
    return np.array([[(i * n + j + 1) % 100 for j in range(n)] for i in range(n)], dtype=np.float64)


def main() -> None:
    n = 200  # 200x200行列

    a = create_matrix(n)
    b = create_matrix(n)

    # 計測開始
    start = time.perf_counter()
    c = np.matmul(a, b)
    end = time.perf_counter()

    # 実行時間をミリ秒に変換
    elapsed_ms = (end - start) * 1000

    # 結果出力
    print("=== 行列積（N×N） - NumPy版 ===")
    print(f"言語: Python (NumPy)")
    print(f"サイズ: {n}x{n}")
    print(f"C[0][0]: {c[0][0]:.0f}")
    print(f"C[{n-1}][{n-1}]: {c[n-1][n-1]:.0f}")
    print(f"実行時間: {elapsed_ms:.2f} ms")


if __name__ == "__main__":
    main()
