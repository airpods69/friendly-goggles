from template import *

from transformers import AutoTokenizer
from petals import AutoDistributedModelForCausalLM

class LLM:
    def __init__(
            self, 
            model_name:str = "bigscience/bloom",
            ) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast = False, add_bos_token = False)
        self.llm = AutoDistributedModelForCausalLM.from_pretrained(model_name)
        self.llm = self.llm

        self.template = template

    def strip_template(self):
        # If template becomes a bit too long, we just strip it off cause we won't be depending on this for context
        if len(self.template) >= 1024:
            self.template = self.template[200: ]  

    def chat(self):
        print("Starting the chat")

        fake_token = self.tokenizer("^")["input_ids"][0]  # Workaround to make SentencePiece .decode() keep leading spaces

        with self.llm.inference_session(max_length=512) as sess:
            while True:
                prompt = input('Human: ')
                if prompt == "":
                    break
                prefix = f"Human: {prompt}\nFriendly AI:"
                prefix = self.tokenizer(prefix, return_tensors="pt")["input_ids"]
                print("Friendly AI:", end="", flush=True)

                while True:
                    outputs = self.llm.generate(
                        prefix, max_new_tokens=1, do_sample=True, top_p=0.9, temperature=0.75, session=sess
                    )
                    outputs = self.tokenizer.decode([fake_token, outputs[0, -1].item()])[1:]
                    print(outputs, end="", flush=True)
                    if "\n" in outputs:
                        break
                    prefix = None  # Prefix is passed only for the 1st token of the bot's response



    # def generate(self, prompt: str, max_new_tokens: int = 128):
        # answer_tokens = self.tokenizer(f"{self.template} {prompt}", return_tensors = "pt")["input_ids"]
        # answer = self.llm.generate(answer_tokens, max_new_tokens = max_new_tokens)
        # answer_string = self.tokenizer.decode(answer[0])
        # 
        #
        # self.template += f"{answer_string} \n"
        # 
        # # A chicky little hack to check be sure that the program doesn't crash if an answer_string couldn't be generated.
        # try:
        #     answer_string = answer_string.replace("  ", " ").split(f"{AI_NAME}:")[1]
        # except:
        #     answer_string = "I couldn't understand what you meant, try asking something else?"
        #
        # return answer_string
        #



def main():
    obj = LLM(model_name = "bigscience/bloom")
    obj.chat()

if __name__ == "__main__":
    main()

