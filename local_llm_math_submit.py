import csv
import ast
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel
import time
import re

# 配置模型路径
base_model_id = "/root/autodl-tmp/Qwen2.5-7B-Instruct"
lora_checkpoint_dir = "/root/code/output/generated_model/lora_result/qwen1half-32b/v0-20241211-232430/checkpoint-50"

# 文件路径
test_file = 'test_sample.csv'
output_file = 'my_submission.csv'

# 是否使用 LoRA 微调的模型
use_lora = False  # 设置为 False 表示仅使用基座模型

# 加载 tokenizer
tokenizer = AutoTokenizer.from_pretrained(base_model_id)

# 加载模型
if use_lora:
    # 先加载基座模型
    model = AutoModelForCausalLM.from_pretrained(base_model_id, torch_dtype=torch.bfloat16, device_map="auto")
    # 加载 LoRA 微调权重
    model = PeftModel.from_pretrained(model, lora_checkpoint_dir)
else:
    # 仅加载基座模型
    model = AutoModelForCausalLM.from_pretrained(base_model_id, torch_dtype=torch.bfloat16, device_map="auto")

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
        prompt = f"请从以下选项中选择最优答案，并只输出选项的索引（从0开始）。注意！是输出答案选项的索引！而不是输出答案内容！\n问题：{question}\n选项：{choices}"
        
        # 记录开始时间
        start_time = time.time()
        
        # 模型生成结果
        inputs = tokenizer(prompt, return_tensors="pt").to(0)
        
        try:
            # 模型生成
            outputs = model.generate(**inputs, max_new_tokens=20)
            # 解码生成的文本
            content = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # 去除 prompt 部分，只保留模型生成的新增文本
            if content.startswith(prompt):
                content = content[len(prompt):].strip()
            
            print(f"模型输出: {content}")
            
            # 使用正则表达式匹配"答案是："后面的数字
            match = re.search(r'答案是：\s*(\d+)', content)
            if match:
                label = int(match.group(1))
            else:
                # 如果没有找到"答案是："，尝试直接提取数字
                match = re.search(r'\b(\d+)\b', content)
                label = int(match.group(1)) if match else 0
                
        except Exception as e:
            print(f"生成过程中出错: {e}")
            label = 0  # fallback
            
        # 记录结束时间
        end_time = time.time()
        inference_time = end_time - start_time
        
        print(f"第{idx}/{total}题答案：{label}")
        print(f"推理时间：{inference_time:.4f}秒")
        
        results.append({'Id': qid, 'label': label})

# 写入结果文件
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Id', 'label'])
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"结果已保存到 {output_file}") 