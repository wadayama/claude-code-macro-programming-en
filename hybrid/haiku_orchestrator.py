#!/usr/bin/env python3
"""
俳句ジェネレータ Pythonオーケストレータ
A.15 Pythonオーケストレーション型ハイブリッドアプローチの実践例
"""

import subprocess
import concurrent.futures
from variable_db import save_variable, VariableDB


def run_macro(macro_file):
    """マクロファイルを実行"""
    with open(macro_file, 'r', encoding='utf-8') as f:
        subprocess.run(["claude", "-p", "--dangerously-skip-permissions"], stdin=f)


def create_agent_macro(agent_id):
    """エージェント専用マクロを生成"""
    import os
    
    # agents/フォルダが存在しない場合は作成
    os.makedirs('agents', exist_ok=True)
    
    with open('agent_template.md', 'r', encoding='utf-8') as f:
        template = f.read()
    
    content = template.replace('{{AGENT_ID}}', str(agent_id))
    filename = f'agents/agent_{agent_id}.md'
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filename


def run_agent(agent_id):
    """エージェント実行"""
    macro_file = create_agent_macro(agent_id)
    run_macro(macro_file)
    return agent_id


def main():
    print("=== 俳句生成マルチエージェントシステム開始 ===")
    
    # 初期化
    import os
    import glob
    
    # 変数クリア
    count = VariableDB().clear_all()
    print(f"🔄 {count}個の変数をクリア")
    
    # agents/フォルダ内のファイルをクリア
    for file in glob.glob('agents/agent_*.md'):
        os.remove(file)
    print("🔄 agents/フォルダをクリア")
    
    # 設定
    agent_count = 3

    save_variable('agent_count', str(agent_count))
    
    # テーマ生成
    run_macro('generate_themes.md')
    
    # 並列俳句生成
    with concurrent.futures.ThreadPoolExecutor() as executor:
        list(executor.map(run_agent, range(1, agent_count + 1)))
    
    # 評価
    run_macro('evaluate_haiku.md')
    
    print("=== 俳句生成マルチエージェントシステム完了 ===")


if __name__ == "__main__":
    main()