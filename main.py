import os
import sys
from distutils.dir_util import copy_tree

import execute


def main():
    path = "./result/textures"
    copy_tree("./textures", path)

    print("[EC] >> Activate")
    if not os.path.exists(path):
        print("[EC] >> ファイル内に変換対象のファイルが入っていません。"
              "[EC] >> 実行ファイルと同じディレクトリ内にtexturesファイルを入れた後、再度実行してください。\n")
        sys.exit()

    exe_mode = int(input("[EC] >> 処理内容を選んでください(グレースケール:0, 色抽出:1): "))
    if not 0 <= exe_mode <= 1:
        print("[EC] >> 入力値が不正です。指定された数値を入力してください")
        sys.exit()

    if exe_mode == 0:
        print("[EC] >> 処理を開始します。(処理予想時間: 1~5分)")
        for pathname, dir_names, filenames in os.walk(path):
            for filename in filenames:
                if filename.endswith(".png"):
                    execute.grayscale(pathname + "/" + filename)

        print("[EC] >> 処理が完了しました。")
        sys.exit()

    color_mode = int(input("[EC] >> 抜き出したい色を選択してください(赤:0, 緑:1, 青:2): "))
    if not 0 <= color_mode <= 2:
        print("[EC] >> 入力値が不正です。指定された数値を入力してください")
        sys.exit()

    color_range = (int(input("[EC] >> 抜き出す色の最小値を入力してください(0 ~ 255): ")),
                   int(input("[EC] >> 抜き出す色の最大値を入力してください(0 ~ 255, 最小値より大きい): ")))
    if color_range[0] > color_range[1]:
        print("[EC] >> 最大値の数値が不正です。最大値より小さい値を入力してください")
        sys.exit()

    elif not 0 <= color_range[0] <= 255 or not 0 <= color_range[1] <= 255:
        print("[EC] >> 入力値が不正です。範囲内の数値を指定してください")
        sys.exit()

    threshold = int(input("[EC] >> \"しきい値\"は抜き出したい色以外の色の差の許容値となります\n"
                          "[EC] >> これが大きいほど抜き出したい色の近似色を拾いますが、想定していない色を拾う可能性が高くなります\n"
                          "[EC] >> しきい値を入力してください(0 ~ 255): "))
    if not 0 <= threshold <= 255:
        print("[EC] >> 入力値が不正です。範囲内の数値を指定してください")
        sys.exit()

    print("[EC] >> 処理を開始します...(処理予想時間: 1~5分)")
    for pathname, dir_names, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".png"):
                execute.extractColor(pathname + "/" + filename, color_mode, color_range, 15)

    print("[EC] >> 処理が完了しました。")


if __name__ == "__main__":
    main()
