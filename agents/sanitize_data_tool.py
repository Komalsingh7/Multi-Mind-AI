# agents/sanitize_data_tool.py

from .agent_base import AgentBase


class SanitizeDataTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(
            name="SanitizeDataTool",
            max_retries=max_retries,
            verbose=verbose
        )

    def execute(self, medical_data):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert healthcare data privacy assistant. "
                    "Your task is to remove or anonymize all Protected Health "
                    "Information (PHI) from medical records while preserving "
                    "the medical meaning of the text."
                )
            },
            {
                "role": "user",
                "content": (
                    "Remove all Protected Health Information (PHI) from the "
                    "following medical data.\n\n"
                    f"{medical_data}\n\n"
                    "Return only the sanitized data."
                )
            }
        ]

        sanitized_data = self.call_llm(
            messages=messages,
            temperature=0.2,
            max_tokens=500
        )

        return sanitized_data