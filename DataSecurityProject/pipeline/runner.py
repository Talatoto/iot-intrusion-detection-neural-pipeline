from dataclasses import dataclass
from typing import Callable, List
from .context import Context

@dataclass
class Stage:
    name: str
    fn: Callable[[Context], None]
    deps: List[str]

def run_pipeline(ctx: Context, stages: List[Stage]) -> None:
    stage_map = {s.name: s for s in stages}
    done = set()

    def run_stage(name: str) -> None:
        if name in done:
            return
        if name not in stage_map:
            raise ValueError(f"Unknown stage: {name}")

        for dep in stage_map[name].deps:
            run_stage(dep)

        print(f"\n--- Running stage: {name} ---")
        stage_map[name].fn(ctx)
        done.add(name)

    for s in stages:
        run_stage(s.name)
