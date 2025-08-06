import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

component_sourcing = Transition(label='Component Sourcing')
sensor_calibrate = Transition(label='Sensor Calibrate')
motor_assembly = Transition(label='Motor Assembly')
frame_build = Transition(label='Frame Build')
software_install = Transition(label='Software Install')
algorithm_tune = Transition(label='Algorithm Tune')
battery_integrate = Transition(label='Battery Integrate')
signal_test = Transition(label='Signal Test')
durability_check = Transition(label='Durability Check')
flight_simulate = Transition(label='Flight Simulate')
quality_inspect = Transition(label='Quality Inspect')
compliance_review = Transition(label='Compliance Review')
packaging_prep = Transition(label='Packaging Prep')
logistics_plan = Transition(label='Logistics Plan')
client_feedback = Transition(label='Client Feedback')

skip = SilentTransition()

# Define the loop for the assembly process
assembly_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    component_sourcing, sensor_calibrate, motor_assembly, frame_build, software_install,
    algorithm_tune, battery_integrate, signal_test, durability_check, flight_simulate
])

# Define the choice for quality assurance
quality_assurance_choice = OperatorPOWL(operator=Operator.XOR, children=[
    quality_inspect, skip
])

# Define the loop for the integration process
integration_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    algorithm_tune, software_install, battery_integrate, signal_test, durability_check
])

# Define the loop for the simulation process
simulation_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    flight_simulate, quality_inspect
])

# Define the loop for the compliance review process
compliance_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    compliance_review, skip
])

# Define the loop for the logistics planning process
logistics_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    logistics_plan, skip
])

# Define the choice for the packaging process
packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[
    packaging_prep, skip
])

# Define the choice for the client feedback process
client_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[
    client_feedback, skip
])

# Define the root process
root = StrictPartialOrder(nodes=[
    assembly_loop, integration_loop, simulation_loop, quality_assurance_choice,
    compliance_review_loop, logistics_plan_loop, packaging_choice, client_feedback_choice
])

# Define the dependencies between the nodes
root.order.add_edge(assembly_loop, integration_loop)
root.order.add_edge(integration_loop, simulation_loop)
root.order.add_edge(simulation_loop, quality_assurance_choice)
root.order.add_edge(quality_assurance_choice, compliance_review_loop)
root.order.add_edge(compliance_review_loop, logistics_plan_loop)
root.order.add_edge(logistics_plan_loop, packaging_choice)
root.order.add_edge(packaging_choice, client_feedback_choice)

root.order.add_edge(assembly_loop, simulation_loop)
root.order.add_edge(integration_loop, quality_assurance_choice)
root.order.add_edge(simulation_loop, compliance_review_loop)
root.order.add_edge(quality_assurance_choice, logistics_plan_loop)
root.order.add_edge(compliance_review_loop, packaging_choice)
root.order.add_edge(logistics_plan_loop, client_feedback_choice)

root.order.add_edge(assembly_loop, compliance_review_loop)
root.order.add_edge(integration_loop, logistics_plan_loop)
root.order.add_edge(simulation_loop, packaging_choice)
root.order.add_edge(quality_assurance_choice, client_feedback_choice)
root.order.add_edge(compliance_review_loop, simulation_loop)
root.order.add_edge(logistics_plan_loop, quality_assurance_choice)
root.order.add_edge(packaging_choice, compliance_review_loop)
root.order.add_edge(client_feedback_choice, integration_loop)

root.order.add_edge(assembly_loop, packaging_choice)
root.order.add_edge(integration_loop, simulation_loop)
root.order.add_edge(simulation_loop, compliance_review_loop)
root.order.add_edge(quality_assurance_choice, logistics_plan_loop)
root.order.add_edge(compliance_review_loop, client_feedback_choice)
root.order.add_edge(logistics_plan_loop, assembly_loop)
root.order.add_edge(packaging_choice, integration_loop)
root.order.add_edge(client_feedback_choice, simulation_loop)

root.order.add_edge(assembly_loop, client_feedback_choice)
root.order.add_edge(integration_loop, compliance_review_loop)
root.order.add_edge(simulation_loop, logistics_plan_loop)
root.order.add_edge(quality_assurance_choice, packaging_choice)
root.order.add_edge(compliance_review_loop, assembly_loop)
root.order.add_edge(logistics_plan_loop, integration_loop)
root.order.add_edge(packaging_choice, simulation_loop)
root.order.add_edge(client_feedback_choice, quality_assurance_choice)

print(root)