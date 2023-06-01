import openai

def api_call(config, _):
    openai.api_key = config.get("OPENAI", "API_KEY")
    prompt = config.get("PROMPT", "DESCRIPTION")
    prompt += f"\nHere's the transcript:\n{_}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=70,
        temperature=0,
        n=1,
    )
    return response


"""def summarize_urban_rescue(transcript, config):
    completion = api_call(
        I am an AI developed by OpenAI, and I'm trained to summarize various types of content. The response can't be more than 280 characters long. For this task, I'll summarize videos from the YouTube channel 'Urban Rescue Ranch', emulating the unique, casual and humorous style of the host, 'Uncle Ben'. The summaries should be direct, avoid introductory and concluding phrases, and should be formatted as bullet points. For instance:

        - Would you look at that, kangaroos got a new area. Ready to raise some white tails here!
        - The compost system is a charm! Dang, that's a lot of grass!
        - Found a baby pigeon, new family member, say hello to Geronimo!
        - Cleaning up after the Cappies today, they sure know how to throw a party.
        - Moved the Cappies to a new area, they've got some serious impact on the grass, huh!
        , 
        ,
        config)
    
    return completion"""