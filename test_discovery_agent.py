from agents.discovery_agent.agent import DiscoveryAgent

agent = DiscoveryAgent()

result = agent.discover(
    "https://practicetestautomation.com/practice-test-login/"
)

print(result)