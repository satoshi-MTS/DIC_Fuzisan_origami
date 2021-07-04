# モジュールのインポート
import math


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


# 関数の宣言
def compare_folding_paper(thickness, number_of_folds):
	"""
	function : 厚さ[thickness]の紙を[number_of_folds]回折るために必要な紙の長さ[long]を求める関数
	:param thickness: int
		折る紙の厚さ
	:param number_of_folds : int
		折る回数
	:return: long
		必要な紙の長さ
	"""

	# 計算
	long = (math.pi * thickness / 6) * (2 ** number_of_folds + 4) * (2 ** number_of_folds - 1)
	# 返り値の設定
	return long


# パラメータの設定
HEIGHT_OF_MT_FUJI = 3776
DISTANCE_TO_THE_MOON = 3844e+5
DISTANCE_TO_THE_PROKISIMA_KENTAURI = 4.0175e+16
THICKNESS_OF_COPY_PAPER = 0.00008

# それぞれの高さを超えるために必要なコピー用紙の折る回数の計算
number_of_folding_fuji = origami_height_compare(THICKNESS_OF_COPY_PAPER, HEIGHT_OF_MT_FUJI)
number_of_folding_moon = origami_height_compare(THICKNESS_OF_COPY_PAPER, DISTANCE_TO_THE_MOON)
number_of_folding_prokisima = origami_height_compare(THICKNESS_OF_COPY_PAPER, DISTANCE_TO_THE_PROKISIMA_KENTAURI)

# それぞれの高さを超えるために必要なコピー用紙を折る回数を折るために必要な紙の長さの計算
required_paper_length_to_reach_fuji = compare_folding_paper(THICKNESS_OF_COPY_PAPER, number_of_folding_fuji)
required_paper_length_to_reach_moon = compare_folding_paper(THICKNESS_OF_COPY_PAPER, number_of_folding_moon)
required_paper_length_to_reach_prokishima = compare_folding_paper(THICKNESS_OF_COPY_PAPER, number_of_folding_prokisima)

# 結果の表示
print('「富士山」に届くために必要な紙の長さは{:e}[m]です。'.format(required_paper_length_to_reach_fuji))
print('「月」に届くために必要な紙の長さは{:e}[m]です。'.format(required_paper_length_to_reach_moon))
print('「最も近い太陽以外の恒星」に届くために必要な紙の長さは{:e}[m]です。'.format(required_paper_length_to_reach_prokishima))
