import asyncio

from kittsay import kitt_agent
from kittsay import kitt_animation


async def run(name: str = "Michael", lang: str = "English") -> None:
    kitt_animation_task = asyncio.create_task(kitt_animation.play())
    kitt_text = await kitt_agent.run(name, lang)
    kitt_animation_task.cancel()

    try:
        await kitt_animation_task
    except asyncio.CancelledError:
        pass

    print(kitt_text)
