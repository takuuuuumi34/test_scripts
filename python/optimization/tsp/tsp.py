import numpy as np
import matplotlib.pyplot as plt
import random
import sys


def calculate_total_distance(order, distance_matrix):
    """Calculate total distance traveled for given visit order"""
    idx_from = np.array(order)
    idx_to = np.array(order[1:] + [order[0]])
    distance_arr = distance_matrix[idx_from, idx_to]

    return np.sum(distance_arr)


def visualize_visit_order(order, city_xy):
    """Visualize traveling path for given visit order"""
    route = np.array(order + [order[0]])  # add point of departure
    x_arr = city_xy[:, 0][route]
    y_arr = city_xy[:, 1][route]

    plt.figure(figsize=(4, 4))
    plt.plot(x_arr, y_arr, 'o-')
    plt.show()


class TSP(object):
    def __init__(self, city_xy):
        self.city_xy = city_xy

        x = city_xy[:, 0]
        y = city_xy[:, 1]
        self.distance_matrix = np.sqrt((x[:, np.newaxis] - x[np.newaxis, :]) ** 2 +
                                  (y[:, np.newaxis] - y[np.newaxis, :]) ** 2)


    def random_play(self, n_play):
        # random
        total_dist = 0
        for _p in range(n_play):
            test_order = list(np.random.permutation(N))
            dist = calculate_total_distance(test_order, self.distance_matrix)
            total_dist += dist
            # print(dist)
        avg_dist = total_dist / n_play
        print("avg: {}".format(avg_dist))

    def play(self, n_play):
        self.q = np.zeros((self.city_xy.shape[0],self.city_xy.shape[0]))
        self.q_count = np.zeros((self.city_xy.shape[0],self.city_xy.shape[0]))
        average_reward = np.zeros(n_play)

        for _p in range(n_play):
            current_city = 0
            total_dist = 0
            state = np.zeros(self.city_xy.shape[0])
            state[current_city] = 1

            # episode
            while sum(state) != self.city_xy.shape[0]:
                # choice next city
                i = random.randrange(self.city_xy.shape[0])

                if state[i] == 0:
                    state[i] = 1
                    total_dist += self.distance_matrix[current_city, i]
                    current_city = i
            print("dist: {}".format(total_dist))
            # update q table



if __name__ == "__main__":
    # randomize city position
    N = 20
    MAP_SIZE = 100

    np.random.seed(10)
    city_xy = np.random.rand(N, 2) * MAP_SIZE

    tsp = TSP(city_xy)
    tsp.play(1)


    # visualize city position
    # plt.figure(figsize=(4, 4))
    # plt.plot(city_xy[:, 0], city_xy[:, 1], 'o')
    # plt.show()

    # 見やすくするために10都市分だけ出力。
    # distance_matrix[i, j]が都市iと都市jの距離。
    # print(np.round(distance_matrix[:10, :10]))

    # # 試しに距離を計算してみる
    # test_order = list(np.random.permutation(N))
    # print('訪問順序 = {}'.format(test_order))
    #
    # total = calculate_total_distance(test_order, distance_matrix)
    # print('総移動距離 = {}'.format(total))
    #
    # # 可視化を試してみる
    # visualize_visit_order(test_order, city_xy)
