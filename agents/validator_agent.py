# agents/validator_agent.py

from .agent_base import AgentBase


class ValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(
            name="ValidatorAgent",
            max_retries=max_retries,
            verbose=verbose
        )

    def execute(self, topic, article):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert academic reviewer. "
                    "Evaluate research articles for accuracy, completeness, "
                    "logical organization, clarity, evidence quality, and "
                    "adherence to academic standards."
                )
            },
            {
                "role": "user",
                "content": (
                    "Review the following research article.\n\n"
                    "Tasks:\n"
                    "1. Check whether the article adequately covers the topic.\n"
                    "2. Evaluate logical flow and organization.\n"
                    "3. Assess academic writing quality.\n"
                    "4. Identify strengths and weaknesses.\n"
                    "5. Rate the article from 1 to 5.\n\n"
                    f"Topic:\n{topic}\n\n"
                    f"Article:\n{article}\n\n"
                    "Validation Report:"
                )
            }
        ]

        validation = self.call_llm(
            messages=messages,
            temperature=0.3,
            max_tokens=500
        )

        return validation