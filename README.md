# Youtube summarize

Youtube Summarize is a project that monitors specific YouTube channels for new video uploads and provides a summarized version of the video content using the OpenAI API. The summarized content is then, ideally, posted to Discord or potentially other bot-supported platforms. Due to the character limit for tweets, the use of a Twitter bot is currently suboptimal, but you can easily add other bots by configuring the .ini file and `bot.py`.

This project relies on a configuration file (.ini format), where you can provide necessary keys and values for the project to run. Here's an explanation of the keys:

## .ini Configuration
* [GOOGLE]

    * API_KEY: Your Google API key which is required to access YouTube data.
* [OPENAI]

    * API_KEY: Your OpenAI API key used to use the OpenAI GPT-4 model for summarizing videos.
* [PROMPT]

    * DESCRIPTION: The system prompt used to set up the style of conversation with the chat completion model. The description should guide the AI to create summaries in a specific manner. For example:
        ```
        You are a helpful assistant that summarizes YouTube videos from the channel TheUrbanRescueRanch. Summarize the video in a humorous style that matches the original content, starting with 'Alright everybody, Uncle Ben here!', including three extremely brief bullet points, and ending directly with only the phrase 'Almost forgot to tell you!'.
        ```
* [TWITTER]

    * ENABLE: Determines if the Twitter bot is used. Set to FALSE by default due to the 140 characters limit for tweets making it difficult to create satisfactory summaries.
    * API_KEY: Your Twitter API key (only necessary if ENABLE is set to TRUE).
    * API_SECRET_KEY: Your Twitter API secret key (only necessary if ENABLE is set to TRUE).
    * ACCESS_TOKEN: Your Twitter access token (only necessary if ENABLE is set to TRUE).
    * ACCESS_TOKEN_SECRET: Your Twitter access token secret (only necessary if ENABLE is set to TRUE).
* [YOUTUBE]

    * CHANNEL_ID: The ID of the YouTube channel you wish to monitor.
    * CHANNEL_NAME: The name of the YouTube channel.
* [DISCORD_LOG]

    * WEBHOOK: Your Discord Webhook URL. If you don't want to get logs using a discord webhook, leave this as is.
    * Several keys to set the logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL). By default all are set to FALSE.

## Running the project

This project can be set up to run at regular intervals (for example, using cron jobs or similar scheduling tools) to automatically check for new videos and provide summaries.