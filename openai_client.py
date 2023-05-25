import openai, os

def api_call(system_prompt, user_prompt, config):
    openai.api_key = config.get("OPENAI", "API_KEY")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )
    return response["choices"][0]["message"]["content"]


def summarize_urban_rescue(transcript, config):
    completion = api_call(
        """I am an AI developed by OpenAI, and I'm trained to summarize various types of content. For this task, I'll summarize videos from the YouTube channel 'Urban Rescue Ranch', emulating the unique, casual and humorous style of the host, 'Uncle Ben'. The summaries should be direct, avoid introductory and concluding phrases, and should be formatted as bullet points. For instance:

        - Would you look at that, kangaroos got a new area. Ready to raise some white tails here!
        - The compost system is a charm! Dang, that's a lot of grass!
        - Found a baby pigeon, new family member, say hello to Geronimo!
        - Cleaning up after the Cappies today, they sure know how to throw a party.
        - Moved the Cappies to a new area, they've got some serious impact on the grass, huh!
        """, 
        f"""Given the following transcript from an 'Urban Rescue Ranch' video, can you provide a summary that captures the main points in Uncle Ben's distinctive style? Here's an example of his style:\n
        - Would you look at that, kangaroos got a new area. Ready to raise some white tails here!
        - The compost system is a charm! Dang, that's a lot of grass!
        - Found a baby pigeon, new family member, say hello to Geronimo!
        - Cleaning up after the Cappies today, they sure know how to throw a party.
        - Moved the Cappies to a new area, they've got some serious impact on the grass, huh!\n{transcript}""",
        config)
    
    return completion