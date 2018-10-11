import random


def hangman(word):
    """
    :param word: answer word
    :return: none
    """
    wrong = 0                           # wrong:間違えた回数を保持
    stages = ["",                       # stages:hangmanの絵を1行ずつリストで保持
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    rletters = list(word)               # rletters:word の文字を1文字ずつの要素に分解したリスト
    board = ['_'] * len(word)           # board:ヒントの文字列リスト。
    win = False                         # win:ゲームに勝ったかどうかの状態を保持
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:       # stagesの要素数回まちがえたらゲーム終了
        print('\n')                     # 見栄えのために改行
        char = input('1文字を予想： ')    # char:入力文字を保持
        if char in rletters:            # 入力された文字がrlettersにあった場合
            cind = rletters.index(char)
            board[cind] = char          # 入力された文字で、board内を置き換え
            rletters[cind] = '$'        # rlettersの該当文字を$で置き換えて消す
        else:
            wrong += 1                  # 間違った回数をインクリメント

        print(" ".join(board))          # board内の文字を空白を入れて表示する
        e = wrong + 1                   # e:stagesの表示の終了位置を保持（+1しないと手前まで）
        print('\n'.join(stages[0:e]))   # 改行の間に、stagesの行を挿入する

        if '_' not in board:                # boardの中に_がなくなったら
            print('あなたの勝ち！')
            print(" ".join(board))      # 正解を表示
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け！正解は {}.'.format(word))


word_list = ['orange', 'apple', 'peach', 'kiwi']
hangman(word_list[random.randint(0, 3)])
