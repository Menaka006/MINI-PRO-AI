# ============================================================
# RESOURCE POOL
# Negotiating Agents for Resource Sharing
# ============================================================


class ResourcePool:

    def __init__(self, cpu, memory, storage):

        self.total_cpu = cpu
        self.total_memory = memory
        self.total_storage = storage

        # Initially available resources
        self.cpu = cpu
        self.memory = memory
        self.storage = storage


    # ========================================================
    # DISPLAY CURRENT RESOURCES
    # ========================================================

    def show_resources(self):

        print("\n----------------------------------------")
        print("        CURRENT RESOURCE POOL")
        print("----------------------------------------")

        print(f"CPU      : {self.cpu} Units")
        print(f"Memory   : {self.memory} GB")
        print(f"Storage  : {self.storage} GB")

        print("----------------------------------------")


    # ========================================================
    # CHECK WHETHER REQUEST CAN BE FULLY ALLOCATED
    # ========================================================

    def can_allocate(self, cpu, memory, storage):

        if (
            self.cpu >= cpu
            and
            self.memory >= memory
            and
            self.storage >= storage
        ):

            return True

        return False


    # ========================================================
    # ALLOCATE RESOURCES
    # ========================================================

    def allocate(self, cpu, memory, storage):

        if not self.can_allocate(cpu, memory, storage):

            return False


        self.cpu -= cpu
        self.memory -= memory
        self.storage -= storage

        return True


    # ========================================================
    # PARTIAL ALLOCATION
    # ========================================================

    def partial_allocate(self, cpu, memory, storage):

        allocated_cpu = min(cpu, self.cpu)

        allocated_memory = min(
            memory,
            self.memory
        )

        allocated_storage = min(
            storage,
            self.storage
        )


        self.cpu -= allocated_cpu

        self.memory -= allocated_memory

        self.storage -= allocated_storage


        return {
            "cpu": allocated_cpu,
            "memory": allocated_memory,
            "storage": allocated_storage
        }


    # ========================================================
    # ADD RESOURCES
    # ========================================================

    def add_resources(
        self,
        cpu=0,
        memory=0,
        storage=0
    ):

        self.cpu += cpu

        self.memory += memory

        self.storage += storage


    # ========================================================
    # MODIFY RESOURCE POOL
    # ========================================================

    def modify_resources(
        self,
        cpu=None,
        memory=None,
        storage=None
    ):

        if cpu is not None:

            self.cpu = cpu


        if memory is not None:

            self.memory = memory


        if storage is not None:

            self.storage = storage


    # ========================================================
    # RESET RESOURCE POOL
    # ========================================================

    def reset(self):

        self.cpu = self.total_cpu

        self.memory = self.total_memory

        self.storage = self.total_storage


    # ========================================================
    # GET CURRENT RESOURCES
    # ========================================================

    def get_resources(self):

        return {

            "cpu": self.cpu,

            "memory": self.memory,

            "storage": self.storage

        }