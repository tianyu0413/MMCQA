# Qwen2.5-7B-Instruct Math Problem Solving Model

[English](docs/README.md) | [中文](docs/README_zh.md)

This project implements a mathematical problem-solving model based on Qwen2.5-7B-Instruct, fine-tuned using LoRA (Low-Rank Adaptation) for multiple-choice question answering.

## Dataset

The project uses the Math Multiple Choice QA (MMCQA) dataset, which focuses on mathematical problem-solving through natural language understanding. Each problem consists of a question and multiple answer choices.

Example:
```
Question: Ali is a dean of a private school where he teaches one class. John is also a dean of a public school. John has two classes in his school. Each class has 1/8 the capacity of Ali's class, which has the capacity of 120 students. What is the combined capacity of both schools?
Choices: A. 947 B. 899 C. 150 D. 803
Answer: 2
```

## Requirements

- Python 3.10.8
- Swift 2.6.1
- CUDA 11.7+ (for training and inference)
- 16GB+ RAM (for model loading and inference)

## Project Structure

```
.
├── src/                    # Source code
│   └── utils/             # Utility functions
│       └── convert_to_swift_format.py
├── scripts/               # Training and evaluation scripts
├── tests/                 # Test files
│   └── test_acc.py
├── data/                  # Data files
│   ├── raw/              # Raw data
│   │   ├── train_mc.jsonl
│   │   ├── test.csv
│   │   └── test_sample.csv
│   └── processed/        # Processed data
│       └── train_mc_swift.json
├── docs/                  # Documentation
│   ├── README.md
│   └── README_zh.md
├── config/               # Configuration files
├── img/                  # Image resources
├── model/                # Model files
├── llm_api.py           # API implementation
├── llm_api_in_context.py # Context-aware API implementation
├── local_llm_math_submit.py # Local model inference
├── train.sh             # Training script
└── requirements.txt      # Python dependencies
```

## Features

1. **Data Processing**
   - JSONL to Swift format conversion
   - Data validation and cleaning
   - Example generation for training

2. **Model Training**
   - Qwen2.5-7B-Instruct base model
   - LoRA fine-tuning
   - Swift-based distributed training
   - Checkpoint management

3. **Inference**
   - Local CPU/GPU inference
   - API-based inference
   - Context-aware prediction
   - Batch processing support

4. **Evaluation**
   - Accuracy metrics
   - Sample validation
   - Full dataset testing

## Getting Started

1. **Setup Environment**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Prepare Data**:
   ```bash
   python src/utils/convert_to_swift_format.py
   ```

3. **Train Model**:
   ```bash
   ./train.sh
   ```


4. **Generate Predictions**:
   ```bash
   # Local inference
   python local_llm_math_submit.py
   
   # API inference
   python llm_api_in_context.py
   ```

5. **Run Tests**:
```bash
# Quick test 10
python tests/test_acc.py

```

## Supported Problem Types

- Arithmetic operations
- Algebraic equations
- Geometry
- Word problems
- Ratios and percentages
- Time, distance, and speed
- Probability and statistics

## Configuration

1. **Environment Variables**
   - Set `OPENAI_API_KEY` for API access
   - Set `OPENAI_API_BASE` for custom API endpoint

2. **Hardware Requirements**
   - GPU with 16GB+ VRAM recommended
   - SSD storage for data
   - 16GB+ system RAM

3. **Model Settings**
   - Adjust batch size based on available memory
   - Configure model quantization as needed
   - Set appropriate cache parameters

