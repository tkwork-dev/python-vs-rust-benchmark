"""文字列処理（回文判定） - Cバインディング活用版 パフォーマンス検証

文字列の反転にスライス（C実装）を使い、比較もC層で行う。
純粋Python版との差を見る。
"""

import time


def is_palindrome_slice(s: str) -> bool:
    """スライスによる回文判定（C実装の文字列反転を活用）"""
    return s == s[::-1]


def generate_test_strings(count: int) -> list[str]:
    """テスト用文字列を生成する（回文と非回文を混在）"""
    strings = []
    base = "abcdefghij" * 10  # 100文字
    for i in range(count):
        if i % 2 == 0:
            # 回文を作る
            half = base[:50]
            s = half + half[::-1]
        else:
            # 非回文
            s = base + str(i)
        strings.append(s)
    return strings


def main() -> None:
    count = 1_000_000  # 100万回判定

    # テストデータ生成（計測対象外）
    strings = generate_test_strings(count)

    # 計測開始
    start = time.perf_counter()
    palindrome_count = 0
    for s in strings:
        if is_palindrome_slice(s):
            palindrome_count += 1
    end = time.perf_counter()

    # 実行時間をミリ秒に変換
    elapsed_ms = (end - start) * 1000

    # 結果出力
    print("=== 文字列処理（回文判定） - スライス版 ===")
    print(f"言語: Python (slice/C layer)")
    print(f"判定回数: {count:,}")
    print(f"回文の数: {palindrome_count:,}")
    print(f"実行時間: {elapsed_ms:.2f} ms")


if __name__ == "__main__":
    main()
