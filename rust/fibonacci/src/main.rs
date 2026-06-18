/// フィボナッチ数列 再帰計算 - パフォーマンス検証（Rust）

use std::time::Instant;

/// 素朴な再帰によるフィボナッチ数計算（メモ化なし）
fn fibonacci(n: u64) -> u64 {
    if n <= 1 {
        return n;
    }
    fibonacci(n - 1) + fibonacci(n - 2)
}

fn main() {
    let n: u64 = 40;

    // 計測開始
    let start = Instant::now();
    let result = fibonacci(n);
    let elapsed = start.elapsed();

    // 実行時間をミリ秒に変換
    let elapsed_ms = elapsed.as_secs_f64() * 1000.0;

    // 結果出力
    println!("=== フィボナッチ数列 再帰計算 ===");
    println!("言語: Rust");
    println!("N: {}", n);
    println!("結果: {}", result);
    println!("実行時間: {:.2} ms", elapsed_ms);
}
