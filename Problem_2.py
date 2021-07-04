# 関数の宣言
def origami_height_compare(thickness, goal_height):
	"""
	function : 目標の高さと対象の紙の厚さを入力すると目標の高さを超えるために必要な折る回数を返す関数

	:param thickness: float
		折りたい紙の厚さ
	:param goal_height: float
		目標の高さ
	height : int (計算用)
		高さの計算のためのパラメータ
	:return number_of_folding : int
		目標の高さを超えるために必要な最小の折る回数
	"""

	# 初期値の設定
	number_of_folding = 0
	height = thickness

	# 計算
	while height < goal_height:
		height = thickness * (2 ** number_of_folding)
		number_of_folding += 1

	# 返り値の設定
	return number_of_folding


thickness_of_copy_paper = 0.00008
height_of_prokishima = 4.0175e+16

print('プロキシマ・ケンタウリを超えるためには{}回、厚さ{}[m]の紙を折る必要があります'
	            .format(origami_height_compare(thickness_of_copy_paper, height_of_prokishima), thickness_of_copy_paper))
