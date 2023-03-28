# ライブラリの読み込み
import whisper

# ファイルの準備
file = "onseicd_202303_02.mp3"

# モデルの読み込み
model = whisper.load_model("base")

result = model.transcribe(file, fp16 = False, verbose=True, language="ja")

# 認識したテキストの出力
print(result["text"])
