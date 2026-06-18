"""行列積（N×N） - パフォーマンス検証（Python）"""

import time


def matrix_multiply(a: list[list[float]], b: list[list[float]], n: int) -> list[list[float]]:
    """N×N行列の積を計算する（三重ループ）"""
    # 結果行列をゼロ初期化
    c = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            s = 0.0
            for k in range(n):
                s += a[i][k] * b[k][j]
            c[i][j] = s
    return c


def create_matrix(n: int) -> list[list[float]]:
    """テスト用の行列を生成する（要素 = (i * n + j + 1) % 100）"""
    return [[(i * n + j + 1) % 100 for j in range(n)] for i in range(n)]


def main() -> None:
    n = 200  # 200x200行列

    a = create_matrix(n)
    b = create_matrix(n)

    # 計測開始
    start = time.perf_counter()
    c = matrix_multiply(a, b, n)
    end = time.perf_counter()

    # 実行時間をミリ秒に変換
    elapsed_ms = (end - start) * 1000

    # 検証用: 左上と右下の要素を表示
    print("=== 行列積（N×N） ===")
    print(f"言語: Python")
    print(f"サイズ: {n}x{n}")
    print(f"C[0][0]: {c[0][0]:.0f}")
    print(f"C[{n-1}][{n-1}]: {c[n-1][n-1]:.0f}")
    print(f"実行時間: {elapsed_ms:.2f} ms")


if __name__ == "__main__":
    main()
