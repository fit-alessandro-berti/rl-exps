import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
culture_addition = Transition(label='Culture Addition')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
cheese_molding = Transition(label='Cheese Molding')
controlled_aging = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')
health_certify = Transition(label='Health Certify')
custom_labeling = Transition(label='Custom Labeling')
cold_packaging = Transition(label='Cold Packaging')
logistics_setup = Transition(label='Logistics Setup')
export_docs = Transition(label='Export Docs')
customs_clearance = Transition(label='Customs Clearance')
shipment_track = Transition(label='Shipment Track')
client_feedback = Transition(label='Client Feedback')

# Define the loop for cheese production
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    milk_sourcing, quality_testing, milk_pasteurize, culture_addition, curd_cutting,
    whey_drain, cheese_molding, controlled_aging, sensory_check, health_certify
])

# Define the XOR for logistics and export
xor_logistics_export = OperatorPOWL(operator=Operator.XOR, children=[
    custom_labeling, cold_packaging, logistics_setup, export_docs, customs_clearance, shipment_track
])

# Define the XOR for feedback and other activities
xor_feedback_other = OperatorPOWL(operator=Operator.XOR, children=[
    client_feedback
])

# Define the root POWL model
root = StrictPartialOrder(nodes=[production_loop, xor_logistics_export, xor_feedback_other])
root.order.add_edge(production_loop, xor_logistics_export)
root.order.add_edge(production_loop, xor_feedback_other)

print(root)