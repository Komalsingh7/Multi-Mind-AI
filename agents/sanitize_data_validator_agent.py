# agents/sanitize_data_validator_agent.py

from .agent_base import AgentBase


class SanitizeDataValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(
            name="SanitizeDataValidatorAgent",
            max_retries=max_retries,
            verbose=verbose
        )

    def execute(self, original_data, sanitized_data):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert healthcare privacy auditor. "
                    "Your task is to validate whether all Protected Health "
                    "Information (PHI) has been successfully removed from "
                    "medical records."
                )
            },
            {
                "role": "user",
                "content": (
                    "Compare the original medical data with the sanitized data.\n\n"
                    "Tasks:\n"
                    "1. Identify any remaining PHI.\n"
                    "2. Explain any privacy risks.\n"
                    "3. Rate the sanitization quality from 1 to 5.\n"
                    "4. Provide recommendations if improvements are needed.\n\n"
                    f"Original Data:\n{original_data}\n\n"
                    f"Sanitized Data:\n{sanitized_data}\n\n"
                    "Validation Report:"
                )
            }
        ]

        validation = self.call_llm(
            messages=messages,
            temperature=0.2,
            max_tokens=512
        )

        return validation