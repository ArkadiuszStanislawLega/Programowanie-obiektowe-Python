from models.manual_wash_body import ManualWashBody
from models.manual_wash_wheels import ManualWashWheels
from models.mechanical_wash_body import MechanicalWashBody
from models.mechanical_wash_wheels import MechanicalWashWheels


def main():
    services_container = [ManualWashBody(), ManualWashWheels(), MechanicalWashBody(), MechanicalWashWheels()]
    for service in services_container:
        service.paid_for_service()
        service.clean()
        print(60*"=")


if '__main__' == __name__:
    main()
