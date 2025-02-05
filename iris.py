import random
import numpy as np

label_name_list = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

# bezdekIris.dataの各一行の構造体（クラス）
#
# X = [1, x1, ..., x4]の5次元
# Wベクトルと内積計算しやすいように先頭は1
# なぜならw0はそのまま加算するから（w0 * 1 = w0）
#
# y = 正解ラベル（読み込んだ行の花の種類）
class data_obj:
    def __init__(self, a_line_list, label_name):
        self.X = np.array([1] + [x for x in a_line_list if x != label_name], dtype=float)
        self.y = label_name

# bezdekIris.dataから指定した花の種類のデータのみを返却
def get_data(label_name):
    with open('./bezdekIris.data', 'r') as bezdekIris:
        a_label_dataset = []

        for a_line in bezdekIris:
            a_line_list = a_line[:-1].split(',')

            if a_line_list[-1] == label_name:
                a_label_dataset.append(data_obj(a_line_list, label_name))

    # data_obj型（構造体）が格納されているリスト
    return a_label_dataset

# 初期化関数
# 線形分離を行う前に一回行う
def initialize(input_a, input_b):
    # 0~1
    p = random.uniform(0, 1)
    # -1~1のリストを内包表記で定義
    # W = [0.3, 0.4, 0.02, -0.3, 0.9]
    W = [random.uniform(-1, 1) for _ in range(5)]

    # 分類したい2クラスのデータを取得
    dataset_a = get_data(label_name_list[input_a])
    dataset_b = get_data(label_name_list[input_b])

    # 合体
    dataset = dataset_a + dataset_b
    # そのまま用いず、花の種類が混ざるようシャッフル
    random.shuffle(dataset)

    return p, np.array(W, dtype=float), dataset

def g(W, X):
    return np.dot(W, X)

# 学習関数
def learning(p, W, dataset, a, b):
    # while文を実行する上限回数
    max_roop = 9999
    # 学習した（while文を実行した）回数
    learning_count = 0

    while True:
        # 線形分離可能ならTrue
        # Trueで初期化
        separable = True

        for data in dataset:
            X = data.X
            y = g(W, X)

            # y = g(X) で予想される結果（花の種類）と
            # 実際の花の種類（正解ラベル）が不一致なら
            # 誤り訂正を行う
            if y < 0 and data.y == label_name_list[a]:
                W = W + p * X
                separable = False
            elif y > 0 and data.y == label_name_list[b]:
                W = W - p * X
                separable = False

        # dataset（for文）を通して一度も誤り訂正しなかった
        # or
        # while文を上限回数まで実行した（線形分離不可）
        if separable == True or max_roop < learning_count:
            break

        learning_count = learning_count + 1

    if separable == True:
        print('separable / learning count : ' + str(learning_count) + ' / w = ' + str(W))
    else:
        print('not separable')

def main():
    print('select two class')
    print('setosa ... 0 / versicolor ... 1 / virginica ... 2')
    input_a = int(input('>>> '))
    input_b = int(input('>>> '))

    if input_a < 0 or 2 < input_a or input_b < 0 or 2 < input_b:
        print('input error')
        return

    # 学習係数pと重みベクトルWを固定にするかランダムにするか
    print('random ... 0 / fixed ... 1')
    input_c = int(input('>>> '))

    if input_c < 0 or 1 < input_c:
        print('input error')
        return

    print('how many do you run ?')
    input_d = int(input('>>> '))

    if input_d < 0:
        print('input error')
        return

    # input_d回実験をする
    for _ in range(input_d):
        # 初期化関数実行
        # p = 学習係数
        # W = 重みベクトル
        # dataset = 学習データ（学習構造体）が格納されたリスト
        p, W, dataset = initialize(input_a, input_b)

        # 固定の値を使用する場合のみ実行
        if input_c == 1:
            p = 0.5
            w = 0.1
            W = np.array([w for _ in range(5)], dtype=float)

        # 学習開始
        learning(p, W, dataset, input_a, input_b)

if __name__ == '__main__':
    main()
