/// 文字列処理（回文判定） - パフォーマンス検証（Rust）

use std::time::Instant;

/// 文字列が回文かどうか判定する
fn is_palindrome(s: &[u8]) -> bool {
    let length = s.len();
    for i in 0..length / 2 {
        if s[i] != s[length - 1 - i] {
            return false;
        }
    }
    true
}

/// テスト用文字列を生成する（回文と非回文を混在）
fn generate_test_strings(count: usize) -> Vec<String> {
    let mut strings = Vec::with_capacity(count);
    let base: String = "abcdefghij".repeat(10); // 100文字

    for i in 0..count {
        let s = if i % 2 == 0 {
            // 回文を作る
            let half = &base[..50];
            let rev: String = half.chars().rev().collect();
            format!("{}{}", half, rev)
        } else {
            // 非回文
            format!("{}{}", base, i)
        };
        strings.push(s);
    }
    strings
}

fn main() {
    let count: usize = 1_000_000; // 100万回判定

    // テストデータ生成（計測対象外）
    let strings = generate_test_strings(count);

    // 計測開始
    let start = Instant::now();
    let mut palindrome_count: usize = 0;
    for s in &strings {
        if is_palindrome(s.as_bytes()) {
            palindrome_count += 1;
        }
    }
    let elapsed = start.elapsed();

    // 実行時間をミリ秒に変換
    let elapsed_ms = elapsed.as_secs_f64() * 1000.0;

    // 結果出力
    println!("=== 文字列処理（回文判定） ===");
    println!("言語: Rust");
    println!("判定回数: {}", count);
    println!("回文の数: {}", palindrome_count);
    println!("実行時間: {:.2} ms", elapsed_ms);
}
