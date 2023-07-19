import template
from llama_cpp import Llama

class LLAMA:
    def __init__(self, model_path, n_gpu_layers=50, n_ctx=512, seed = -1, n_threads = 8, n_parts = -1):
        self.llm = Llama(model_path, n_gpu_layers = n_gpu_layers, n_ctx = n_ctx, seed = seed, n_threads = n_threads, n_parts = n_parts)
        self.llm.reset()
        self.USER_NAME = template.USER_NAME
        self.AI_NAME = template.AI_NAME
        self.template = template.template

    def generate_reply(self, prompt):
        answer_stream = self.llm("{} {}".format(self.template, prompt), stop = [f"{self.USER_NAME}", ".\n"], max_tokens = 128, stream = True, top_k=1)
        answer = ""

        for line in answer_stream:
            answer += line["choices"][0]["text"]

        self.template += answer + "\n"

        try:
            answer = answer.replace("  ", " ").split(f"{self.AI_NAME}:")[1]
            self.strip_template()
        except:
            answer = "I couldn't understand, try using a different prompt. "
        # answer = answer_stream["choices"][0]["text"].replace("  ", " ")

        # self.generate_summary(answer)

        return answer


    def strip_template(self):
        if len(self.template) >= 1024:
            self.template = self.template[200: ] 


def main():
    obj = LLAMA(model_path="./model/ggml-vic13b-uncensored-q5_1.bin")
    print("---------------------------------------------------------")
    obj.generate_reply("Tell me about a C-arm Machine.")

    # print("---------------------------------------------------------")
    # obj.generate_reply("Oh what is the use of Anesthesia Machine? Can we kill someone with it? ")

if __name__ == "__main__":
    main()
