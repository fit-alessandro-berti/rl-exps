from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order with dependencies
root = StrictPartialOrder(nodes=[
    Component_Sourcing,
    Sensor_Calibrate,
    Motor_Assembly,
    Frame_Build,
    Software_Install,
    Algorithm_Tune,
    Battery_Integrate,
    Signal_Test,
    Durability_Check,
    Flight_Simulate,
    Quality_Inspect,
    Compliance_Review,
    Packaging_Prep,
    Logistics_Plan,
    Client_Feedback
])

# Define the order between transitions
root.order.add_edge(Component_Sourcing, Sensor_Calibrate)
root.order.add_edge(Sensor_Calibrate, Motor_Assembly)
root.order.add_edge(Motor_Assembly, Frame_Build)
root.order.add_edge(Frame_Build, Software_Install)
root.order.add_edge(Software_Install, Algorithm_Tune)
root.order.add_edge(Algorithm_Tune, Battery_Integrate)
root.order.add_edge(Battery_Integrate, Signal_Test)
root.order.add_edge(Signal_Test, Durability_Check)
root.order.add_edge(Durability_Check, Flight_Simulate)
root.order.add_edge(Flight_Simulate, Quality_Inspect)
root.order.add_edge(Quality_Inspect, Compliance_Review)
root.order.add_edge(Compliance_Review, Packaging_Prep)
root.order.add_edge(Packaging_Prep, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Client_Feedback)