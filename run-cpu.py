# Model downloaded locally from: https://huggingface.co/google/gemma-7b-it

# Import the AutoTokenizer class from the transformers library and give it an alias 'at'
# Import the AutoModelForCausalLM class from the transformers library and give it an alias 'am'
from transformers import AutoTokenizer as at, AutoModelForCausalLM as am

# Use the AutoTokenizer class (aliased as 'at') to load a pre-trained tokenizer
# The model name "google/gemma-2b-it" specifies which tokenizer to load from the Hugging Face Model Hub
tokenizer = at.from_pretrained("google/gemma-2b-it")