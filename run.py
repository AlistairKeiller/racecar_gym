import gymnasium
import racecar_gym.envs.gym_api

# For predefined environments:
env = gymnasium.make(
    id='SingleAgentAustria-v0',
    render_mode='human'
)

# For custom scenarios:
env = gymnasium.make(
    id='SingleAgentRaceEnv-v0', 
    scenario='examples/scenarios/austria.yml',
    render_mode='rgb_array_follow', # optional
    render_options=dict(width=320, height=240, agent='A') # optional
)

done = False
reset_options = dict(mode='grid')
obs, info = env.reset(options=reset_options)

while not done:
    print("test")
    action = env.action_space.sample()
    obs, rewards, terminated, truncated, states = env.step(action)
    done = terminated or truncated

env.close()