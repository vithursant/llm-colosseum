import sys

from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()


def main():
    # Environment Settings
    game = Game(
        render=True,
        player_1=Player1(
            nickname="Cerebras",
            model="cerebras:llama3.1-70b",
        ),
        player_2=Player2(
            # nickname="Groq",
            # model="groq:llama-3.1-70b-versatile",
            # nickname="Together AI",
            # model="together:meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
            nickname="Fireworks AI",
            model="fireworks:accounts/fireworks/models/llama-v3p1-70b-instruct",
        ),
    )
    return game.run()

if __name__ == "__main__":
    main()
