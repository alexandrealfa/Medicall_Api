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

class EnumState(enum.Enum):
    AC = "AC"
    AL = "AL"
    AP = "AP"
    AM = "AM"
    BA = "BA"
    CE = "CE"
    DF = "DF"
    ES = "ES"
    GO = "GO"
    MA = "MA"
    MS = "MS"
    MT = "MT"
    MG = "MG"
    PA = "PA"
    PB = "PB"
    PR = "PR"
    PE = "PE"
    PI = "PI"
    RJ = "RJ"
    RN = "RN"
    RS = "RS"
    RO = "RO"
    RR = "RR"
    SC = "SC"
    SP = "SP"
    SE = "SE"
    TO = "TO"