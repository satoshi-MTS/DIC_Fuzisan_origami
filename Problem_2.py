# 関数の宣言
def origami_height_compare(thickness, goal_height):
	"""
	function : 目標の高さ[goal_height]と紙の厚さ[thickness]を入力すると
			   目標の高さを超えるために必要な折る回数[number_of_folds]を返す関数

	:param thickness: float
		折りたい紙の厚さ
	:param goal_height: float
		目標の高さ
	height : int (計算用)
		高さの計算のためのパラメータ
	:return number_of_folds : int
		目標の高さを超えるために必要な最小の折る回数
	"""

	# 初期値の設定
	number_of_folds = 0
	height = thickness

	# 計算
	while height < goal_height:
		height = thickness * (2 ** number_of_folds)
		number_of_folds += 1

	# 返り値の設定
	return number_of_folds


# パラメータの設定
THICKNESS_OF_COPY_PAPER = 0.00008
DISTANCE_TO_THE_PROKISIMA_KENTAURI = 4.0175e+16

# 結果の表示
print('プロキシマ・ケンタウリを超えるためには{}回、厚さ{}[m]の紙を折る必要があります'
         .format(origami_height_compare(THICKNESS_OF_COPY_PAPER, DISTANCE_TO_THE_PROKISIMA_KENTAURI),
		                                THICKNESS_OF_COPY_PAPER))
