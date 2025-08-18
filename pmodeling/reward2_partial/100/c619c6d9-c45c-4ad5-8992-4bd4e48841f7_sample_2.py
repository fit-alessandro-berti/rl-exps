import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) based on the provided description
Design_Consult = Transition(label='Design Consult')
Component_Sourcing = Transition(label='Component Sourcing')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Firmware_Integrate = Transition(label='Firmware Integrate')
Payload_Configure = Transition(label='Payload Configure')
Assembly_Setup = Transition(label='Assembly Setup')
Wiring_Connect = Transition(label='Wiring Connect')
Chassis_Build = Transition(label='Chassis Build')
Software_Load = Transition(label='Software Load')
Flight_Testing = Transition(label='Flight Testing')
Data_Analyze = Transition(label='Data Analyze')
Regulation_Check = Transition(label='Regulation Check')
Quality_Inspect = Transition(label='Quality Inspect')
Packaging_Prepare = Transition(label='Packaging Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Client_Review = Transition(label='Client Review')

# Create the Partial Order Workflow Language (POWL) model
root = StrictPartialOrder(nodes=[
    Design_Consult,
    Component_Sourcing,
    Sensor_Calibrate,
    Firmware_Integrate,
    Payload_Configure,
    Assembly_Setup,
    Wiring_Connect,
    Chassis_Build,
    Software_Load,
    Flight_Testing,
    Data_Analyze,
    Regulation_Check,
    Quality_Inspect,
    Packaging_Prepare,
    Logistics_Plan,
    Client_Review
])

# Define the dependencies between activities
root.order.add_edge(Design_Consult, Component_Sourcing)
root.order.add_edge(Component_Sourcing, Sensor_Calibrate)
root.order.add_edge(Sensor_Calibrate, Firmware_Integrate)
root.order.add_edge(Firmware_Integrate, Payload_Configure)
root.order.add_edge(Payload_Configure, Assembly_Setup)
root.order.add_edge(Assembly_Setup, Wiring_Connect)
root.order.add_edge(Wiring_Connect, Chassis_Build)
root.order.add_edge(Chassis_Build, Software_Load)
root.order.add_edge(Software_Load, Flight_Testing)
root.order.add_edge(Flight_Testing, Data_Analyze)
root.order.add_edge(Data_Analyze, Regulation_Check)
root.order.add_edge(Regulation_Check, Quality_Inspect)
root.order.add_edge(Quality_Inspect, Packaging_Prepare)
root.order.add_edge(Packaging_Prepare, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Client_Review)

# Print the root model for verification
print(root)