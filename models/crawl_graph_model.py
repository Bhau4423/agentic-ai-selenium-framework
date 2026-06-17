from dataclasses import dataclass, field


@dataclass
class CrawlGraph:

    edges: dict = field(default_factory=dict)

    def add_edge(self, from_url: str, to_url: str):

        if not from_url or not to_url:
            return

        if from_url not in self.edges:
            self.edges[from_url] = set()

        self.edges[from_url].add(to_url)

    def get_graph(self):

        return {
            k: list(v)
            for k, v in self.edges.items()
        }