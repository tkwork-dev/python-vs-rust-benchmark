/// 行列積（N×N） - パフォーマンス検証（Rust）

use std::time::Instant;

/// N×N行列の積を計算する（三重ループ）
fn matrix_multiply(a: &[Vec<f64>], b: &[Vec<f64>], n: usize) -> Vec<Vec<f64>> {
    let mut c = vec![vec![0.0f64; n]; n];

    for i in 0..n {
        for j in 0..n {
            let mut s = 0.0f64;
            for k in 0..n {
                s += a[i][k] * b[k][j];
            }
            c[i][j] = s;
        }
    }
    c
}

/// テスト用の行列を生成する（要素 = (i * n + j + 1) % 100）
fn create_matrix(n: usize) -> Vec<Vec<f64>> {
    (0..n)
        .map(|i| (0..n).map(|j| ((i * n + j + 1) % 100) as f64).collect())
        .collect()
}

fn main() {
    let n: usize = 200; // 200x200行列

    let a = create_matrix(n);
    let b = create_matrix(n);

    // 計測開始
    let start = Instant::now();
    let c = matrix_multiply(&a, &b, n);
    let elapsed = start.elapsed();

    // 実行時間をミリ秒に変換
    let elapsed_ms = elapsed.as_secs_f64() * 1000.0;

    // 結果出力
    println!("=== 行列積（N×N） ===");
    println!("言語: Rust");
    println!("サイズ: {}x{}", n, n);
    println!("C[0][0]: {:.0}", c[0][0]);
    println!("C[{}][{}]: {:.0}", n - 1, n - 1, c[n - 1][n - 1]);
    println!("実行時間: {:.2} ms", elapsed_ms);
}
