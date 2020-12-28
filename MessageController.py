import re
import DamageCalculator #ダメージの計算をするクラス

class MessageController:
    def __init__(self):
        self.mDmgCalc = DamageCalculator.DamageCalculator()
        self.mInputFunc = None
        
    def SetInputFunc(self, pFunction):
        self.mInputFunc = pFunction
        
    def InputProcess(self, pInput):
        #ここを入力切り分けの関数にした
        if(pInput == "/count"):
            print("カウント開始")
            self.DamageInput()
            self.PrintResult()
        else:
            print("無効")


    def DamageInput(self):
        #ダメージ入力のときには、複数の入力ループが必要。
        isEnd = False            
        while (not isEnd):
            string = self.mInputFunc()
            
            #終了の処理
            if (string == "/end"):
                print("カウントを終了します")
                isEnd = True
                continue
            
            #結果を抽出する
            dmgMatch = re.match(r'[0-9]+まん', string)

            if(dmgMatch == None):
                print("無効なダメージ入力です")
                continue
            
            #以下は有効な入力
            dmg10e4 = re.match(r'[0-9]+', dmgMatch.group())#100万->100にする
            print(dmg10e4.group() + "(万)をデータに追加しました")#debug用
            self.mDmgCalc.InsertResult("Me", int(dmg10e4.group()))#ダメージ計算機に結果を追加

    def DamageInput2(self):
        #ダメージ入力のときには、複数の入力ループが必要。
        isEnd = False            
        while (not isEnd):
            string = self.mInputFunc()
            
            #終了の処理
            if (string == "/endw"):
                print("カウントを終了します")
                isEnd = True
                continue
            
            #結果を抽出する
            dmgMatch = re.match(r'[0-9]+ちん', string)

            if(dmgMatch == None):
                print("無効なダメージ入力です")
                continue
            
            #以下は有効な入力
            dmg10e5 = re.match(r'[0-9]+', dmgMatch.group())#100万->100にする
            print(dmg10e5.group() + "(万)をデータに追加しました")#debug用
            self.mDmgCalc.InsertResult("Me", int(dmg10e5.group()))#ダメージ計算機に結果を追加        
            
    def PrintResult(self):
        self.mDmgCalc.CalcResult()#合計を計算
        for resultTaple in self.mDmgCalc.GetResult():
            print( "名前:" + resultTaple[0] + " " + "スコア:" + str(resultTaple[1]) + "万" )
        print( "合計" + str(self.mDmgCalc.GetResultTotal()) + "万" )
