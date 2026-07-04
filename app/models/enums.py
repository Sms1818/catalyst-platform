from enum import Enum


class InterviewStatus(str, Enum):
    SCHEDULED = "scheduled"
    PROCESSING = "processing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
