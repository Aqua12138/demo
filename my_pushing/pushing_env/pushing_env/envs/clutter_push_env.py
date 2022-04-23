import gym
import matplotlib.pyplot as plt
from gym.envs.robotics import robot_env
import numpy as np
from gym.envs.robotics.fetch import push

import os
from gym import utils
from gym.envs.robotics import fetch_env


# Ensure we get the path separator correct on windows
MODEL_XML_PATH = os.path.join('fetch', 'push.xml')


class My_clutter_push_env(fetch_env.FetchEnv, utils.EzPickle):
    def __init__(self, reward_type='sparse'):
        initial_qpos = {
            'robot0:slide0': 0.405,
            'robot0:slide1': 0.48,
            'robot0:slide2': 0.0,
            'object0:joint': [1.25, 0.53, 0.4, 1., 0., 0., 0.],
            # 'object1:joint': [1.25, 0.7, 0.4, 1., 0., 0., 0.],
            # 'object2:joint': [1.25, 0.8, 0.4, 1., 90., 90., 0.]
        }
        fetch_env.FetchEnv.__init__(
            self, MODEL_XML_PATH, has_object=True, block_gripper=True, n_substeps=20,
            gripper_extra_height=0.0, target_in_the_air=False, target_offset=0.0,
            obj_range=0.15, target_range=0.15, distance_threshold=0.05,
            initial_qpos=initial_qpos, reward_type=reward_type)
        utils.EzPickle.__init__(self)


    # 获取相机obs
    def render(self, mode='human', width=500, height=500):
        self._render_callback()
        if mode == 'rgb_array':
            # 修改部分
            camera_id = None
            # camera_name = "track"
            camera_name = "add_cam"
            camera_id = self.model.camera_name2id(camera_name)
            self._get_viewer(mode).render(width, height, camera_id=camera_id)
            # 结束修改
            # self._get_viewer(mode).render(width, height)
            # window size used for old mujoco-py:
            data = self._get_viewer(mode).read_pixels(width, height, depth=False)
            # original image is upside-down, so flip it
            return data[::-1, :, :]
        elif mode == 'human':
            self._get_viewer(mode).render()

    # 设置目标装配件（可更换）
    # 随机设置object位置
    # def _reset_sim(self):
    #     # 设置环境初始状态
    #     self.sim.set_state(self.initial_state)
    #
    #     if self.has_object:
    #         # 将物体设置在初始夹抓位置
    #         object_xpos = self.initial_gripper_xpos[:2]
    #         # 在夹抓周围的obs限制范围内随机取距离，如果距离太近，重新random
    #         while np.linalg.norm(object_xpos - self.initial_gripper_xpos[:2]) < 0.1: # 计算矩阵的二范数
    #             object_xpos = self.initial_gripper_xpos[:2] + self.np_random.uniform(
    #                 -self.obj_range, self.obj_range, size=2
    #             )
    #             obstacle_xpos = self.initial_gripper_xpos[:2] + self.np_random.uniform(
    #                 -self.obj_range, self.obj_range, size=2
    #             )
    #
    #         # 获取目标的位置
    #         object_qpos = self.sim.data.get_joint_qpos("object0:joint").copy()
    #         obstacle_qpos = self.sim.data.get_joint_qpos("object1:joint").copy()
    #         # 如果目标的size不为(7,)直接报错
    #         assert object_qpos.shape == (7,)
    #         assert obstacle_qpos.shape == (7,)
    #
    #         # 设置object的x,y为新的object_xpos
    #         object_qpos[:2] = object_xpos
    #         obstacle_qpos[:2] = obstacle_xpos
    #         # 设置位置
    #         self.sim.data.set_joint_qpos("object0:joint", object_qpos)
    #         # self.sim.data.set_joint_qpos("object1:joint", obsacle_qpos)

        # self.sim.forward()
        # return True



    # 设置障碍物（随机设置、几种摆放好的设置）

    # 设置机器人（可更换）（设计运动底层的修改）

    #


