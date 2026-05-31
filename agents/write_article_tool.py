# agents/write_article_tool.py

from .agent_base import AgentBase


class WriteArticleTool(AgentBase):
    def __init__(self, max_retries=3, verbose=True):
        super().__init__(
            name="WriteArticleTool",
            max_retries=max_retries,
            verbose=verbose
        )

    def execute(self, topic, outline=None):
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an expert academic researcher and writer. "
                    "Generate well-structured, detailed, and professional "
                    "research articles using formal academic language."
                )
            }
        ]

        user_prompt = (
            f"Write a comprehensive research article on the following topic.\n\n"
            f"Topic: {topic}\n\n"
        )

        if outline and outline.strip():
            user_prompt += (
                f"Use the following outline as guidance:\n"
                f"{outline}\n\n"
            )

        user_prompt += (
            "The article should include:\n"
            "- Title\n"
            "- Abstract\n"
            "- Introduction\n"
            "- Main Discussion\n"
            "- Conclusion\n"
            "- Future Scope (if applicable)\n\n"
            "Article:"
        )

        messages.append(
            {
                "role": "user",
                "content": user_prompt
            }
        )

        article = self.call_llm(
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )

        return article