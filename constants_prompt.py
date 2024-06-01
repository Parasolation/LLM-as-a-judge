PROMPT_INPUT_SYSTEM: str = '[INST] <<SYS>>\n{system_message}\n<</SYS>>\n\n{input} [/INST]'

PROMPT_INPUT_WO_SYSTEM: str = "[INST] {input} [/INST]"

PROMPT_INPUT_FOR_SCENARIO_CLS: str = "Identify the scenario for the user's query, output 'default' if you are uncertain.\nQuery:\n{input}\nScenario:\n"

single = """Write critiques for a submitted response on a given user's query, and grade the response:
  
[BEGIN DATA]
***
[Query]: {prompt}
***
[Response]: {response}
***
[END DATA]

Write critiques for this response. After that, you should give a final rating for the response on a scale of 1 to 10 by strictly following this format: "[[rating]]", for example: "Rating: [[5]]"."""

pairwise_tie = """You are assessing two submitted responses on a given user's query and judging which response is better or they are tied.

Here are the instructions to assess and compare the two responses:
1. Pinpoint the key factors to distinguish these two responses.
2. Conclude your comparison by providing a final decision on which response is better, or they are tied. Begin your final decision statement with "So, the final decision is Response 1 / Response 2 / Tie". Ensure that your decision aligns coherently with the comprehensive evaluation and comparison you've provided.

Here is the data:

[BEGIN DATA]
***
[Query]: {prompt}
***
[Response 1]: {response}
***
[Response 2]: {response_another}
***
[END DATA]

Here are the instructions to assess and compare the two responses:

1. Pinpoint the key factors to distinguish these two responses.
2. Conclude your comparison by providing a final decision on which response is better, or they are tied. Begin your final decision statement with "So, the final decision is Response 1 / Response 2 / Tie". Ensure that your decision aligns coherently with the comprehensive evaluation and comparison you've provided."""


multiturn_pairwise_tie_type1 = """
You are assessing two submitted responses on a given 2-turn user's query and judging which response is better or they are tied. Please take both turns of response into account.

Here are the instructions to assess and compare the two responses:
1. Pinpoint the key factors to distinguish these two responses.
2. Conclude your comparison by providing a final decision on which response is better, or they are tied. Begin your final decision statement with "So, the final decision is Response 1 / Response 2 / Tie". Ensure that your decision aligns coherently with the comprehensive evaluation and comparison you've provided.

Here are the instructions to assess and compare the two responses:

[BEGIN DATA]
***
[Turn 1]: 
[Query]: {prompt1}
***
[Response 1]: {response1}
***
[Response 2]: {response_another1}
***
[Turn 2]: 
[Query]: {prompt2}
***
[Response 1]: {response2}
***
[Response 2]: {response_another2}
***


[END DATA]
"""

multiturn_pairwise_tie_type2 = """
You are assessing two submitted responses on a given 2-turn user's query and judging which response is better or they are tied. Please take both turns of response into account.

Here are the instructions to assess and compare the two responses:
1. Pinpoint the key factors to distinguish these two responses.
2. Conclude your comparison by providing a final decision on which response is better, or they are tied. Begin your final decision statement with "So, the final decision is Response 1 / Response 2 / Tie". Ensure that your decision aligns coherently with the comprehensive evaluation and comparison you've provided.

Here are the instructions to assess and compare the two responses:

[BEGIN DATA]
***
[Query turn 1]: {prompt1}
[Query turn 2]: {prompt2}
***
[response 1]: 
[turn 1]: {response1}
[turn 2]: {response2}
***
[Response 2]: 
[turn 1]: {response_another1}
[turn 2]: {response_another2}
***

[END DATA]
"""

protocol_mapping = {
    "pairwise_tie": pairwise_tie,
    "single": single,
    "multiturn_pairwise_tie_type1": multiturn_pairwise_tie_type1,
    "multiturn_pairwise_tie_type2": multiturn_pairwise_tie_type2,
}


def llama2_wrapper(usr_msg, sys_msg=None):
    if sys_msg is None:
        return PROMPT_INPUT_WO_SYSTEM.format(input=usr_msg)
    else:
        return PROMPT_INPUT_SYSTEM.format(input=usr_msg, system_message=sys_msg)


def build_autoj_input(prompt, resp1, resp2=None, prompt2=None, resp1_2=None, resp2_2=None, protocol="single"):
    if protocol in ['single', 'pairwise_tie']:
        user_msg = protocol_mapping[protocol].format(prompt=prompt, response=resp1, response_another=resp2)
    else:
        user_msg = protocol_mapping[protocol].format(prompt1=prompt, response1=resp1, response_another1=resp2, prompt2=prompt2, response2=resp1_2, response_another2=resp2_2)
    return llama2_wrapper(user_msg, )


if __name__ == '__main__':
    t = build_autoj_input("instruction", "resp1", "resp2", "pairwise_tie")
    print(t)
