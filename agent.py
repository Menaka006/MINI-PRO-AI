class Agent:

    def __init__(self, name, cpu, memory, storage, priority):
        self.name = name

        # Required resources
        self.cpu_required = cpu
        self.memory_required = memory
        self.storage_required = storage

        # Priority
        self.priority = priority

        # Allocated resources
        self.cpu_allocated = 0
        self.memory_allocated = 0
        self.storage_allocated = 0

    def utility(self):

        cpu_score = self.cpu_allocated / self.cpu_required
        memory_score = self.memory_allocated / self.memory_required
        storage_score = self.storage_allocated / self.storage_required

        total = (
            cpu_score +
            memory_score +
            storage_score
        ) / 3

        return total * 100

    def display(self):

        print(f"\nAgent: {self.name}")
        print(f"Priority: {self.priority}")

        print(
            f"CPU: {self.cpu_allocated}/"
            f"{self.cpu_required}"
        )

        print(
            f"Memory: {self.memory_allocated}/"
            f"{self.memory_required} GB"
        )

        print(
            f"Storage: {self.storage_allocated}/"
            f"{self.storage_required} GB"
        )

        print(f"Utility: {self.utility():.2f}%")