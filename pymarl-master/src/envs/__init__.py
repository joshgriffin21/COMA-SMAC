from functools import partial
from .multiagentenv import MultiAgentEnv
from .stag_hunt import StagHunt
from .matrix_game.matrix_game_simple import Matrixgame
import sys
import os

def env_fn(env, **kwargs) -> MultiAgentEnv:
    return env(**kwargs)

REGISTRY = {}
REGISTRY["matrix_game"] = partial(env_fn, env=Matrixgame)
REGISTRY["stag_hunt"] = partial(env_fn, env=StagHunt)