# Qwen2.5-7B-Instruct 数学问题求解模型

[English](README.md) | [中文](README_zh.md)

本项目基于Qwen2.5-7B-Instruct模型，使用LoRA（低秩适应）进行微调，专门用于数学选择题解答任务。

## 数据集

本项目使用数学选择题问答（MMCQA）数据集，该数据集专注于通过自然语言理解解决数学问题。每个问题包含一个问题和多个选项。

示例：
```
问题：Ali是一所私立学校的校长，他在那里教一个班。John也是一所公立学校的校长。John的学校有两个班。每个班的容量是Ali班级的1/8，Ali的班级容量为120名学生。两所学校的总容量是多少？
选项：A. 947 B. 899 C. 150 D. 803
答案：2
```

## 环境要求

- Python 3.10.8
- Swift 2.6.1
- CUDA 11.7+（用于训练和推理）
- 16GB+ 内存（用于模型加载和推理）

## 项目结构

```
.
├── src/                    # 源代码
│   └── utils/             # 工具函数
│       └── convert_to_swift_format.py
├── scripts/               # 训练和评估脚本
├── tests/                 # 测试文件
│   └── test_acc.py
├── data/                  # 数据文件
│   ├── raw/              # 原始数据
│   │   ├── train_mc.jsonl
│   │   ├── test.csv
│   │   └── test_sample.csv
│   └── processed/        # 处理后数据
│       └── train_mc_swift.json
├── docs/                  # 文档
│   ├── README.md
│   └── README_zh.md
├── config/               # 配置文件
├── img/                  # 图片资源
├── model/                # 模型文件
├── llm_api.py           # API实现
├── llm_api_in_context.py # 上下文感知API实现
├── local_llm_math_submit.py # 本地模型推理
├── train.sh             # 训练脚本
└── requirements.txt      # Python依赖
```

## 功能特点

1. **数据处理**
   - JSONL到Swift格式转换
   - 数据验证和清洗
   - 训练示例生成

2. **模型训练**
   - Qwen2.5-7B-Instruct基础模型
   - LoRA微调
   - 基于Swift的分布式训练
   - 检查点管理

3. **推理**
   - 本地CPU/GPU推理
   - API推理
   - 上下文感知预测
   - 批处理支持

4. **评估**
   - 准确率指标
   - 样本验证
   - 完整数据集测试

## 快速开始

1. **环境配置**：
   ```bash
   pip install -r requirements.txt
   ```

2. **数据准备**：
   ```bash
   python src/utils/convert_to_swift_format.py
   ```

3. **模型训练**：
   ```bash
   ./train.sh
   ```

4. **生成预测**：
   ```bash
   # 本地推理
   python local_llm_math_submit.py
   
   # API推理
   python llm_api_in_context.py
   ```

5. **运行测试**：
   ```bash
   # 快速测试 10 题准确率
   python tests/test_acc.py
   ```

## 支持的问题类型

- 算术运算
- 代数方程
- 几何问题
- 文字题
- 比例和百分比
- 时间、距离和速度
- 概率和统计

## 配置说明

1. **环境变量**
   - 设置`OPENAI_API_KEY`用于API访问
   - 设置`OPENAI_API_BASE`用于自定义API端点

2. **硬件要求**
   - 建议使用16GB+显存的GPU
   - 使用SSD存储数据
   - 16GB+系统内存

3. **模型设置**
   - 根据可用内存调整批次大小
   - 根据需要配置模型量化
   - 设置适当的缓存参数 