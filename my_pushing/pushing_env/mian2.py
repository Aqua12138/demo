



import time
import gym, pushing_env
# Number of steps you run the agent for
num_steps = 1500
env = gym.make("clutter-v0")
obs = env.reset()

for step in range(num_steps):
    # take random action, but you can also do something more intelligent
    # action = my_intelligent_agent_fn(obs)
    action = env.action_space.sample()

    # apply the action
    obs, reward, done, info = env.step(action)

    # Render the env
    env.render()

    # Wait a bit before the next frame unless you want to see a crazy fast video
    time.sleep(0.001)

    # If the epsiode is up, then start another one
    if done:
        b = env.reset()
        c = b['observation']
# Close the env
env.close()