#!/bin/bash

CUDA_VISIBLE_DEVICES=0 \
NNODES=1 \
NODE_RANK=0 \
MASTER_ADDR=127.0.0.1 \
NPROC_PER_NODE=1 \
swift sft \
    --model_type qwen1half-7b \
    --model_id_or_path /root/autodl-tmp/Qwen2.5-7B-Instruct \
    --dataset /root/code/train_mc_swift.json \
    --output_dir output/generated_model/lora_result \
    --check_model_is_latest false \
    --deepspeed default-zero2 \
    --num_train_epochs 30