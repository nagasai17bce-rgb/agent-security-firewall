# Agent Security Firewall

A lightweight security gate for agent inputs. The demo detects common prompt-injection and credential-like patterns and exposes explicit allow/block signals.

## Run
```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

## Production extensions
Use layered classifiers, secret scanners, tenant policies, tool-level authorization, rate limits, structured audit events, and continuous adversarial evaluation.
