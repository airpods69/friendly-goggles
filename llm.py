from template import *

from transformers import AutoTokenizer
from petals import AutoDistributedModelForCausalLM

class LLM:
    def __init__(
            self, 
            model_name = "bigscience/bloom",
            ) -> None:
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast = False, add_bos_token = False)
        self.llm = AutoDistributedModelForCausalLM.from_pretrained(model_name)
        self.llm = self.llm.cuda()

        self.template = template

    def strip_template(self):
        # If template becomes a bit too long, we just strip it off cause we won't be depending on this for context
        if len(self.template) >= 1024:
            self.template = self.template[200: ]  



    def generate_reply(self, prompt, max_tokens = 128):
        answer_tokens = self.tokenizer(f"{self.template} {prompt}", return_tensors = "pt")["input_ids"].cuda()
        answer = self.llm.generate(answer_tokens, max_new_tokens = 5)
        answer_string = self.tokenizer.decode(answer[0])
        

        self.template += f"{answer_string} \n"
        
        # A chicky little hack to check be sure that the program doesn't crash if an answer_string couldn't be generated.
        try:
            answer_string = answer_string.replace("  ", " ").split(f"{AI_NAME}:")[1]
        except:
            answer_string = "I couldn't understand what you meant, try asking something else?"

        return answer_string



def main():
    obj = LLM(model_name = "enoch/llama-65b-hf")
    print(obj.generate_reply("How are you doing, my dearest AI?"))

if __name__ == "__main__":
    main()

