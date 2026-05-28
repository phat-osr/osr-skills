# SEO Engine Setup Guide

Quick setup guide for new machines.

## 1. Clone repository

```bash
git clone <your-repo-url>
cd seo-engine
```

## 2. Setup environment variables

```bash
# Copy example and fill in your API keys
cp .env.example .env
nano .env  # Fill in your actual API keys
```

Required keys:
- `UNSPLASH_ACCESS_KEY` - Get from https://unsplash.com/developers
- `UNSPLASH_SECRET_KEY` - Get from https://unsplash.com/developers

## 3. Install Python dependencies

```bash
# Create virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt  # If you have requirements.txt
# Or manually install what's needed
```

## 4. Setup Claude Code skill symlink

```bash
# Create symlink so /osr-seo works globally in Claude Code
ln -s "$(pwd)/.claude/skills/osr-seo" ~/.claude/skills/osr-seo

# Verify
ls -la ~/.claude/skills/osr-seo
```

## 5. Verify setup

```bash
# Check if .env is loaded correctly
python -c "from config import *; print('Config loaded successfully')"

# Run a test (optional)
cd keyword_research
python -c "import config_kw; print('All imports OK')"
```

## 6. Ready to use!

```bash
# In Claude Code:
cd /path/to/seo-engine
/osr-seo 5  # Generate 5 articles
```

## Troubleshooting

### Symlink not working
```bash
# Make sure path is absolute
ln -sf "$(pwd)/.claude/skills/osr-seo" ~/.claude/skills/osr-seo
```

### Missing API keys
- Check `.env` file exists and has correct values
- Don't commit `.env` to git (it's in `.gitignore`)
