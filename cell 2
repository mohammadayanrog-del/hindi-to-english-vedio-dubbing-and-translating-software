# ============================================================
# CELL 2 — Enter Groq API Key
# Free key at: https://console.groq.com  (no credit card needed)
# ============================================================
import ipywidgets as widgets
from IPython.display import display, clear_output, HTML
from groq import Groq

display(HTML('''
<div style="background:#f0f7ff;border:1px solid #4a90d9;border-radius:8px;padding:16px;max-width:560px">
  <h3 style="margin:0 0 8px 0">🔑 Groq API Key Required</h3>
  <p style="margin:0 0 12px 0;font-size:14px">
    Get your <b>free</b> key at <a href="https://console.groq.com" target="_blank">console.groq.com</a>
    — no credit card, generous free tier (14,400 tokens/min for LLaMA 3 70B).
  </p>
</div>
'''))

api_key_box = widgets.Password(
    placeholder='gsk_...',
    description='Groq Key:',
    layout=widgets.Layout(width='460px')
)
verify_btn  = widgets.Button(description='✅ Verify & Save', button_style='primary', icon='check')
status_out  = widgets.Output()

GROQ_CLIENT = None

def on_verify(b):
    global GROQ_CLIENT
    with status_out:
        clear_output()
        key = api_key_box.value.strip()
        if not key.startswith('gsk_'):
            print('⚠️  Key should start with "gsk_" — please check and re-enter.')
            return
        try:
            client = Groq(api_key=key)
            # Quick test call
            resp = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role":"user","content":"Say hello in one word."}],
                max_tokens=10
            )
            reply = resp.choices[0].message.content.strip()
            GROQ_CLIENT = client
            print(f'✅ Groq API key verified! Test response: "{reply}"')
            print(f'   Model  : llama-3.3-70b-versatile')
            print(f'   Status : Ready for translation')
        except Exception as e:
            print(f'❌ Verification failed: {e}')
            print('   Check your key at https://console.groq.com')

verify_btn.on_click(on_verify)
display(api_key_box, verify_btn, status_out)
