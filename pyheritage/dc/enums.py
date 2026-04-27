# -*- coding: utf-8 -*-

"""DCMI Type Vocabulary;

"""


from enum import Enum


__all__ = ('DCMIType', 'AccrualMethod', 'AccrualPeriodicity', 'AccrualPolicy', )


class DCMIType(str, Enum):
    """DCMI Type Vocabulary;

    https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/

    """

    COLLECTION = "Collection"
    DATASET = "Dataset"
    EVENT = "Event"
    IMAGE = "Image"
    INTERACTIVE_RESOURCE = "InteractiveResource"
    MOVING_IMAGE = "MovingImage"
    PHYSICAL_OBJECT = "PhysicalObject"
    SERVICE = "Service"
    SOFTWARE = "Software"
    SOUND = "Sound"
    STILL_IMAGE = "StillImage"
    TEXT = "Text"


# ******************************************************************************************************************* #


class AccrualMethod(str, Enum):
    """Collection accrual methods;

    https://www.dublincore.org/specifications/dublin-core/collection-description/accrual-method/

    """

    DEPOSIT = "Deposit"
    DONATION = "Donation"
    PURCHASE = "Purchase"
    ITEM_CREATION = "ItemCreation"


# ******************************************************************************************************************* #


class AccrualPeriodicity(str, Enum):
    """Collection accrual periodicity;

    https://www.dublincore.org/specifications/dublin-core/collection-description/accrual-periodicity/

    """

    ANNUAL = "Annual"
    BIENNIAL = "Biennial"
    BIMONTHLY = "Bimonthly"
    BIWEEKLY = "Biweekly"
    CONTINUOUS = "Continuous"
    DAILY = "Daily"
    IRREGULAR = "Irregular"
    MONTHLY = "Monthly"
    QUARTERLY = "Quarterly"
    SEMIANNUAL = "Semiannual"
    SEMIMONTHLY = "Semimonthly"
    TRIENNIAL = "Triennial"
    WEEKLY = "Weekly"


# ******************************************************************************************************************* #


class AccrualPolicy(str, Enum):
    """Collection accrual policy;

    https://www.dublincore.org/specifications/dublin-core/collection-description/accrual-policy/

    """

    CLOSED = "Closed"
    PASSIVE = "Passive"
    ACTIVE = "Active"
    PARTIAL = "Partial"
