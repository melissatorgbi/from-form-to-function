from experimentSetup import runTests_NLI

if __name__ == '__main__' :
    openai_completion_style = "ChatCompletion"

    api_path = "openai_api_keys.env"

    test_data = "data/constructional_NLI/CoGS-NLI_3_examples_test.tsv" #NLI example

    train_data = "data/constructional_NLI/CoGS-NLI_3_examples_train.csv" #Not neccessary if running  zero shot NLI, can leave as is
    train_data_version = "CoGS-NLI" #Not neccessary if running zero shot NLI, can leave as is

    test_data_version = "target" #Not necessary if running a NLI experiment, can leave as is

    temperature = 0 #Change the temperature from 0 to 1 for o1 model

    output_directory = "Output"
    model = "gpt-4o" #Other options inlcude, "o1-preview-2024-09-12" and "gpt-3.5-turbo"
    prompt_number = 2 #Prompts can be found in prompts/CxNLI_prompts.py
    experiment_name = "CoGS-NLI"

    tester = runTests_NLI( test_data, train_data, output_directory, openai_completion_style, api_path, train_data_version)
    tester.get_all(model, prompt_number, experiment_name, temperature)