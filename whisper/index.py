import whisper
import wget
model = whisper.load_model("medium")

wget.download("http://www.moviesoundclips.net/download.php?id=3094&ft=mp3")

