from .agent_base import AgentBase

class QAAgent(AgentBase):

    def __init__(self, max_retries=2, verbose=True):
        super().__init__("QAAgent", max_retries, verbose)

    def execute(self, context, question):

        messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant that answers questions based ONLY on the given document."
            },
            {
                "role": "user",
                "content": f"""
DOCUMENT:
{context}

QUESTION:
{question}
"""
            }
        ]

        return self.call_llm(messages)