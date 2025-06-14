import csv

# 正确答案列表
correct_answers = [2, 2, 2, 3, 1, 3, 3, 1, 3, 3]

# 读取提交的答案
submitted_answers = []
with open('my_submission.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        submitted_answers.append(int(row['label']))

# 计算正确率
correct_count = 0
total = len(correct_answers)

print("题目对比：")
print("题号\t提交答案\t正确答案\t是否正确")
print("-" * 40)

for i in range(total):
    is_correct = submitted_answers[i] == correct_answers[i]
    if is_correct:
        correct_count += 1
    print(f"{i+1}\t{submitted_answers[i]}\t{correct_answers[i]}\t{'✓' if is_correct else '✗'}")

accuracy = (correct_count / total) * 100
print("\n统计结果：")
print(f"总题数：{total}")
print(f"正确数：{correct_count}")
print(f"正确率：{accuracy:.2f}%") 