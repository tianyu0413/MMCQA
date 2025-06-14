# Qwen2.5-7B-Instruct 数学问题求解模型

[English](docs/README.md) | [中文](docs/README_zh.md)

本项目基于Qwen2.5-7B-Instruct模型，采用LoRA（Low-Rank Adaptation）方法进行微调，专门用于解决数学选择题的自然语言理解任务。

## 数据集

本项目使用Math Multiple Choice QA (MMCQA)数据集，这是一个专注于数学问题的自然语言理解任务。给定一个问题和多个选项，目标是选择正确答案。

示例：
```
问题：Ali是一所私立学校的校长，他教授一个班级。John也是一所公立学校的校长。John的学校有两个班级。每个班级的容量是Ali班级容量的1/8，Ali的班级容量为120名学生。两所学校的总容量是多少？
选项：A. 947 B. 899 C. 150 D. 803
答案：2
```

## 环境要求

- Python 3.10.8
- Swift 2.6.1
- CUDA 11.7+ (推荐用于训练和推理)
- 16GB+ RAM (推荐用于模型加载和推理)

## 项目结构

```
.
├── src/                    # 源代码目录
│   ├── api/               # API相关代码
│   │   ├── llm_api.py
│   │   └── llm_api_in_context.py
│   ├── models/            # 模型相关代码
│   │   └── local_llm_math_submit.py
│   └── utils/             # 工具函数
│       └── convert_to_swift_format.py
├── scripts/               # 训练和评估脚本
│   └── train.sh
├── tests/                 # 测试文件
│   └── test_acc.py
├── data/                  # 数据目录
│   ├── raw/              # 原始数据文件
│   │   ├── train_mc.jsonl
│   │   ├── test.csv
│   │   └── test_sample.csv
│   └── processed/        # 处理后的数据文件
│       └── train_mc_swift.json
├── docs/                  # 文档
│   ├── README.md
│   └── README_zh.md
├── config/               # 配置文件
├── img/                  # 图片资源
├── model/                # 模型文件
└── requirements.txt      # Python依赖
```

## 核心功能

### 1. 数据预处理
- 数据格式转换：将原始JSONL格式转换为Swift训练所需的JSON格式
- 数据清洗：确保数据格式统一，移除异常样本
- 示例构建：生成包含丰富示例的训练数据

### 2. 模型训练
- 基于Qwen2.5-7B-Instruct预训练模型
- 采用LoRA方法进行参数高效微调
- 使用Swift框架进行分布式训练
- 支持断点续训和模型检查点保存

### 3. 模型推理
- 本地模型推理：支持CPU和GPU推理
- API调用推理：支持多种API接口
- 上下文学习：提供丰富的示例增强推理能力
- 批量处理：支持大规模数据的高效推理

### 4. 评估与测试
- 准确率评估：提供详细的评估指标
- 快速验证：使用test_sample.csv进行模型快速验证
- 完整测试：使用test.csv进行完整性能评估

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
   ./scripts/train.sh
   ```

4. **快速验证**：
   ```bash
   python tests/test_acc.py --test_file data/raw/test_sample.csv
   ```

5. **完整测试**：
   ```bash
   python tests/test_acc.py --test_file data/raw/test.csv
   ```

6. **生成预测结果**：
   ```bash
   # 本地模型推理
   python src/models/local_llm_math_submit.py
   
   # API调用推理
   python src/api/llm_api_in_context.py
   ```

## 模型性能

模型在以下类型的数学问题上表现出色：
- 基础算术运算
- 代数方程求解
- 几何问题
- 应用题
- 比例和百分比计算
- 时间、距离和速度问题
- 概率统计问题

## 最佳实践

1. **硬件配置**：
   - 推荐使用GPU进行训练和推理
   - 确保有足够的显存（建议16GB+）
   - 使用SSD存储训练数据

2. **API使用**：
   - 妥善保管API密钥
   - 实现请求限流和错误重试
   - 监控API调用成本

3. **模型部署**：
   - 使用模型量化减小模型体积
   - 实现模型缓存机制
   - 配置适当的批处理大小 