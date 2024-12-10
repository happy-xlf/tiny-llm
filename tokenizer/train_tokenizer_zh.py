#!/usr/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   train_tokenizer_zh.py
@Time    :   2024/12/10 21:50:27
@Author  :   Lifeng Xu 
@desc :   
'''
import sentencepiece as spm
import os
import glob

def tain_chinses_spm(input_txt_dir, vocab_size, output_dir="."):
    # 保存的模型名称
    prefix = os.path.join(output_dir, f"chinese_spm_{vocab_size}")

    text_filenames = sorted(glob.glob(os.path.join(input_txt_dir, "*.txt")))
    print("file list: ", text_filenames)

    # 2) train the sentencepiece model
    print("Will now train the vocab...")
    spm.SentencePieceTrainer.train(input=text_filenames,
                                   model_prefix=prefix,
                                   model_type="bpe",
                                   vocab_size=vocab_size,
                                   self_test_sample_size=0,
                                   input_format="text",
                                   character_coverage=0.9995,
                                   num_threads=os.cpu_count(),
                                   split_digits=True,       # 是否将数字划分为单个 token, 在 llama 中是这么做的
                                   allow_whitespace_only_pieces=True,
                                   byte_fallback=True,
                                   unk_surface=r" \342\201\207 ",
                                   max_sentence_length=24000)


    print(f"Trained tokenizer is in {prefix}.model")
    print("Done.")

def test_chinese_spm(spm_model_path):
    sp_bpe = spm.SentencePieceProcessor() 
    sp_bpe.load(spm_model_path)
    print('*** BPE ***')
    print(sp_bpe.encode_as_pieces('萧峰一抬头，远远望出去，只见东面、北面、南面三方，辽军长矛的矛头犹如树林般刺向天空，竟然已经合围。'))
    print(len(sp_bpe.encode_as_pieces('萧峰一抬头，远远望出去，只见东面、北面、南面三方，辽军长矛的矛头犹如树林般刺向天空，竟然已经合围。')))

if __name__ == "__main__":
    # input_txt_dir = "doc_data"
    # vocab_size = 20000
    # output_dir = "sp_output"
    # tain_chinses_spm(input_txt_dir, vocab_size, output_dir)

    spm_model_path = "./sp_output/chinese_spm_20000.model"
    test_chinese_spm(spm_model_path)