# agents/write_article_validator_agent.py

from .agent_base import AgentBase


class WriteArticleValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(
            name="WriteArticleValidatorAgent",
            max_retries=max_retries,
            verbose=verbose
        )

    def execute(self, topic, article):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert academic reviewer. "
                    "Evaluate research articles for completeness, "
                    "accuracy, structure, clarity, and adherence "
                    "to academic standards."
                )
            },
            {
                "role": "user",
                "content": (
                    "Review the following research article.\n\n"
                    "Tasks:\n"
                    "1. Assess topic coverage.\n"
                    "2. Evaluate logical structure and organization.\n"
                    "3. Check academic writing quality.\n"
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
            temperature=0.2,
            max_tokens=512
        )

        return validation