# ============================================================
# CELL 1 — Install All Dependencies
# ============================================================
import subprocess

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

print('📦 Installing system packages...')
run('apt-get install -y ffmpeg > /dev/null 2>&1')

print('📦 Installing Python packages...')
run('pip install -q whisper-timestamped pydub librosa natsort moviepy yt-dlp')
run('pip install -q torch torchaudio --index-url https://download.pytorch.org/whl/cu118')
run('pip install -q transformers sentencepiece accelerate')
run('pip install -q groq')        # Groq Python SDK
run('pip install -q f5-tts')      # F5-TTS for voice cloning

print()
print('✅ All dependencies installed!')
print('ℹ️  Translation : Groq API — LLaMA 3 70B (free, fast, no local GPU needed)')
print('ℹ️  TTS         : F5-TTS with voice cloning')
print('ℹ️  STT         : Whisper large-v3 (local)')
