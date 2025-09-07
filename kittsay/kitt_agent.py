from pydantic_ai import Agent


def generate_system_prompt(name: str = "", lang: str = "English") -> str:
    if name:
        return f"""
        You are KITT from the series Knight Rider.
        In your response, mention the following name: {name}.
        Reply with a typical sentence KITT would say during a conversation, in the {lang} language.
        """
    else:
        return f"""
        You are KITT from the series Knight Rider.
        In your response, do not address anyone directly and do not mention any names.
        Reply with a typical sentence KITT would say, in the {lang} language.
        """


def run(name: str = "", lang: str = "English") -> str:
    agent = Agent(
        model="openai:gpt-5-nano",
        system_prompt=generate_system_prompt(name, lang),
        output_type=str,
    )

    result = agent.run_sync()
    return result.output
