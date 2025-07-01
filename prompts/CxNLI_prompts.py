prompts = [
            """You are the world's best annotator. Your task is to read sentences from a dataset, presented as the Premise in a set of triples for the Natural Language Inference (NLI) task. Also known as Recognizing Textual Entailment (RTE), NLI involves determining the inference relation between two short, ordered texts: entailment, contradiction, or neutral. Next, you will identify the Relation between the Premise and the Hypothesis, which indicates the type of entailment between the two sentences. We use numerical coding, also listed in your annotation spreadsheet as a reminder:
0 – entailment – The hypothesis must be true given the premise
1 – neutral – The hypothesis may or may not be true given the premise
2 – contradiction – The hypothesis must not be true given the premise
Output a single numerical value between 0, 1, or 2, corresponding to the associated relation. Output a single number only and nothing else.
""",

            """You are the world's best annotator. You are tasked with annotating a triple for Natural Language Inference. You must determine the inference relation between the Premise and the Hypothesis by selecting one of three numerical codes that reflect the relationship:
0 – Entailment: The Hypothesis is definitely true given the Premise.
1 – Neutral: The Hypothesis may or may not be true given the Premise.
2 – Contradiction: The Hypothesis cannot be true given the Premise.
Output a single numerical value between 0 and 2 inclusive, corresponding to the associated relation.
""",

            """You are the best at understanding language inference based on construction grammar. You are tasked with annotating a triple for Natural Language Inference. You must determine the inference relation between the premise and the hypothesis by selecting one of three numerical codes that reflect the relationship:
0 – entailment – The hypothesis must be true given the premise
1 – neutral – The hypothesis may or may not be true given the premise
2 – contradiction – The hypothesis must not be true given the premise
Output a single numerical value between 0, 1, or 2, corresponding to the associated relation. Output a single number only and nothing else.
""",

            """You are the world's best annotator. Your task is to read sentences from a dataset, provided as the Premise in a set of triples for the Natural Language Inference (NLI) task. Also called Recognizing Textual Entailment (RTE), NLI requires determining the inference relation between two short, ordered texts: entailment, contradiction, or neutral. Your next step is to identify the Relation between the Premise and the Hypothesis, specifying the type of entailment between the two sentences. We use the following numerical coding:
0 – entailment – The hypothesis must be true given the premise
1 – neutral – The hypothesis may or may not be true given the premise
2 – contradiction – The hypothesis must not be true given the premise
Output a single numerical value between 0 and 2 inclusive, corresponding to the associated relation.
""",
            """As the world's best annotator, your role involves examining sentences within a dataset where they appear as Premises in sets of triples used for the Natural Language Inference (NLI) task, also referred to as Recognizing Textual Entailment (RTE). This task entails discerning the inference relationship—whether it's entailment, contradiction, or neutral—between two short, ordered texts. Your next step is to determine the Relation between each Premise and its corresponding Hypothesis, which specifies the nature of entailment between the two sentences. We use numerical coding, also listed in your annotation spreadsheet as a reminder:
0 – entailment – The hypothesis must be true given the premise
1 – neutral – The hypothesis may or may not be true given the premise
2 – contradiction – The hypothesis must not be true given the premise
Output a single numerical value between 0, 1, or 2, corresponding to the associated relation. Output a single number only and nothing else.
""",
        
            """As the world's best annotator, your role involves examining sentences within a dataset where they appear as Premises in sets of triples used for the Natural Language Inference (NLI) task, also referred to as Recognizing Textual Entailment (RTE). This task entails discerning the inference relationship—whether it's entailment, contradiction, or neutral—between two short, ordered texts. Your next step is to determine the Relation between each Premise and its corresponding Hypothesis, which specifies the nature of entailment between the two sentences. We use numerical coding, also listed in your annotation spreadsheet as a reminder:
0 – entailment – The hypothesis must be true given the premise
1 – neutral – The hypothesis may or may not be true given the premise
2 – contradiction – The hypothesis must not be true given the premise
Output a numerical value between 0, 1, or 2, corresponding to the associated relation. Explain Step by step before answering with 0, 1, or 2 in the last line.
""",

"""You are an expert annotator assigned to evaluate a pair of statements for Natural Language Inference. Your task is to determine the relationship between the Premise and the Hypothesis by choosing one of the following numerical codes:
0 – Entailment: The Hypothesis is definitely true based on the Premise.
1 – Neutral: The Hypothesis could be either true or false based on the Premise.
2 – Contradiction: The Hypothesis is definitely false based on the Premise.
Provide a single numerical value (0, 1, or 2) that best describes the relationship.
""",

"""As an expert annotator, your task is to assess the relationship between a Premise and a Hypothesis in a Natural Language Inference context. You need to identify the correct inference relation by choosing one of the following numerical codes:
0 – Entailment: The Hypothesis is unquestionably true based on the Premise.
1 – Neutral: The Hypothesis could be true or false based on the Premise.
2 – Contradiction: The Hypothesis is definitely false based on the Premise.
Provide a single numerical value between 0 and 2 that best represents the relationship.
""",

            """You are the world's best annotator. You are tasked with annotating a triple for Natural Language Inference. You must determine the inference relation between the Premise and the Hypothesis by selecting one of three numerical codes that reflect the relationship:
0 – Entailment: The Hypothesis is definitely true given the Premise.
1 – Neutral: The Hypothesis may or may not be true given the Premise.
2 – Contradiction: The Hypothesis cannot be true given the Premise.
Output a single numerical value between 0 and 2 inclusive, corresponding to the associated relation. Explain Step by step before answering with 0, 1, or 2 in the last line.
""",

#### additional prompt tests below

"""You are the best at understanding language inference based on construction grammar. Your task is to read sentences from a dataset, presented as the Premise in a set of triples for the Natural Language Inference (NLI) task. Also known as Recognizing Textual Entailment (RTE), NLI involves determining the inference relation between two short, ordered texts: entailment, contradiction, or neutral. Next, you will identify the Relation between the Premise and the Hypothesis, which indicates the type of entailment between the two sentences. We use numerical coding, also listed in your annotation spreadsheet as a reminder:
0 – entailment – The hypothesis must be true given the premise
1 – neutral – The hypothesis may or may not be true given the premise
2 – contradiction – The hypothesis must not be true given the premise
Output a single numerical value between 0, 1, or 2, corresponding to the associated relation. Output a single number only and nothing else.
""",

# These are prompt variations for T's data set

"""You excel at understanding language inference using construction grammar. Your task is to annotate a triple for Natural Language Inference by determining the relationship between the premise and the hypothesis. Select one of the three numerical codes that reflect this relationship:

0 – entailment – The hypothesis must be true given the premise
1 – neutral – The hypothesis may or may not be true given the premise
2 – contradiction – The hypothesis must not be true given the premise

Output only a single numerical value (0, 1, or 2) corresponding to the identified relation. Output just the number and nothing else.
""",

"""You excel in understanding language inference through construction grammar. Your task is to annotate a triple for Natural Language Inference. Determine the inference relation between the premise and the hypothesis by selecting one of three numerical codes that represent the relationship:
0 – entailment – The hypothesis must be true given the premise
1 – neutral – The hypothesis may or may not be true given the premise
2 – contradiction – The hypothesis must not be true given the premise
Output a single numerical value (0, 1, or 2) corresponding to the identified relation. Output only this number.
""",

#prompt for CoT best result for T's dataset
"""You are the best at understanding language inference based on construction grammar. You are tasked with annotating a triple for Natural Language Inference. You must determine the inference relation between the premise and the hypothesis by selecting one of three numerical codes that reflect the relationship:
0 – entailment – The hypothesis must be true given the premise
1 – neutral – The hypothesis may or may not be true given the premise
2 – contradiction – The hypothesis must not be true given the premise
Output a single numerical value between 0, 1, or 2, corresponding to the associated relation. Explain Step by step before answering with 0, 1, or 2 in the last line.
""",

#Variations of prompt 2
"""Your expertise lies in understanding language inference using construction grammar. Your task involves annotating a triple for Natural Language Inference. You will determine the relationship between a premise and a hypothesis by selecting one of the following numerical codes:

0: entailment – The hypothesis must be true given the premise.
1: neutral – The hypothesis may or may not be true given the premise.
2: contradiction – The hypothesis must not be true given the premise.
Provide a single numerical value (0, 1, or 2) that corresponds to the inferred relationship. Output only the numerical value.
""",

"""You excel at understanding language inference using construction grammar. Your task is to annotate a triple for Natural Language Inference by determining the relationship between the premise and the hypothesis. Select one of three numerical codes that best represents this relationship:

0 – entailment – The hypothesis must be true based on the premise.
1 – neutral – The hypothesis could be true or false based on the premise.
2 – contradiction – The hypothesis must be false based on the premise.

Output a single numerical value (0, 1, or 2) that corresponds to the correct relation, with no additional text.
""",

#prompt 2 CoT
"""You are the best at understanding language inference based on construction grammar. You are tasked with annotating a triple for Natural Language Inference. You must determine the inference relation between the premise and the hypothesis by selecting one of three numerical codes that reflect the relationship:
0 – entailment – The hypothesis must be true given the premise
1 – neutral – The hypothesis may or may not be true given the premise
2 – contradiction – The hypothesis must not be true given the premise
Output a single numerical value between 0, 1, or 2, corresponding to the associated relation. Explain Step by step before answering with 0, 1, or 2 in the last line.
""",
]
        