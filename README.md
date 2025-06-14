# Qwen2.5-7B-Instruct Math Problem Solving Model

[English](README.md) | [中文](README_zh.md)

This project is based on the Qwen2.5-7B-Instruct model, utilizing LoRA (Low-Rank Adaptation) for fine-tuning, specifically designed for mathematical multiple-choice question answering tasks.

## Dataset

This project uses the Math Multiple Choice QA (MMCQA) dataset, a natural language understanding task focused on mathematical problems. Given a question and multiple choices, the goal is to select the correct answer.

Example:
```
Question: Ali is a dean of a private school where he teaches one class. John is also a dean of a public school. John has two classes in his school. Each class has 1/8 the capacity of Ali's class, which has the capacity of 120 students. What is the combined capacity of both schools?
Choices: A. 947 B. 899 C. 150 D. 803
Answer: 2
```

## Requirements

- Python 3.10.8
- Swift 2.6.1
- CUDA 11.7+ (recommended for training and inference)
- 16GB+ RAM (recommended for model loading and inference)

## Project Structure

```
.
├── img/                    # Image resources directory
├── model/                  # Model files directory
├── llm_api_in_context.py   # LLM API implementation with examples
├── llm_api.py             # Basic LLM API implementation
├── local_llm_math_submit.py # Local model submission implementation
├── test_acc.py            # Test accuracy calculation script
├── train_mc_swift.json    # Training data in Swift format
├── convert_to_swift_format.py # Data format conversion script
├── test_sample.csv        # Test sample data (10 questions for quick validation)
└── test.csv              # Complete test dataset
```

## Core Features

### 1. Data Preprocessing
- Data format conversion: Convert original JSONL format to Swift training JSON format
- Data cleaning: Ensure data format consistency, remove abnormal samples
- Example construction: Generate training data with rich examples

### 2. Model Training
- Based on Qwen2.5-7B-Instruct pre-trained model
- Parameter-efficient fine-tuning using LoRA
- Distributed training using Swift framework
- Support for checkpoint saving and resuming training

### 3. Model Inference
- Local model inference: Support for CPU and GPU inference
- API inference: Support for multiple API interfaces
- Context learning: Enhanced inference with rich examples
- Batch processing: Efficient inference for large-scale data

### 4. Evaluation and Testing
- Accuracy evaluation: Detailed evaluation metrics
- Quick validation: Using test_sample.csv for rapid model validation
- Complete testing: Using test.csv for full performance evaluation

## Quick Start

1. **Environment Setup**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Data Preparation**:
   ```bash
   python convert_to_swift_format.py
   ```

3. **Model Training**:
   ```bash
   swift train.py
   ```

4. **Quick Validation**:
   ```bash
   python test_acc.py --test_file test_sample.csv
   ```

5. **Complete Testing**:
   ```bash
   python test_acc.py --test_file test.csv
   ```

6. **Generate Predictions**:
   ```bash
   # Local model inference
   python local_llm_math_submit.py
   
   # API inference
   python llm_api_in_context.py
   ```

## Model Performance

The model excels in the following types of mathematical problems:
- Basic arithmetic operations
- Algebraic equation solving
- Geometric problems
- Word problems
- Ratio and percentage calculations
- Time, distance, and speed problems
- Probability and statistics

## Best Practices

1. **Hardware Configuration**:
   - Recommended to use GPU for training and inference
   - Ensure sufficient VRAM (16GB+ recommended)
   - Use SSD for training data storage

2. **API Usage**:
   - Securely store API keys
   - Implement request rate limiting and error retry
   - Monitor API call costs

3. **Model Deployment**:
   - Use model quantization to reduce model size
   - Implement model caching mechanism
   - Configure appropriate batch sizes

