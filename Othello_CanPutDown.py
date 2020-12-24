#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
#Othello

class Othello_CanPutDown():
    def reverse_check(self, array, next_str):#check(self, ボタンの配列情報, 次のプレイヤーの情報)
        for i in range(8):
            for j in range(8):
                #打てる場所の情報を初期化する
                if array[i * 8 + j] == "x":#xはまだ打たれていない箇所 0~63  
                    array[i * 8 + j] = ""# "" ＝ 空である
        v = True
        if next_str == "○":
            #次のプレイヤーが白の時
            for i in range(8):
                for j in range(8):
                    if array[i * 8 + j] == "○":
                        for k in range(3):#白の時，周り８マス中心の白１マス，
                            for l in range(3):
                                #白の周囲８マスに黒があるかを探す button43白○(k=1,l=1)を基準とした場合は

                                #button32白○（1）button33白○（2），button34白○（3）
                                #button42白○（4）button43白○（5），button44白○（6）
                                #button52白○（7）button53白○（8），button54白○（9）
                                if (k == 1 and l == 1) or (j == 0 and l == 0) or (j == 7 and l == 2) or (i == 0 and k == 0) or (i == 7 and k == 2):
                                    #範囲外を探す場合をスルー
                                    continue
                                else:
                                    if array[8 * i + j + 8 * k + l - 9] == "●":
                                        #黒があったら、その延長線上に空欄があるかを探す
                                        #○●●x　or ○●●|延長線上が範囲外の可能性もある．
                                        x = j + l - 1 #移動した先のx座標
                                        y = i + k - 1 #移動した先のy座標
                                        x_2 = l - 1 #元のx座標から何マス移動したか
                                        y_2 = k - 1 #元のy座標から何マス移動したか
                                        while v:
                                            if x >= 0 and x <= 7 and y >= 0 and y <= 7:
                                                #範囲外を探す場合をスルー
                                                if array[8 * y + x] == "":
                                                    #空欄だったら打てる場所なので、xを配列に入れる
                                                    array[8 * y + x] = "x"
                                                    v = False
                                                elif array[8 * y + x] == "●":
                                                    #黒があったら、その延長線上に空欄があるかを探す
                                                    x = x + x_2#x座標の更新
                                                    y = y + y_2#y座標の更新
                                                else:
                                                    v = False
                                            else:
                                                v = False
                                        v = True
        elif next_str == "●":
            #次のプレイヤーが黒の時
            for i in range(8):
                for j in range(8):
                    if array[i * 8 + j] == "●":
                        for k in range(3):
                            for l in range(3):
                                #黒の周囲８マスに白があるかを探す
                                if (k == 1 and l == 1) or (j == 0 and l == 0) or (j == 7 and l == 2) or (i == 0 and k == 0) or (i == 7 and k == 2):
                                    #範囲外を探す場合をスルー
                                    continue
                                else:
                                    if array[8 * i + j + 8 * k + l - 9] == "○":
                                        #白があったら、その延長線上に空欄があるかを探す
                                        x = j + l - 1 #移動した先のx座標
                                        y = i + k - 1 #移動した先のy座標
                                        x_2 = l - 1 #元のx座標から何マス移動したか
                                        y_2 = k - 1 #元のy座標から何マス移動したか
                                        while v:
                                            if x >= 0 and x <= 7 and y >= 0 and y <= 7:
                                                #範囲外を探す場合をスルー
                                                if array[8 * y + x] == "":
                                                    #空欄だったら打てる場所なので、xを配列に入れる
                                                    array[8 * y + x] = "x"
                                                    v = False
                                                elif array[8 * y + x] == "○":
                                                    #白があったら、その延長線上に空欄があるかを探す
                                                    x = x + x_2#x座標の更新
                                                    y = y + y_2#y座標の更新
                                                else:
                                                    v = False
                                            else:
                                                v = False
                                        v = True
        return array