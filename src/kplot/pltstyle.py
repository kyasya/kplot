import matplotlib as plt
# plt.rcParams["font.family"] = "Times New Roman"     #全体のフォントを設定

plt.rcParams["font.size"] = 16                      #フォントの大きさ
plt.rcParams["xtick.direction"] = "in"              #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams["ytick.direction"] = "in"              #y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams["xtick.minor.visible"] = True          #x軸補助目盛りの追加
plt.rcParams["ytick.minor.visible"] = True          #y軸補助目盛りの追加
plt.rcParams["xtick.major.width"] = 1.0             #x軸主目盛り線の線幅
plt.rcParams["ytick.major.width"] = 1.0             #y軸主目盛り線の線幅
plt.rcParams["xtick.minor.width"] = 1.0             #x軸補助目盛り線の線幅
plt.rcParams["ytick.minor.width"] = 1.0             #y軸補助目盛り線の線幅
plt.rcParams["xtick.major.size"] = 10               #x軸主目盛り線の長さ
plt.rcParams["ytick.major.size"] = 10               #y軸主目盛り線の長さ
plt.rcParams["xtick.minor.size"] = 5                #x軸補助目盛り線の長さ
plt.rcParams["ytick.minor.size"] = 5                #y軸補助目盛り線の長さ
plt.rcParams['xtick.top'] = False                   #x軸の上部目盛り
plt.rcParams['ytick.right'] = False                 #y軸の右部目盛り
plt.rcParams["axes.linewidth"] = 1.0                #囲みの太さ