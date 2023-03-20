# ライブラリの読み込み
import whisper

# モデルの読み込み
model = whisper.load_model("base")

# 音声データの読み込みと30秒のデータへのトリミング処理
audio = whisper.load_audio("onseicd_202303_02.mp3")
audio = whisper.pad_or_trim(audio)

# 音声データのログメルスペクトログラムへの変換
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# 言語の検知と出力
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# 音声の解読
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

# 認識したテキストの出力
print(result.text)
