def get_client(model_str):
    split_result = model_str.split(":")
    if len(split_result) == 1:
        # Assume default provider to be openai
        provider = "openai"
        model_name = split_result[0]
    elif len(split_result) > 2:
        # Some model names have :, so we need to join the rest of the string
        provider = split_result[0]
        model_name = ":".join(split_result[1:])
    else:
        provider = split_result[0]
        model_name = split_result[1]
    if provider == "openai":
        from llama_index.llms.openai import OpenAI

        return OpenAI(model=model_name)
    elif provider == "anthropic":
        from llama_index.llms.anthropic import Anthropic

        return Anthropic(model=model_name)
    elif provider == "cerebras":
        from llama_index.llms.cerebras import Cerebras

        return Cerebras(model=model_name)
    elif provider == "together":
        from llama_index.llms.together import TogetherLLM

        return TogetherLLM(model=model_name)
    elif provider == "fireworks":
        from llama_index.llms.fireworks import Fireworks

        return Fireworks(model=model_name)
    elif provider == "groq":
        from llama_index.llms.groq import Groq
        import os

        return Groq(model=model_name)
    elif provider == "ollama":
        from llama_index.llms.ollama import Ollama

        return Ollama(model=model_name)
    elif provider == "bedrock":
        from llama_index.llms.bedrock import Bedrock
        
        return Bedrock(model=model_name)
