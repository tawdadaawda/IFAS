import numpy as np
import cv2


class Model:

    def __init__(self):
        ### TODO: 変数を初期化 ###
        self.plugin = None
        # デバイス名。CPUならCPU
        self.device = None
        self.num_requests = None
        self.network = None
        self.input_blob = None
        self.output_blob = None
        # 推論を実行するオブジェクト。IEのネットワークを引数に取る
        self.exec_network = None

    def load_model(self, model, device, num_requests, ie, cpu_extension=None):
        ### TODO: モデルをロード ###
        self.plugin = ie

        # モデルのパス指定
        model_xml = model + ".xml"
        model_bin = model + ".bin"

        # モデルの読み込み、ネットワーク設定
        self.network = self.plugin.read_network(
            model=model_xml, weights=model_bin)

        # 推論用ネットワーク設定
        self.exec_network = self.plugin.load_network(
            network=self.network, device_name=device, num_requests=num_requests)

    def get_input_shape(self):
        ### TODO: インプットの仕様を取得 ###
        self.input_blob = next(iter(self.network.input_info))
        return self.network.input_info[self.input_blob].input_data.shape

    def convert_image(self, frame, shape):
        ### TODO: 画像を加工（インプットに合わせる） ###
        batch_size, color, height, width = shape

        img = cv2.resize(frame, (width, height))
        img = img.transpose((2, 0, 1))
        img = np.expand_dims(img, axis=0)

        return img

    def exec_net(self, image):
        ### TODO: 非同期リクエスト作成 ###
        self.exec_network.start_async(
            request_id=0, inputs={self.input_blob: image})
        return

    def wait(self):
        ### TODO: リクエスト完了まで待つ ###
        status = self.exec_network.requests[0].wait(-1)
        return status

    def get_output(self):
        ### TODO: アウトプットのBlobオブジェクトを生成、戻り値で返す ###
        self.output_blob = next(iter(self.network.outputs))
        return self.exec_network.requests[0].outputs, self.exec_network.requests[0].outputs[self.output_blob]
