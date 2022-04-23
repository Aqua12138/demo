import gym, pushing_env
import matplotlib.pyplot as plt
# env = gym.make("FetchPush-v1")
env = gym.make("clutter-v0")

env_screen = env.render(mode = 'rgb_array')
env.action_space
plt.imshow(env_screen)
plt.show()
