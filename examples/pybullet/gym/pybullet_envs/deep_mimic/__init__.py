from .humanoid_deepmimic_gym_env import HumanoidDeepMimicGymEnv

import gym
from gym.envs.registration import registry, make, spec
def register(id,*args,**kvargs):
    if id in registry.env_specs:
        return
    else:
        return gym.envs.registration.register(id,*args,**kvargs)

# ------------bullet-------------

register(
    id='HumanoidDeepMimicBulletEnv-v2',
    entry_point='deep_mimic:HumanoidDeepMimicGymEnv',
    max_episode_steps=1000,
    reward_threshold=20000.0,
)