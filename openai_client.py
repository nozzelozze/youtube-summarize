import openai
from utils import log_and_send

def api_call(config, transcript):
    try:
        log_and_send("Making API call to OpenAI with transcript.")

        openai.api_key = config.get("OPENAI", "API_KEY")
        prompt = config.get("PROMPT", "DESCRIPTION")
    
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": transcript}
            ]
        )
        
        cost = (response["usage"]["total_tokens"]/1000) * 0.002
        log_and_send(f"Successfully made API call to OpenAI. Cost: {cost}$.")
        log_and_send(f"OpenAI API reponse: {response}")
        
        return response

    except Exception as e:
        log_and_send("Failed to make API call to OpenAI:", e, "error")
        raise e