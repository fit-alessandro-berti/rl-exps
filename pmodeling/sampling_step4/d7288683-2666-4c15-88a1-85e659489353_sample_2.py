import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Component_Sourcing = Transition(label='Component Sourcing')
Frame_Assembly = Transition(label='Frame Assembly')
Motor_Installation = Transition(label='Motor Installation')
Sensor_Mounting = Transition(label='Sensor Mounting')
Wiring_Setup = Transition(label='Wiring Setup')
Firmware_Upload = Transition(label='Firmware Upload')
AI_Module = Transition(label='AI Module')
Calibration_Phase = Transition(label='Calibration Phase')
Stress_Testing = Transition(label='Stress Testing')
Flight_Simulation = Transition(label='Flight Simulation')
Pattern_Adjustment = Transition(label='Pattern Adjustment')
Quality_Inspect = Transition(label='Quality Inspect')
Compliance_Check = Transition(label='Compliance Check')
Packaging_Final = Transition(label='Packaging Final')
Delivery_Setup = Transition(label='Delivery Setup')

# Define the workflow model
root = StrictPartialOrder(nodes=[Component_Sourcing, Frame_Assembly, Motor_Installation, Sensor_Mounting, Wiring_Setup, Firmware_Upload, AI_Module, Calibration_Phase, Stress_Testing, Flight_Simulation, Pattern_Adjustment, Quality_Inspect, Compliance_Check, Packaging_Final, Delivery_Setup])

# Add dependencies between activities
root.order.add_edge(Component_Sourcing, Frame_Assembly)
root.order.add_edge(Frame_Assembly, Motor_Installation)
root.order.add_edge(Motor_Installation, Sensor_Mounting)
root.order.add_edge(Sensor_Mounting, Wiring_Setup)
root.order.add_edge(Wiring_Setup, Firmware_Upload)
root.order.add_edge(Firmware_Upload, AI_Module)
root.order.add_edge(AI_Module, Calibration_Phase)
root.order.add_edge(Calibration_Phase, Stress_Testing)
root.order.add_edge(Stress_Testing, Flight_Simulation)
root.order.add_edge(Flight_Simulation, Pattern_Adjustment)
root.order.add_edge(Pattern_Adjustment, Quality_Inspect)
root.order.add_edge(Quality_Inspect, Compliance_Check)
root.order.add_edge(Compliance_Check, Packaging_Final)
root.order.add_edge(Packaging_Final, Delivery_Setup)

print(root)