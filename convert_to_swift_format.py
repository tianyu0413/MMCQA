import json
import ast

def convert_to_swift_format():
    # 输入和输出文件
    input_file = 'train_mc.jsonl'
    output_file = 'train_mc_swift.json'
    
    # 存储转换后的数据
    swift_data = []
    
    # 读取原始数据
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                question = data.get('Question', '')
                choices = data.get('Choices', [])
                answer = data.get('label', '')
                
                # 构造新的数据格式，保持与local_llm_math_submit.py中的prompt格式一致
                swift_item = {
                    "instruction": "请从以下选项中选择最优答案，并只输出选项的索引（从0开始）。注意！是输出答案选项的索引！而不是输出答案内容！",
                    "input": f"问题：{question}\n选项：{choices}",
                    "output": f"答案是：{answer}"  # 修改输出格式，添加"答案是："前缀
                }
                
                swift_data.append(swift_item)
                
            except Exception as e:
                print(f"处理数据时出错: {e}")
                continue
    
    # 保存转换后的数据
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(swift_data, f, ensure_ascii=False, indent=2)
    
    print(f"转换完成！共处理 {len(swift_data)} 条数据")
    print(f"结果已保存到 {output_file}")

if __name__ == "__main__":
    convert_to_swift_format() 