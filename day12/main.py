from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple, Set, Callable


@dataclass(frozen=True)
class Edge:
    ends: Tuple[str, str]

    @staticmethod
    def parse(desc) -> "Edge":
        return Edge(tuple(desc.split("-")))

    def connects(self, node: str) -> bool:
        return node in self.ends

    def traverse(self, from_node: str) -> str:
        if self.ends[0] == from_node:
            return self.ends[1]
        elif self.ends[1] == from_node:
            return self.ends[0]
        else:
            raise Exception(f"{self=} does not contain {from_node=}")


def generate_new_paths(
    partial_path: Tuple[str],
    edges: Set[Edge],
    allowed_new_node: Callable[[str, Tuple[str]], bool],
) -> Set[Tuple[str]]:
    new_nodes: Set[str] = {
        edge.traverse(partial_path[-1])
        for edge in edges
        if edge.connects(partial_path[-1])
    }
    return {
        (*partial_path, new_node)
        for new_node in new_nodes
        if allowed_new_node(new_node, partial_path)
    }


def silver_allowed_new_node(new_node: str, partial_path: Tuple[str]) -> bool:
    return new_node.isupper() or new_node not in partial_path


def silver(input_file_path: Path) -> int:
    return core(input_file_path, silver_allowed_new_node)


def gold_allowed_new_node(new_node: str, partial_path: Tuple[str]) -> bool:
    if new_node == "start":
        return False
    if new_node.isupper():
        return True
    if new_node not in partial_path:
        return True
    lower_cased_nodes = [
        node
        for node in partial_path
        if node.islower()
    ]
    return Counter(lower_cased_nodes).most_common()[0][1] == 1


def gold(input_file_path: Path) -> int:
    return core(input_file_path, gold_allowed_new_node)


def core(input_file_path: Path, allowed_new_node: Callable[[str, Tuple[str]], bool]) -> int:
    edges = {
        Edge.parse(desc)
        for desc in input_file_path.read_text().split("\n")
    }

    partial_paths = {("start",)}
    full_paths = set()

    while len(partial_paths) > 0:
        partial_path = partial_paths.pop()
        new_paths = generate_new_paths(partial_path, edges, allowed_new_node)
        full_paths = full_paths.union({
            new_path
            for new_path in new_paths
            if new_path[-1] == "end"
        })
        partial_paths = partial_paths.union({
            new_path
            for new_path in new_paths
            if new_path[-1] != "end"
        })

    return len(full_paths)
