## Tiny LLM  项目数据集

此数据用于项目[wdndev/tiny-llm-zh (github.com)](https://github.com/wdndev/tiny-llm-zh)的训练，详细训练过程，见github项目。

### 1.训练数据

本次训练的预训练预料都来自[Hugging Face](https://huggingface.co/)，主要包含以下几个经典的中文数据集，大约有35B左右Token，详细数据集如下：

| 中文预训练语料    | 链接                                                         | 描述                                            |
| ----------------- | ------------------------------------------------------------ | ----------------------------------------------- |
| Wiki中文百科      | [wikipedia](https://huggingface.co/datasets/pleisto/wikipedia-cn-20230720-filtered) | 中文Wikipedia的数据                             |
| BaiduBaiKe        | [baidubaike](https://huggingface.co/datasets/xuqinyang/BaiduBaike-5.63M) | 中文BaiduBaiKe的数据                            |
| zhihu             | [zhihu](https://huggingface.co/datasets/wangrui6/Zhihu-KOL)  | 知乎KOL中截取的数据                             |
| 网络小说      | [webnovel](https://huggingface.co/datasets/wdndev/webnovel-chinese) | 个人爬虫数据清洗的数据                             |
| TigerBot 部分数据 | [tigerBot](https://huggingface.co/datasets/TigerResearch/pretrain_zh) | TigerBot 模型训练的部分中文数据，原始数据太多了 |
| c4_zh | [chinese-c4](https://huggingface.co/datasets/shjwudp/chinese-c4) | 清洗后的C4中文数据集 |
| wanjuan | [wanjuan](https://opendatalab.com/OpenDataLab/WanJuan1_dot_0) | 清洗过后的万卷中文数据 |

上述数据处理脚本为，在处理时，Tokenizer后保存为可直接训练的二进制文件(`.bin`)。

注意：此处使用二进制文件保存，不需要考虑每个 max_seq_len 的长度，尽可能压缩存储空间。后续的SFT执行微调数据和RLHF数据集是较小，不需要提前保存为二进制文件。


### 2.微调数据

SFT指令微调预料都来自[Hugging Face](https://huggingface.co/)，主要包含以下几个经典的SFT数据集，大约有400w条，详细数据集如下：

| SFT微调数据 | 链接                                                         | 描述                                       |
| ----------- | ------------------------------------------------------------ | ------------------------------------------ |
| Belle       | [Belle](https://huggingface.co/datasets/BelleGroup/train_2M_CN) | 包含约200万条由BELLE项目生成的中文指令数据 |
| Firefly     | [Firefly](https://huggingface.co/datasets/YeungNLP/firefly-train-1.1M) | 流萤开源模型SFT数据集                      |
| TigerBot    | [tigerBot](https://huggingface.co/datasets/TigerResearch/sft_zh) | TigerBot 模型SFT数据集                     |
|             |                                                              |                                            |

### 3.偏好数据

RL偏好数据集都来自[Hugging Face](https://huggingface.co/)，主要包含以下几个经典的偏好数据集，大约有17w条，详细数据集如下：

| RL偏好数据集                           | 链接                                                         | 描述                                   |
| -------------------------------------- | ------------------------------------------------------------ | -------------------------------------- |
| CValues-Comparison                     | [CValues-Comparison](https://www.modelscope.cn/datasets/iic/CValues-Comparison/summary) | 通义实验室提供的价值观比较数据集       |
| rlhf-reward-single-round-trans_chinese | [rlhf-reward-single-round-trans_chinese](https://huggingface.co/datasets/beyond/rlhf-reward-single-round-trans_chinese) | rlhf-reward-single-round-trans_chinese |
| zhihu_rlhf_3k                          | [zhihu_rlhf_3k](https://huggingface.co/datasets/liyucheng/zhihu_rlhf_3k) | 知乎问答数据集                         |
|                                        |                                                              |                                        |

### 



