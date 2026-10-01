from negotiation import NegotiationEngine


def peer_to_peer_architecture(agents, pool):

    print("\n")
    print("=" * 60)
    print("          PEER-TO-PEER ARCHITECTURE")
    print("=" * 60)

    print(
        "\nAgents communicate directly with each other."
    )

    engine = NegotiationEngine()

    # ---------------------------------------------
    # Peer negotiation
    # ---------------------------------------------

    for i in range(len(agents)):

        current = agents[i]

        print("\n" + "-" * 50)
        print(
            f"{current.name} negotiating with peers"
        )
        print("-" * 50)

        for j in range(len(agents)):

            if i == j:
                continue

            peer = agents[j]

            print(
                f"{current.name} ↔ {peer.name}"
            )

            if current.priority == "High":

                print(
                    f"{current.name}: "
                    f"High priority request"
                )

            elif current.priority == "Medium":

                print(
                    f"{current.name}: "
                    f"Medium priority request"
                )

            else:

                print(
                    f"{current.name}: "
                    f"Low priority request"
                )

    # ---------------------------------------------
    # Allocate resources after peer negotiation
    # ---------------------------------------------

    for agent in agents:

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