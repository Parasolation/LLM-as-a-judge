

#### 模型部分：

通过OpenCompass2.0大语言模型评测榜单的客观综合和主观综合部分初选出了以下几个开源模型，囿于硬件性能，我只选择了模型大小14B以下的模型。

加上给定Benchmark所提供的两个用于评估大模型表现的两个大模型Autoj-13B以及PandaLM-7B-v1

- [Qwen1.5-7B-Chat](https://huggingface.co/Qwen/Qwen1.5-7B-Chat)
- [Qwen1.5-14B-Chat](https://huggingface.co/Qwen/Qwen1.5-14B-Chat)
- [Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct)
- [Nanbeige2-8B-Chat](https://huggingface.co/Nanbeige/Nanbeige2-8B-Chat)
- [ChatGLM3-6B](https://huggingface.co/THUDM/chatglm3-6b)
- [InternLM2-chat-7B](https://huggingface.co/internlm/internlm2-chat-7b)
- [Deepseek-llm-7B-chat](https://huggingface.co/deepseek-ai/deepseek-llm-7b-chat)
- [Autoj-13B](https://huggingface.co/GAIR/autoj-13b)
- [PandaLM-7B](https://huggingface.co/WeOpenML/PandaLM-7B-v1)

#### 代码部分：









#### 运行结果：

| Model                | Auto-J | PandaLM | LLMBar_natural | *LLMBar_neighbor* | *LLMBar_gptinst* | *LLMBar_gptout* | *LLMBar_manual* | *MTBench* | 备注————————————                                 |
| :------------------- | :----- | :------ | :------------- | :---------------- | :--------------- | :-------------- | :-------------- | :-------- | :----------------------------------------------- |
| Qwen1.5-7B-Chat      | 48.99  | 62.36   | 61.00          | 22.39             | 29.35            | 48.94           | 30.43           | 54.61     |                                                  |
| Qwen1.5-14B-Chat     | 48.64  | 70.57   | 72.00          | 23.13             | 25.00            | 51.06           | 32.61           | 43.99     | 本身结果不错，但格式错误太多了，需要微调学习格式 |
| Llama-3-8B-Instruct  | 55.24  | 70.17   | 71.00          | 16.42             | 22.83            | 57.45           | 28.26           | 46.65     |                                                  |
| ChatGLM3-6B          | 42.53  | 51.65   | 52.00          | 23.88             | 33.70            | 48.94           | 32.61           | 36.15     | 格式错误太多                                     |
| InternLM2-chat-7B    | 42.10  | 52.55   | 54.00          | 15.67             | 34.78            | 36.17           | 23.91           | 52.55     |                                                  |
| Deepseek-llm-7B-chat | 36.64  | 50.55   | 43.00          | 29.85             | 29.35            | 40.43           | 26.09           | 30.04     | 格式错误太多                                     |
| Auto-J-13B           | 59.99  | 69.67   | 66.00          | 20.15             | 19.57            | 42.55           | 23.91           | 57.35     |                                                  |
| PandaLM-7B           |        |         |                |                   |                  |                 |                 |           |                                                  |
| 原论文结果：         |        |         |                |                   |                  |                 |                 |           |                                                  |
| GPT 4-0613           | 56.3   | 78.68   | 93.5           | 64.2              | 76.6             | 76.6            | 75.0            | 66.9      |                                                  |
| Auto-J-13B           | 54.6   | 71.47   | 70.0           | 20.9              | 21.7             | 46.8            | 23.9            | 51.7      |                                                  |
| PandaLM-7B           | 40.0   | 67.57   | 59.0           | 16.5              | 21.7             | 42.6            | 26.1            | 55.2      |                                                  |
|                      |        |         |                |                   |                  |                 |                 |           |                                                  |



初步运行结果如表：

可以发现Qwen1.5-7B-chat和Qwen1.5-14B-chat以及Llama-3-8B-Instruct效果还不错，但是有很多回答并未按prompt所提供的格式正常生成。所以后续在该3个模型上进行微调。

训练集选择Auto-J数据库里的train set，共有3000+条数据，按照过去的经验，数据量比较够了。

