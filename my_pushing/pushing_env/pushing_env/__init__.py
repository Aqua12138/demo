from gym.envs.registration import register

for reward_type in ["sparse", "dense"]:
    suffix = "Dense" if reward_type == "dense" else ""
    kwargs = {
        "reward_type": reward_type,
    }
register(
    id='clutter-v0',
    entry_point='pushing_env.envs:My_clutter_push_env',
    kwargs=kwargs,
    max_episode_steps=50,
)
