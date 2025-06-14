import csv
import ast
from openai import OpenAI
import re

client = OpenAI(
    api_key="sk-zZN8G1vgTHXTjpXKPskN9l6FgzReYqhFxCMZsLNEynx6vHV4",
    base_url="https://api.chatanywhere.tech/v1"
)

# 读取测试集
test_file = 'test_sample.csv'
# test_file = 'test.csv'
output_file = 'my_submission.csv'

results = []

# 先统计总行数
total = 0
with open(test_file, newline='', encoding='utf-8') as csvfile:
    total = sum(1 for _ in csvfile) - 1  # 去掉表头

with open(test_file, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for idx, row in enumerate(reader, 1):
        print(f"正在处理第{idx}/{total}题……")
        qid = row['Id']
        question = row['Question']
        choices = ast.literal_eval(row['Choices'])
        # 构造 prompt
        # prompt = f"请从以下选项中选择最优答案，并只输出选项的索引（从0开始）。注意！是输出答案选项的索引！而不是输出答案内容！\n问题：{question}\n选项：{choices}"
        prompt = f"""请仔细阅读以下数学问题，并从选项中选出正确答案。请严格按照格式输出答案。

示例：
问题：Martin spends 2 hours waiting in traffic, then four times that long trying to get off the freeway. How much time does he waste total?
选项：[620, 10, 536, 379]
答案是：1

现在请回答以下问题：
问题：{question}
选项：{choices}

请只输出"答案是："后跟选项的索引（从0开始）。例如：答案是：1"""
        messages = [{'role': 'user', 'content': prompt}]
        # 调用 LLM API
        completion = client.chat.completions.create(model="deepseek-v3", messages=messages)
        content = completion.choices[0].message.content.strip()
        print(f"模型输出: {content}")
        
        # 使用正则表达式匹配"答案是："后面的数字
        match = re.search(r'答案是：\s*(\d+)', content)
        if match:
            label = int(match.group(1))
        else:
            # 如果没有找到"答案是："，尝试直接提取数字
            match = re.search(r'\b(\d+)\b', content)
            label = int(match.group(1)) if match else 0

        print(f"第{idx}/{total}题答案：{label}")
        results.append({'Id': qid, 'label': label})

# 写入结果文件
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Id', 'label'])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"结果已保存到 {output_file}") 