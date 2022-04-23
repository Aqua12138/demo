import gym, pushing_env
from Agent import DDPGAgent
from utils import learning_curve
import numpy as np

env = gym.make("clutter-v0")

agent = DDPGAgent(env, state_dim=31)
# agent.load_models(3000)
data = agent.learning(max_episode_num = 3000, display = True)
