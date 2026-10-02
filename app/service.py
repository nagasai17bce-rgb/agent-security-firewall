import re

class Service:
    def run(self, value: str):
        injection = bool(re.search(r"(ignore previous|system prompt|bypass|delete all)", value, re.I))
        secret = bool(re.search(r"(api[_ -]?key|secret|password)\s*[:=]", value, re.I))
        return {
            "allow": not (injection or secret),
            "signals": {"prompt_injection": injection, "secret_pattern": secret},
        }
