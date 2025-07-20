# 自然言語マクロ スキーマ検証テスト

統合型チェック機能付き変数管理システムの動作検証テスト

## 使用可能なスキーマ定義

このテストで使用するスキーマは `test_schema.json` で定義されています。

**利用可能なスキーマ一覧**:

### 基本型
- **integer**: 整数値
- **number**: 数値（整数・小数）
- **string**: 文字列
- **boolean**: 真偽値（true/false）

### 制約付き型
- **age**: 整数、範囲 0-150（年齢）
- **percentage**: 数値、範囲 0-100（パーセンテージ）
- **status**: 文字列、値は "pending", "completed", "failed" のいずれか

## 環境初期化

全ての変数をクリアしてください

## 基本型検証

### 整数型

25をinteger型として{{user_age}}に保存してください

{{user_age}}を取得してください

### 数値型  

3.14をnumber型として{{pi_value}}に保存してください

{{pi_value}}を取得してください

### 文字列型

"Hello, Schema!"をstring型として{{message}}に保存してください

{{message}}を取得してください

### 真偽値型

trueをboolean型として{{is_enabled}}に保存してください

{{is_enabled}}を取得してください

## 制約付き型検証

### 年齢制約（0-150）

30をage型として{{current_age}}に保存してください

{{current_age}}を取得してください

### パーセンテージ制約（0-100）

75をpercentage型として{{completion}}に保存してください

{{completion}}を取得してください

### ステータス列挙制約

completedをstatus型として{{task_status}}に保存してください

{{task_status}}を取得してください

## 型チェック機能

全ての変数の型チェックを実行してください

## エラーケース検証

以下は意図的にスキーマ違反を発生させ、エラーハンドリングを確認するテストです。

### 範囲制約違反

-5をage型として{{invalid_age}}に保存してください

1.5をpercentage型として{{invalid_pct}}に保存してください

### 列挙制約違反

unknownをstatus型として{{invalid_status}}に保存してください

### 型制約違反

"not_a_number"をinteger型として{{invalid_int}}に保存してください

## 日本語文字列対応

"こんにちは、型安全な世界！"をstring型として{{japanese_text}}に保存してください

{{japanese_text}}を取得してください

## 基本保存（型チェックなし）との比較

型指定なしでの保存をテストしてください：

{{untyped_var}}に"任意の値"を保存してください

{{untyped_var}}を取得してください

## 最終確認

全ての変数の型チェックを実行してください