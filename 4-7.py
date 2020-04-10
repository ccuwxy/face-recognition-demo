import numpy as np


# 零均值化，即中心化，是数据处理的预处理方法
def zero_centered(data):
    matrix_mean = np.mean(data, axis=0)
    return data - matrix_mean


def pca_eig(data, n):
    new_data = zero_centered(data)
    cov_mat = np.dot(new_data.T, new_data)
    eig_values, eig_vectors = np.linalg.eig(np.mat(cov_mat))
    value_indices = np.argsort(eig_values)
    n_vectors = eig_vectors[:, value_indices[-1: -(n + 1): -1]]
    return new_data * n_vectors


def pca_svg(data, n):
    new_data = zero_centered(data)
    cov_mat = np.dot(new_data.T, new_data)
    U, s, V = np.linalg.svd(cov_mat)
    pc = np.dot(new_data, U)
    return pc[:, 0]


def unit_test():
    data = np.array([
        [2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0],
        [2.3, 2.7], [2, 1.6], [1, 1.1], [1.5, 1.6], [1.1, 0.9]
    ])
    result_eig = pca_eig(data, 1)
    print(result_eig)
    result_svd = pca_svg(data, 1)
    print(result_svd)


if __name__ == '__main__':
    unit_test()
