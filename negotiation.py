class NegotiationEngine:

    def __init__(self):
        self.rounds = 0

    def negotiate(
        self,
        agent,
        resource,
        requested,
        available
    ):

        self.rounds += 1

        print(
            f"{agent.name} requests "
            f"{requested} {resource}"
        )

        # Enough resource available
        if available >= requested:

            print(
                f"Accepted: {requested} {resource}"
            )

            return requested

        # No resource available
        if available <= 0:

            print(
                f"Rejected: No {resource} available"
            )

            return 0

        # Resource is limited
        print(
            f"Counter offer: {available} {resource}"
        )

        # High priority gets available resource
        if agent.priority == "High":

            print(
                f"{agent.name} accepts counter offer"
            )

            return available

        # Medium priority accepts if at least half
        elif agent.priority == "Medium":

            if available >= requested / 2:

                print(
                    f"{agent.name} accepts counter offer"
                )

                return available

            else:

                print(
                    f"{agent.name} rejects counter offer"
                )

                return 0

        # Low priority
        else:

            print(
                f"{agent.name} rejects counter offer"
            )

            return 0