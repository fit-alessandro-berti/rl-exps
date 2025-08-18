import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
Component_Sourcing = Transition(label='Component Sourcing')
Frame_Assembly = Transition(label='Frame Assembly')
Sensor_Mounting = Transition(label='Sensor Mounting')
Wiring_Harness = Transition(label='Wiring Harness')
Circuit_Testing = Transition(label='Circuit Testing')
Firmware_Loading = Transition(label='Firmware Loading')
Initial_Calibration = Transition(label='Initial Calibration')
Software_Integration = Transition(label='Software Integration')
Flight_Testing = Transition(label='Flight Testing')
Data_Logging = Transition(label='Data Logging')
Performance_Tuning = Transition(label='Performance Tuning')
Packaging_Prep = Transition(label='Packaging Prep')
Custom_Labeling = Transition(label='Custom Labeling')
Documentation_Print = Transition(label='Documentation Print')
Quality_Review = Transition(label='Quality Review')
Client_Training = Transition(label='Client Training')
Remote_Monitoring = Transition(label='Remote Monitoring')
Firmware_Update = Transition(label='Firmware Update')

# Define the process as a StrictPartialOrder with the defined activities
root = StrictPartialOrder(nodes=[
    Component_Sourcing,
    Frame_Assembly,
    Sensor_Mounting,
    Wiring_Harness,
    Circuit_Testing,
    Firmware_Loading,
    Initial_Calibration,
    Software_Integration,
    Flight_Testing,
    Data_Logging,
    Performance_Tuning,
    Packaging_Prep,
    Custom_Labeling,
    Documentation_Print,
    Quality_Review,
    Client_Training,
    Remote_Monitoring,
    Firmware_Update
])

# Define the dependencies between activities
root.order.add_edge(Component_Sourcing, Frame_Assembly)
root.order.add_edge(Frame_Assembly, Sensor_Mounting)
root.order.add_edge(Sensor_Mounting, Wiring_Harness)
root.order.add_edge(Wiring_Harness, Circuit_Testing)
root.order.add_edge(Circuit_Testing, Firmware_Loading)
root.order.add_edge(Firmware_Loading, Initial_Calibration)
root.order.add_edge(Initial_Calibration, Software_Integration)
root.order.add_edge(Software_Integration, Flight_Testing)
root.order.add_edge(Flight_Testing, Data_Logging)
root.order.add_edge(Data_Logging, Performance_Tuning)
root.order.add_edge(Performance_Tuning, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Custom_Labeling)
root.order.add_edge(Custom_Labeling, Documentation_Print)
root.order.add_edge(Documentation_Print, Quality_Review)
root.order.add_edge(Quality_Review, Client_Training)
root.order.add_edge(Client_Training, Remote_Monitoring)
root.order.add_edge(Remote_Monitoring, Firmware_Update)

print(root)