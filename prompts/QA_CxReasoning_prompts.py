prompts = [

"""You are the world's best annotator. Your task is to read questions from a dataset, and determine the correct answer from the options provided using only the information given in the question. Output a single character of either A, B or C and nothing else.

 Question: {}

""",

"""Using only the information given in the question, output a single character of either A, B, or C, corresponding to the correct answer. Output a single character only and nothing else.

 Question: {}

""",

"""You are the world's best annotator. Your task is to read questions from a dataset, and determine the correct answer from the options provided using only the information given in the question. Output a single character of either A, B or C and nothing else.
If the answer is not clear from the context provided, output the character C.

 Question: {}

""",

 """Using only the information given in the question, output a single character of either A, B, or C, corresponding to the correct answer. Output a single character only and nothing else.
 If the answer is not clear from the context provided, output the character C.

 Question: {}

""",

"""Based solely on the information provided in the question, output a single character: either A, B, or C, corresponding to the correct answer. Output only one character and nothing else. If the answer is ambiguous, output C.

Question: {}

""",

""" Based solely on the information provided in the question, output a single character: A, B, or C, representing the correct answer. Output only one character. If the correct answer is not clear, output C.

Question: {}

 """,


"""Based solely on the information provided in the question, give a comprehensive answer to the question.
Respond using 1 sentence or less. If the answer is not clear from the context provided, do not give an answer. 

Question: {}

""",

""" Based solely on the information provided in the question, output the character A, B, or C, representing the correct answer. If the correct answer is not clear, output C. Explain Step by step before answering with A, B, or C in the last line.

Question: {}

 """,

 """ You are the top annotator in the world. Your task is to review questions from a dataset and select the correct answer from the given options using only the information provided in the question. Output a single character: A, B, or C. If the correct answer is unclear from the context, output the character C. 

Question: {}

 """,

"""You are the top annotator in the world. Your job is to read questions from a dataset and select the correct answer from the given options based solely on the information in the question. Output only one character: A, B, or C. If the correct answer is not evident from the context, output C.

Question: {}

 """,

  """ You are the top annotator in the world. Your task is to review questions from a dataset and give a comprehensive answer to the questions.
Respond using 1 sentence or less. select the correct answer from the given options using only the information provided in the question. If the correct answer is unclear from the context, do not give an answer. 

Question: {}

 """,

  """ You are the top annotator in the world. Your task is to review questions from a dataset and select the correct answer from the given options using only the information provided in the question. Output a single character: A, B, or C. If the correct answer is unclear from the context, output the character C. Explain Step by step before answering with A, B, or C in the last line.

Question: {}

 """,
# (added "If the answer is not clear from the context provided, output the character C." for prompt variation)
        ]