from kittsay import kitt_agent


async def run(name: str = "Michael", lang: str = "English") -> None:
    kitt_text = await kitt_agent.run(name, lang)
    print(kitt_text)
