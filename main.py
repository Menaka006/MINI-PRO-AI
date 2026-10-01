from agent import Agent
from resource_pool import ResourcePool

from centralized import centralized_architecture
from sequential import sequential_architecture
from peer_to_peer import peer_to_peer_architecture


# =========================================================
# CREATE AGENTS
# =========================================================

def create_agents():

    agent1 = Agent(
        "Agent A",
        cpu=5,
        memory=6,
        storage=30,
        priority="High"
    )

    agent2 = Agent(
        "Agent B",
        cpu=4,
        memory=5,
        storage=25,
        priority="Medium"
    )

    agent3 = Agent(
        "Agent C",
        cpu=6,
        memory=7,
        storage=40,
        priority="Low"
    )

    return [agent1, agent2, agent3]


# =========================================================
# CREATE RESOURCE POOL
# =========================================================

def create_resource_pool():

    print("\nEnter Resource Pool")

    cpu = int(input("Total CPU: "))
    memory = int(input("Total Memory (GB): "))
    storage = int(input("Total Storage (GB): "))

    return ResourcePool(
        cpu=cpu,
        memory=memory,
        storage=storage
    )


# =========================================================
# DISPLAY FINAL RESULTS
# =========================================================

def display_results(agents, pool):

    print("\n")
    print("=" * 60)
    print("              FINAL RESULTS")
    print("=" * 60)

    for agent in agents:

        agent.display()

    print("\n" + "-" * 50)

    print(
        f"Resource Utilization: "
        f"{pool.utilization():.2f}%"
    )

    pool.display()


# =========================================================
# MAIN PROGRAM
# =========================================================

def main():

    print("\n")
    print("=" * 60)
    print("     NEGOTIATING AGENTS FOR RESOURCE SHARING")
    print("=" * 60)

    print(
        "\nThree architectures will be compared:"
    )

    print("1. Centralized Architecture")
    print("2. Sequential / Pipeline Architecture")
    print("3. Peer-to-Peer Architecture")


    # =====================================================
    # CENTRALIZED
    # =====================================================

    agents = create_agents()
    pool = create_resource_pool()

    rounds = centralized_architecture(
        agents,
        pool
    )

    display_results(
        agents,
        pool
    )

    print(
        f"\nCentralized Negotiation Rounds: {rounds}"
    )


    # =====================================================
    # SEQUENTIAL / PIPELINE
    # =====================================================

    agents = create_agents()
    pool = create_resource_pool()

    rounds = sequential_architecture(
        agents,
        pool
    )

    display_results(
        agents,
        pool
    )

    print(
        f"\nSequential Negotiation Rounds: {rounds}"
    )


    # =====================================================
    # PEER-TO-PEER
    # =====================================================

    agents = create_agents()
    pool = create_resource_pool()

    rounds = peer_to_peer_architecture(
        agents,
        pool
    )

    display_results(
        agents,
        pool
    )

    print(
        f"\nPeer-to-Peer Negotiation Rounds: {rounds}"
    )


    # =====================================================
    # PROJECT COMPLETE
    # =====================================================

    print("\n")
    print("=" * 60)
    print("              PROJECT COMPLETED")
    print("=" * 60)


# =========================================================
# START PROGRAM
# =========================================================

if __name__ == "__main__":
    main()