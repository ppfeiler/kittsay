from pydantic_ai import Agent


def generate_system_prompt(name: str = "Michael", lang: str = "English") -> str:
    return f"You are K.I.T.T. (Knight Industries Two Thousand) from the TV series “Knight Rider.” Immediately respond in {lang}, in K.I.T.T.’s polite, slightly ironic yet intelligent tone. Do not explain yourself. Directly output a random quote or remark that sounds like something K.I.T.T. would say in the series, addressing {name}"


async def run(name: str = "Michael", lang: str = "English") -> str:
    agent = Agent(
        model="openai:gpt-5-nano",
        system_prompt=generate_system_prompt(name, lang),
        output_type=str,
    )

    result = await agent.run()
    return result.output
