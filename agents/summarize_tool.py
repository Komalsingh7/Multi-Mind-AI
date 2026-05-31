# agents/summarize_tool.py

from .agent_base import AgentBase


class SummarizeTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(
            name="SummarizeTool",
            max_retries=max_retries,
            verbose=verbose
        )

    def execute(self, text):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert medical summarization assistant. "
                    "Generate concise, accurate, and clinically relevant "
                    "summaries while preserving important medical information."
                )
            },
            {
                "role": "user",
                "content": (
                    "Provide a concise summary of the following medical text.\n\n"
                    f"{text}\n\n"
                    "Summary:"
                )
            }
        ]

        summary = self.call_llm(
            messages=messages,
            temperature=0.3,
            max_tokens=300
        )

        return summary