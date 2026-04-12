# Telegram Bot on Hugging Face Spaces

This Telegram bot is deployed on Hugging Face Spaces to reduce codespace usage.

## Deployment Instructions

### 1. Create a Hugging Face Space
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Choose:
   - **Space name**: Your desired space name
   - **License**: MIT or your preferred license
   - **Hardware**: CPU basic (free tier)
   - **Space SDK**: Flask
   - **Git repository**: Clone your existing repository or create new one

### 2. Upload Your Files
Upload these files to your Hugging Face Space:
- `app.py` (main application file)
- `requirements.txt` (dependencies)
- `users.txt` (authorized users)
- `.env` (environment variables - create this file)

### 3. Set Environment Variables
In your Hugging Face Space settings, add these environment variables:
- `BOT_TOKEN`: Your Telegram bot token
- `SPACE_NAME`: Your Hugging Face space name

### 4. Deploy
The space will automatically build and deploy once you push the files.

## Files Description

- `app.py`: Main Flask application with Telegram bot integration
- `requirements.txt`: Python dependencies
- `users.txt`: List of authorized Telegram user IDs
- `.env.example`: Example environment variables file

## Benefits of Hugging Face Spaces

- **Free tier**: 2 vCPU, 8GB RAM always available
- **No codespace hours**: Runs continuously without consuming your codespace quota
- **Public URL**: Your bot gets a permanent public URL
- **Easy deployment**: Automatic builds when you push changes

## Migration from Codespace

1. Copy your bot logic from `m.py` to the appropriate handlers in `app.py`
2. Update your bot token in environment variables
3. Upload authorized users to `users.txt`
4. Deploy to Hugging Face Spaces

## Webhook Setup

The bot uses webhooks instead of polling, which is more efficient:
- Automatically sets webhook when the app starts
- Receives updates instantly when users send messages
- No need for continuous polling
