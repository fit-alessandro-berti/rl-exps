import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Client_Brief = Transition(label='Client Brief')
Design_Draft = Transition(label='Design Draft')
Part_Sourcing = Transition(label='Part Sourcing')
Component_Fabric = Transition(label='Component Fabric')
Circuit_Assembly = Transition(label='Circuit Assembly')
Software_Upload = Transition(label='Software Upload')
Initial_Testing = Transition(label='Initial Testing')
Flight_Calibrate = Transition(label='Flight Calibrate')
Payload_Mount = Transition(label='Payload Mount')
Stress_Testing = Transition(label='Stress Testing')
Feedback_Loop = Transition(label='Feedback Loop')
Quality_Check = Transition(label='Quality Check')
Certification = Transition(label='Certification')
Packaging = Transition(label='Packaging')
Delivery_Plan = Transition(label='Delivery Plan')
Post_Support = Transition(label='Post Support')
skip = SilentTransition()

# Define nodes
# Initial steps
init_node = OperatorPOWL(operator=Operator.XOR, children=[Client_Brief, skip])

# Design and component fabrication
design_node = OperatorPOWL(operator=Operator.XOR, children=[Design_Draft, skip])
component_node = OperatorPOWL(operator=Operator.XOR, children=[Part_Sourcing, skip])
fabric_node = OperatorPOWL(operator=Operator.XOR, children=[Component_Fabric, skip])

# Circuit assembly and software upload
circuit_node = OperatorPOWL(operator=Operator.XOR, children=[Circuit_Assembly, skip])
software_node = OperatorPOWL(operator=Operator.XOR, children=[Software_Upload, skip])

# Testing and calibration
testing_node = OperatorPOWL(operator=Operator.XOR, children=[Initial_Testing, skip])
flight_calibrate_node = OperatorPOWL(operator=Operator.XOR, children=[Flight_Calibrate, skip])

# Payload mounting and stress testing
payload_node = OperatorPOWL(operator=Operator.XOR, children=[Payload_Mount, skip])
stress_node = OperatorPOWL(operator=Operator.XOR, children=[Stress_Testing, skip])

# Quality check and certification
quality_node = OperatorPOWL(operator=Operator.XOR, children=[Quality_Check, skip])
certification_node = OperatorPOWL(operator=Operator.XOR, children=[Certification, skip])

# Packaging and delivery plan
packaging_node = OperatorPOWL(operator=Operator.XOR, children=[Packaging, skip])
delivery_node = OperatorPOWL(operator=Operator.XOR, children=[Delivery_Plan, skip])

# Post support
post_support_node = OperatorPOWL(operator=Operator.XOR, children=[Post_Support, skip])

# Define partial order
root = StrictPartialOrder(nodes=[
    init_node, design_node, component_node, fabric_node,
    circuit_node, software_node, testing_node, flight_calibrate_node,
    payload_node, stress_node, quality_node, certification_node,
    packaging_node, delivery_node, post_support_node
])

# Define dependencies
root.order.add_edge(init_node, design_node)
root.order.add_edge(init_node, component_node)
root.order.add_edge(design_node, component_node)
root.order.add_edge(component_node, fabric_node)
root.order.add_edge(fabric_node, circuit_node)
root.order.add_edge(circuit_node, software_node)
root.order.add_edge(software_node, testing_node)
root.order.add_edge(testing_node, flight_calibrate_node)
root.order.add_edge(flight_calibrate_node, payload_node)
root.order.add_edge(payload_node, stress_node)
root.order.add_edge(stress_node, quality_node)
root.order.add_edge(quality_node, certification_node)
root.order.add_edge(certification_node, packaging_node)
root.order.add_edge(packaging_node, delivery_node)
root.order.add_edge(delivery_node, post_support_node)