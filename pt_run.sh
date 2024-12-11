python ptm_train.py --do_train --output_dir ../output --per_device_train_batch_size 4 --gradient_accumulation_steps 8 --lr_scheduler_type cosine --logging_steps 10 --warmup_ratio 0.1 --save_steps 100 --learning_rate 5e-5 --num_train_epochs 3.0 --fp16

python ptm_train.py --do_train --output_dir ../output --per_device_train_batch_size 4 --gradient_accumulation_steps 8 --num_train_epochs 3 --logging_strategy steps --logging_steps 10 --weight_decay 0.01 --adam_beta1 0.9 --adam_beta1 0.95 --max_grad_norm 1 --lr_scheduler_type "cosine" --learning_rate 3e-4 --warmup_ratio 0.05 --weight_decay 0.01 --save_strategy steps --save_total_limit 3 --save_steps 100 --ddp_timeout 30000 --logging_first_step True --save_safetensors False --ddp_find_unused_parameters False

