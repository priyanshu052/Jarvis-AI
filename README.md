# Jarvis-AI

## Setup

1. Install the Python dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

2. Create your local configuration file and add your API keys:

   ```powershell
   Copy-Item config.example.json config.json
   ```

   `config.json` is ignored by Git. Do not commit API keys or other credentials.

3. Set `OPENAI_API_KEY` in your environment if you want to use the OpenAI
   conversation feature.

4. Start Jarvis:

   ```powershell
   python main.py
   ```

Personal voice samples and runtime data are kept locally and are not tracked by
Git.
