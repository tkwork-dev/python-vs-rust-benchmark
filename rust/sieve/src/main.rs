/// 素数計算（エラトステネスの篩） - パフォーマンス検証（Rust）

use std::time::Instant;

/// エラトステネスの篩で limit 以下の素数を列挙する
fn sieve_of_eratosthenes(limit: usize) -> Vec<usize> {
    let mut is_prime = vec![true; limit + 1];
    is_prime[0] = false;
    is_prime[1] = false;

    let mut i = 2;
    while i * i <= limit {
        if is_prime[i] {
            let mut j = i * i;
            while j <= limit {
                is_prime[j] = false;
                j += i;
            }
        }
        i += 1;
    }

    let mut primes = Vec::new();
    for i in 2..=limit {
        if is_prime[i] {
            primes.push(i);
        }
    }
    primes
}

fn main() {
    let limit: usize = 10_000_000; // 1000万

    // 計測開始
    let start = Instant::now();
    let primes = sieve_of_eratosthenes(limit);
    let elapsed = start.elapsed();

    // 実行時間をミリ秒に変換
    let elapsed_ms = elapsed.as_secs_f64() * 1000.0;

    // 結果出力
    println!("=== 素数計算（エラトステネスの篩） ===");
    println!("言語: Rust");
    println!("上限: {}", limit);
    println!("素数の個数: {}", primes.len());
    println!("最大の素数: {}", primes.last().unwrap());
    println!("実行時間: {:.2} ms", elapsed_ms);
}
