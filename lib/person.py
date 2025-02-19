class Person:
    APPROVED_JOBS = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Sales",
        "General Management",
        "Research & Development",
        "Marketing",
        "Purchasing"
    ]

    def __init__(self, name="Unknown", job=None):
        self._name = None  # Prevent uninitialized attributes
        self._job = None
        self.name = name  # Use setter for validation
        self.job = job  # Use setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # ✅ Convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")  # ✅ Print error message

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, job):
        if job in Person.APPROVED_JOBS:  # ✅ Fix: Reference `Person.APPROVED_JOBS`
            self._job = job
        else:
            print("Job must be in list of approved jobs.")  # ✅ Print error message instead of raising
