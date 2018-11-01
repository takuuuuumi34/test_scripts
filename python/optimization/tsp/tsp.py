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
        self.epsilon = 0.1

        x = city_xy[:, 0]
        y = city_xy[:, 1]
        self.distance_matrix = np.sqrt((x[:, np.newaxis] - x[np.newaxis, :]) ** 2 +
                                  (y[:, np.newaxis] - y[np.newaxis, :]) ** 2)
        print("distance matrix")
        print(self.distance_matrix)

    def play(self, n_play, alpha, gamma):
        self.q = {}
        average_reward = np.zeros(n_play)
        min_dist = 10000

        for _p in range(n_play):
            # initialize episode
            # state
            start_city = 0
            destinations = list(range(self.city_xy.shape[0]))
            visited = (start_city,)
            state_history = [visited]

            current_city = start_city
            total_dist = 0
            route = np.zeros((self.city_xy.shape[0], self.city_xy.shape[0]))

            # episode
            while len(set(destinations) - set(visited)) != 0:
                actions = list(set(destinations) - set(visited))

                if visited not in self.q.keys():
                    self.q[visited] = np.zeros(self.city_xy.shape[0])

                # choice next city
                if _p < 1000 or random.random() < self.epsilon:
                    i = random.choice(actions)
                else:
                    i = actions[np.argmax(self.q[visited][actions])]

                # update q table
                new_state = visited + (i,)
                if new_state not in self.q.keys():
                    self.q[new_state] = np.zeros(self.city_xy.shape[0])

                if len(actions) > 0:
                    tmp = self.q[visited]
                    tmp[i] = alpha * (-self.distance_matrix[current_city, i] + gamma * self.q[new_state][actions].max() - tmp[i])
                    self.q[visited] = tmp

                # update state
                total_dist += self.distance_matrix[current_city, i]
                current_city = i
                state_history.append(visited)
                visited = new_state

            total_dist += self.distance_matrix[current_city, start_city]
            route[current_city, start_city] += 1

            # print(self.q)
            if min_dist >= total_dist:
                min_dist = total_dist
                l = list(visited)
                while len(l) != 1:
                    i = l.pop()
                    tmp = self.q[tuple(l)]
                    tmp[i] *= 0.9
                    self.q[tuple(l)] = tmp
            else:
                l = list(visited)
                while len(l) != 1:
                    i = l.pop()
                    tmp = self.q[tuple(l)]
                    tmp[i] *= 1.1
                    self.q[tuple(l)] = tmp

        print(self.q)


if __name__ == "__main__":
    # randomize city position
    N = 20
    MAP_SIZE = 100

    city_xy = np.array([[0, 0],
                        [1, 5],
                        [5, 9],
                        [3, 2],
                        [7, 4]])

    tsp = TSP(city_xy)
    tsp.play(100000000, 0.9, 0.05)
