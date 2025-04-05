# Termux-Based Development Philosophy

This project was built entirely inside **Termux**, a Linux terminal emulator for Android. No IDEs, no GUI editors—just pure system-level control.

## Why Termux?

- **Portable AI development**: Code, commit, and deploy directly from a smartphone
- **Self-sufficiency**: All git authentication handled via SSH keys from Termux
- **Efficiency**: CLI tools like `nano`, `ssh-agent`, and `python3` form the backbone of the stack

## Live CLI Workflow

- `nano` for code, Markdown, and env config
- `git` for version control and remote management
- `openai` + Python for AI integration
- `.env` for key security, no GUI secrets

## Example Commands Used

```bash
ssh-keygen -t ed25519 -C "email@example.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
GIT_SSH_COMMAND='ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes' git push origin main


