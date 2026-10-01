from negotiation import NegotiationEngine


def centralized_architecture(agents, pool):

    print("\n")
    print("=" * 60)
    print("          CENTRALIZED ARCHITECTURE")
    print("=" * 60)

    print("\nCentral Manager controls all negotiations.")

    engine = NegotiationEngine()

    # High priority agents are handled first
    priority = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }

    agents = sorted(
        agents,
        key=lambda x: priority[x.priority],
        reverse=True
    )

    for agent in agents:

        print("\n" + "-" * 50)
        print(f"Central Manager → {agent.name}")
        print("-" * 50)

        # CPU
        amount = engine.negotiate(
            agent,
            "CPU",
            agent.cpu_required,
            pool.available_cpu
        )

        pool.allocate_cpu(agent, amount)

        # Memory
        amount = engine.negotiate(
            agent,
            "Memory",
            agent.memory_required,
            pool.available_memory
        )

        pool.allocate_memory(agent, amount)

        # Storage
        amount = engine.negotiate(
            agent,
            "Storage",
            agent.storage_required,
            pool.available_storage
        )

        pool.allocate_storage(agent, amount)

    return engine.rounds