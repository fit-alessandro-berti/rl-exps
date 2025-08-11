import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Component_Sourcing = Transition(label='Component Sourcing')
Sensor_Calibrate = Transition(label='Sensor Calibrate')
Motor_Assembly = Transition(label='Motor Assembly')
Frame_Build = Transition(label='Frame Build')
Software_Install = Transition(label='Software Install')
Algorithm_Tune = Transition(label='Algorithm Tune')
Battery_Integrate = Transition(label='Battery Integrate')
Signal_Test = Transition(label='Signal Test')
Durability_Check = Transition(label='Durability Check')
Flight_Simulate = Transition(label='Flight Simulate')
Quality_Inspect = Transition(label='Quality Inspect')
Compliance_Review = Transition(label='Compliance Review')
Packaging_Prep = Transition(label='Packaging Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Client_Feedback = Transition(label='Client Feedback')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Component_Sourcing, Sensor_Calibrate, Motor_Assembly, Frame_Build, Software_Install, Algorithm_Tune, Battery_Integrate, Signal_Test, Durability_Check, Flight_Simulate])
xor = OperatorPOWL(operator=Operator.XOR, children=[Quality_Inspect, Compliance_Review, Packaging_Prep, Logistics_Plan, Client_Feedback])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)