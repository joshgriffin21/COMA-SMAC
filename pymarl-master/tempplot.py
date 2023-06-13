import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import json


def readData(file_path):
    with open (file_path, 'r') as _f:
        d = json.load(_f)

        return np.array(d['test_return_mean']), np.array(d['test_return_mean_T'])
    
if __name__ == '__main__':
    directory = 'temp'

    alg_files = ['coma', 'coma_nm', 'coma_qmix', 'coma_vdn']

    plt.figure()

    for alg_file in alg_files:
        alg_file_path = os.path.join(directory, alg_file)
        mean_returns = []
        time_steps_list = np.zeros(0)
        files = os.listdir(alg_file_path)

        for file in files:
            file_path = os.path.join(alg_file_path, file)
            returns, time_steps = readData(file_path)

            mean_returns.append([entry['value'] for entry in returns])
            time_steps_list = time_steps 

        mean_returns = np.mean(mean_returns, axis=0)

        print("run")
        plt.plot(time_steps, mean_returns, label=alg_file)

    plt.xlabel('Time Steps')
    plt.ylabel('Return')
    plt.legend()
    plt.show() 