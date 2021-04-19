import enum


class EnumEmergency(enum.Enum):
    EMERGENCY = "emergency"
    VERY_URGENT = "very urgent"
    URGENT = "urgent"
    LESS_URGENT = "less urgent"
    NOT_URGENT = "not urgent"


class EnumType(enum.Enum):
    DOCTOR = "doctor"
    PATIENT = "patient"
    SUPER_USER = "superuser"
