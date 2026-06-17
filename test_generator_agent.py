from agents.generator_agent.agent import (
    GeneratorAgent
)

agent = GeneratorAgent()

result = (
    agent.generate_framework()
)

print(result)