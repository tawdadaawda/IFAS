from numpy.core.fromnumeric import squeeze
import numpy as np
from openvino.inference_engine import IECore
import sys
from . import openvino_wrap
args = sys.argv


class inferenceEngine(object):
    def __init__(self, model_name):
        ### TODO: 変数を初期化 ###
        # IECoreオブジェクト生成
        self.ie = IECore()

        # モデルオブジェクト生成
        self.model = openvino_wrap.Model()

        # モデル名指定
        self.model_name = model_name

    def infer(self, image):
        ### TODO: 画像に対し推論実行 ###
        # モデルのロード
        self.model.load_model(model=self.model_name,
                              device='CPU', num_requests=1, ie=self.ie)

        # インプットの仕様を取得
        input_shape = self.model.get_input_shape()

        # 引数で受けた画像ファイルを、インプットの仕様に合わせリシェイプ
        image_for_inference = self.model.convert_image(image, input_shape)

        # 推論実行
        self.model.exec_net(image_for_inference)
        self.model.wait()

        # 推論結果を取得。
        blob, result = self.model.get_output()

        # opencvで使えるように次元を削減
        output = np.squeeze(result)

        return output
