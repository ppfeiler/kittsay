from kittsay import kitt_agent


def run(name: str = "", lang: str = "English") -> None:
    print(kitt_agent.run(name, lang))
