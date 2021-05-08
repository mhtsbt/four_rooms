import gym
import argparse
import cv2
import gym_miniworld
from common.make_env import make_env


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-name", default="MiniWorld-FourRooms-v0")
    parser.add_argument("--steps", default=int(10e3))
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()
    env = make_env(env_name=args.env_name)

    state = env.reset()

    for step_id in range(args.steps):
        action = env.action_space.sample()
        state, reward, done, info = env.step(action=action)

        print(f"step: {step_id} reward: {reward} done: {done}")

        env.render(view='top')

        if done:
            env.reset()

    env.close()
