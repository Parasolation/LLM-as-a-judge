# 采用autoj模板
def extract_pariwise_result(raw_output):
    raw_output = raw_output.strip()
    pos = raw_output.rfind('final decision is ')
    pred_label = -1
    if pos != -1:
        pred_rest = raw_output[pos + len('final decision is '):].strip().lower()
        if pred_rest.startswith('response 1'):
            pred_label = 0
        elif pred_rest.startswith('response 2'):
            pred_label = 1
        elif pred_rest.startswith('tie'):
            pred_label = 2
    return pred_label

def build_own_prompt(parttern='pandalm'):
    prompt_dict = {
        'pandalm': "For the problem, there are two answers, [1] and [2]. You need to choose the better one based on the instruction and the input. Please show your anwser with a pair of brackets directly in the response, like [0], [1] or [2]. If you think [1] is better than [2], return [1]. If you think [2] is better than [1], return [2]. If you think they are similar, return [0].  You don't need to give other addtional response. ",
        'autoj': "For the problem in a specific scenario, there are two answers, [1] and [2]. You need to choose the better one based on the instruction and the input. Please show your anwser with a pair of brackets directly in the response, like [0], [1] or [2]. If you think [1] is better than [2], return [1]. If you think [2] is better than [1], return [2]. If you think they are similar, return [0].  You don't need to give other addtional response. ",
        'llmbar': "For the problem, there are two answers, [1] and [2]. You need to choose the better one based on the instruction and the input. Please show your anwser with a pair of brackets directly in the response, like [1] or [2]. If you think [1] is better than [2], return [1]. If you think [2] is better than [1], return [2].  You don't need to give other addtional response. ",
        'mtbench':"For the problem, there are two 2-turns answers, [1] and [2]. You need to choose the better one based on the instruction and the 2-turns input. Please show your anwser with a pair of brackets directly in the response, like [0], [1] or [2]. If you think [1] is better than [2], return [1]. If you think [2] is better than [1], return [2]. If you think they are similar, return [0].  You don't need to give other addtional response. "
    }
    
    return prompt_dict[parttern]