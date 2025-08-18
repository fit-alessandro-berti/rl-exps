from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Quantum Init'),
    Transition(label='Data Ingest'),
    Transition(label='AI Forecast'),
    Transition(label='Inventory Sync'),
    Transition(label='Procurement Plan'),
    Transition(label='Production Align'),
    Transition(label='Distribution Map'),
    Transition(label='IoT Monitor'),
    Transition(label='Risk Assess'),
    Transition(label='Maintenance Alert'),
    Transition(label='Quantum Compute'),
    Transition(label='Feedback Loop'),
    Transition(label='Schedule Adjust'),
    Transition(label='Demand Update'),
    Transition(label='Delivery Track'),
    Transition(label='Compliance Check')
])

# Define the dependencies between activities
root.order.add_edge(Transition(label='Quantum Init'), Transition(label='Data Ingest'))
root.order.add_edge(Transition(label='Data Ingest'), Transition(label='AI Forecast'))
root.order.add_edge(Transition(label='AI Forecast'), Transition(label='Inventory Sync'))
root.order.add_edge(Transition(label='Inventory Sync'), Transition(label='Procurement Plan'))
root.order.add_edge(Transition(label='Procurement Plan'), Transition(label='Production Align'))
root.order.add_edge(Transition(label='Production Align'), Transition(label='Distribution Map'))
root.order.add_edge(Transition(label='Distribution Map'), Transition(label='IoT Monitor'))
root.order.add_edge(Transition(label='IoT Monitor'), Transition(label='Risk Assess'))
root.order.add_edge(Transition(label='Risk Assess'), Transition(label='Maintenance Alert'))
root.order.add_edge(Transition(label='Maintenance Alert'), Transition(label='Quantum Compute'))
root.order.add_edge(Transition(label='Quantum Compute'), Transition(label='Feedback Loop'))
root.order.add_edge(Transition(label='Feedback Loop'), Transition(label='Schedule Adjust'))
root.order.add_edge(Transition(label='Schedule Adjust'), Transition(label='Demand Update'))
root.order.add_edge(Transition(label='Demand Update'), Transition(label='Delivery Track'))
root.order.add_edge(Transition(label='Delivery Track'), Transition(label='Compliance Check'))

# Print the final POWL model
print(root)