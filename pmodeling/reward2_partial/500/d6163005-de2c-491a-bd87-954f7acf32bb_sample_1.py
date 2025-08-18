import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
Requirement_Analysis = Transition(label='Requirement Analysis')
Component_Sourcing = Transition(label='Component Sourcing')
Quality_Check = Transition(label='Quality Check')
Frame_Assembly = Transition(label='Frame Assembly')
Motor_Installation = Transition(label='Motor Installation')
Sensor_Setup = Transition(label='Sensor Setup')
Control_Unit = Transition(label='Control Unit')
Firmware_Upload = Transition(label='Firmware Upload')
System_Calibration = Transition(label='System Calibration')
Flight_Testing = Transition(label='Flight Testing')
Error_Correction = Transition(label='Error Correction')
Cosmetic_Finish = Transition(label='Cosmetic Finish')
Packaging_Prep = Transition(label='Packaging Prep')
User_Manual = Transition(label='User Manual')
Client_Training = Transition(label='Client Training')
Support_Scheduling = Transition(label='Support Scheduling')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Requirement_Analysis,
    Component_Sourcing,
    Quality_Check,
    Frame_Assembly,
    Motor_Installation,
    Sensor_Setup,
    Control_Unit,
    Firmware_Upload,
    System_Calibration,
    Flight_Testing,
    Error_Correction,
    Cosmetic_Finish,
    Packaging_Prep,
    User_Manual,
    Client_Training,
    Support_Scheduling
])

# Define the partial order dependencies
root.order.add_edge(Requirement_Analysis, Component_Sourcing)
root.order.add_edge(Component_Sourcing, Quality_Check)
root.order.add_edge(Quality_Check, Frame_Assembly)
root.order.add_edge(Frame_Assembly, Motor_Installation)
root.order.add_edge(Motor_Installation, Sensor_Setup)
root.order.add_edge(Sensor_Setup, Control_Unit)
root.order.add_edge(Control_Unit, Firmware_Upload)
root.order.add_edge(Firmware_Upload, System_Calibration)
root.order.add_edge(System_Calibration, Flight_Testing)
root.order.add_edge(Flight_Testing, Error_Correction)
root.order.add_edge(Error_Correction, Cosmetic_Finish)
root.order.add_edge(Cosmetic_Finish, Packaging_Prep)
root.order.add_edge(Packaging_Prep, User_Manual)
root.order.add_edge(User_Manual, Client_Training)
root.order.add_edge(Client_Training, Support_Scheduling)