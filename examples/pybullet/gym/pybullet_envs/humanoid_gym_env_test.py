import gym
import deep_mimic
from deep_mimic.humanoid import jointsInfo


def get_kin_action(humanoid):
    pose = humanoid.InitializePoseFromMotionData()
    action = []
    for joint_name, joint_info in jointsInfo.items():
        if joint_info['spherical']:
            axis, angle = humanoid._pybullet_client.getAxisAngleFromQuaternion(pose.GetJointRot(joint_name))
            action.extend([angle] + list(axis))
        else:
            action.append(pose.GetJointRot(joint_name)[0])
    return action


def main():
    env = gym.make('HumanoidDeepMimicBulletEnv-v2')

    env.render(mode='human')
    d = True

    for _ in range(10000):
        if d:
            s = env.reset()
        s, r, d, _ = env.step(get_kin_action(env.unwrapped._humanoid))
        print(r)


if __name__ == '__main__':
    main()