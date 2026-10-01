from negotiation import NegotiationEngine


def sequential_architecture(agents, pool):

    print("\n")
    print("=" * 60)
    print("       SEQUENTIAL / PIPELINE ARCHITECTURE")
    print("=" * 60)

    print(
        "\nAgents negotiate one after another "
        "through a pipeline."
    )

    engine = NegotiationEngine()

    for agent in agents:

        print("\n" + "-" * 50)
        print(f"Pipeline → {agent.name}")
        print("-" * 50)

        # Stage 1 - CPU
        amount = engine.negotiate(
            agent,
            "CPU",
            agent.cpu_required,
            pool.available_cpu
        )

        pool.allocate_cpu(agent, amount)

        # Stage 2 - Memory
        amount = engine.negotiate(
            agent,
            "Memory",
            agent.memory_required,
            pool.available_memory
        )

        pool.allocate_memory(agent, amount)

        # Stage 3 - Storage
        amount = engine.negotiate(
            agent,
            "Storage",
            agent.storage_required,
            pool.available_storage
        )

        pool.allocate_storage(agent, amount)

    return engine.rounds