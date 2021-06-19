# realsenseをPythonで使うときのライブラリ
import pyrealsense2 as rs
# 画像ファイルの処理用Numpy
import numpy as np


class Realsense(object):
    def __init__(self):
        ### TODO: 変数を初期化 ###
        # Realsenseのパイプライン作成
        self.pipeline = rs.pipeline()

        # パイプラインへ流すのコンフィグ作成
        self.config = rs.config()

        # 深度情報（背景除去に利用）
        self.clipping_distance = None

        # alignオブジェクトを作成。alignで深度情報をカラー情報と統合できる。
        self.align = None

        # 背景除去用の色指定
        self.background_color = 153

    def __del__(self):
        ### TODO: Realsenseのパイプライン削除 ###
        self.pipeline.stop()

    def configurePipeline(self):
        ### TODO: パイプラインにコンフィグを入れ設定 ###
        # デバイス情報取得
        pipeline_wrapper = rs.pipeline_wrapper(self.pipeline)
        pipeline_profile = self.config.resolve(pipeline_wrapper)
        device = pipeline_profile.get_device()
        device_product_line = str(device.get_info(rs.camera_info.product_line))

        # 深度カメラのストリーム設定
        self.config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

        # カラーカメラのストリーム設定
        if device_product_line == 'L500':
            self.config.enable_stream(
                rs.stream.color, 960, 540, rs.format.bgr8, 30)
        else:
            self.config.enable_stream(
                rs.stream.color, 640, 480, rs.format.bgr8, 30)

    def startStream(self):
        ### TODO: パイプラインでストリーム開始 ###
        # ストリーミング開始
        profile = self.pipeline.start(self.config)

        # 深度センサーのdepth scaleを取得(深度画像の画素値をメートルに換算する際に必要)
        depth_sensor = profile.get_device().first_depth_sensor()
        depth_scale = depth_sensor.get_depth_scale()
        print("Depth Scale is: ", depth_scale)

        # clipping_distance_in_meters に指定した距離(メートル)から奥の背景を除去する。
        clipping_distance_in_meters = 1.8

        # メートル→センサーの深度に変換。
        self.clipping_distance = clipping_distance_in_meters / depth_scale

        # alignオブジェクトを設定
        align_to = rs.stream.color
        self.align = rs.align(align_to)

    def getFrame(self):
        ### TODO: 通常のカラー画像と、背景除去済みのカラー画像を返す ###

        # カラーと深度のフレームを取得
        frames = self.pipeline.wait_for_frames()

        # カラーのフレームと深度のフレームを統合
        aligned_frames = self.align.process(frames)

        # 統合したフレームを取得。 サイズは 640x480
        aligned_depth_frame = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()

        # 深度画像を生成(numpy)
        depth_image = np.asanyarray(aligned_depth_frame.get_data())

        # カラー画像を生成(numpy)
        color_image = np.asanyarray(color_frame.get_data())

        # 背景除去用設定
        self.background_color = 153
        # 深度イメージは1チャネル、カラーは3チャネルなので、深度イメージのチャネル数をカラーイメージに合わせる
        depth_image_3d = np.dstack((depth_image, depth_image, depth_image))

        # カラー画像から背景を除去
        bg_removed = np.where((depth_image_3d > self.clipping_distance) | (
            depth_image_3d <= 0), self.background_color, color_image)

        # カラー画像と、背景除去した画像をそれぞれnumpy配列で返す。
        return color_image, bg_removed
