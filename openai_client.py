import openai
from utils import log_and_send

def api_call(config, transcript):
    try:
        log_and_send("Making API call to OpenAI with transcript.")

        openai.api_key = config.get("OPENAI", "API_KEY")
        prompt = config.get("PROMPT", "DESCRIPTION")
        prompt += f"\nHere's the transcript:\n{transcript}"
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=70,
            temperature=0,
            n=1,
        )
        
        cost = response["usage"]["total_tokens"] * 0.02

        log_and_send(f"Successfully made API call to OpenAI. Cost: {cost}$.")
        
        return response

    except Exception as e:
        log_and_send("Failed to make API call to OpenAI:", e, "error")
        raise e  # re-raise the exception so it can be handled further up the call stack