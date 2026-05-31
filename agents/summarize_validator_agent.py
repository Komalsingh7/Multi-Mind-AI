# agents/summarize_validator_agent.py

from .agent_base import AgentBase


class SummarizeValidatorAgent(AgentBase):
    def __init__(self, max_retries=2, verbose=True):
        super().__init__(
            name="SummarizeValidatorAgent",
            max_retries=max_retries,
            verbose=verbose
        )

    def execute(self, original_text, summary):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert medical summary evaluator. "
                    "Assess summaries for accuracy, completeness, "
                    "clinical relevance, and conciseness."
                )
            },
            {
                "role": "user",
                "content": (
                    "Compare the original medical text with its summary.\n\n"
                    "Tasks:\n"
                    "1. Check factual accuracy.\n"
                    "2. Identify any missing important information.\n"
                    "3. Evaluate conciseness and clarity.\n"
                    "4. Rate the summary from 1 to 5.\n\n"
                    f"Original Text:\n{original_text}\n\n"
                    f"Summary:\n{summary}\n\n"
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