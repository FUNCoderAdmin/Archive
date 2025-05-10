from pathlib import Path

def main():
    # Gather inputs
    day = input('何曜日ですか（例: Mon, Tue, Wed, Thu, Fri）: ').strip()
    week = input('何週目（例: week2）: ').strip()
    virtual_link = input('バーチャルコンテストのリンクを入力してください: ').strip()

    # Collect problems
    problems = []
    print('問題を入力します。終了するにはEnterを押してください。')
    while True:
        contest_id = input('コンテストID（例: abc397）: ').strip()
        if not contest_id:
            break
        problem_id = input('問題ID（例: A）: ').strip()
        problem_name = input('問題名（例: Thermometer）: ').strip()
        problem_link = input('問題リンク（URL）: ').strip()
        solution_link = input('解答例リンク（URL）: ').strip()
        problems.append({
            'contest_id': contest_id,
            'problem_id': problem_id,
            'problem_name': problem_name,
            'problem_link': problem_link,
            'solution_link': solution_link,
        })
        print('--- 次の問題 ---')

    # Prepare directory
    dir_path = Path(f"./{day}/{week}")
    dir_path.mkdir(parents=True, exist_ok=True)
    readme_path = dir_path / 'README.md'

    # Build README content
    lines = []
    lines.append(f"# 第{week.replace('week', '')}回活動記録")
    lines.append("")
    lines.append("## バーチャルコンテスト")
    lines.append("")
    lines.append(f"> [FUNCoder 第{week.replace('week', '')}回活動]({virtual_link})")
    lines.append("")
    lines.append("### 問題リンク一覧")
    lines.append("")
    for p in problems:
        lines.append(f"- [{p['problem_id']} - {p['problem_name']}]({p['problem_link']})")
    lines.append("")

    for p in problems:
        lines.append(f"### {p['problem_id']} - {p['problem_name']}")
        lines.append("")
        lines.append(f"> [{p['problem_id']} - {p['problem_name']}]({p['problem_link']})")
        lines.append("")
        lines.append("#### 解答・解説 <!-- markdownlint-disable-line MD024 -->")
        lines.append("")
        lines.append(f"> [解答例1]({p['solution_link']})")
        lines.append("")

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(lines))

    print(f"README.md を作成しました: {readme_path}")

if __name__ == '__main__':
    main()