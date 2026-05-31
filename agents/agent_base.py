from abc import ABC, abstractmethod
from loguru import logger
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Initialize model
model = genai.GenerativeModel("gemini-2.5-flash")


class AgentBase(ABC):
    def __init__(self, name, max_retries=2, verbose=True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def call_llm(
        self,
        messages,
        temperature=0.7,
        max_tokens=150
    ):
        retries = 0

        while retries < self.max_retries:
            try:
                # Convert chat messages to a single prompt
                prompt_parts = []

                for msg in messages:
                    role = msg.get("role", "user")
                    content = msg.get("content", "")
                    prompt_parts.append(f"{role}: {content}")

                prompt = "\n".join(prompt_parts)

                if self.verbose:
                    logger.info(
                        f"[{self.name}] Sending prompt to Gemini"
                    )

                response = model.generate_content(prompt)

                # Safe extraction
                if hasattr(response, "text"):
                    reply = response.text
                else:
                    reply = str(response)

                if self.verbose:
                    logger.info(
                        f"[{self.name}] Received response"
                    )

                return reply

            except Exception as e:
                retries += 1

                logger.error(
                    f"[{self.name}] Error during Gemini call: {e}. "
                    f"Retry {retries}/{self.max_retries}"
                )

        raise Exception(
            f"[{self.name}] Failed after "
            f"{self.max_retries} retries."
        )

    # Backward compatibility with existing code
    def call_openai(
        self,
        messages,
        temperature=0.7,
        max_tokens=150
    ):
        return self.call_llm(
            messages,
            temperature=temperature,
            max_tokens=max_tokens
        )