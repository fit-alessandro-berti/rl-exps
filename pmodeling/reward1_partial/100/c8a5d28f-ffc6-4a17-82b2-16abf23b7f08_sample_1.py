import pm4py

# Define the transitions
milk_sourcing = pm4py.objects.powl.obj.Transition(label='Milk Sourcing')
quality_testing = pm4py.objects.powl.obj.Transition(label='Quality Testing')
milk_pasturize = pm4py.objects.powl.obj.Transition(label='Milk Pasteurize')
culture_addition = pm4py.objects.powl.obj.Transition(label='Culture Addition')
curd_cutting = pm4py.objects.powl.obj.Transition(label='Curd Cutting')
whey_drain = pm4py.objects.powl.obj.Transition(label='Whey Drain')
cheese_molding = pm4py.objects.powl.obj.Transition(label='Cheese Molding')
controlled_aging = pm4py.objects.powl.obj.Transition(label='Controlled Aging')
sensory_check = pm4py.objects.powl.obj.Transition(label='Sensory Check')
health_certify = pm4py.objects.powl.obj.Transition(label='Health Certify')
custom_labeling = pm4py.objects.powl.obj.Transition(label='Custom Labeling')
cold_packaging = pm4py.objects.powl.obj.Transition(label='Cold Packaging')
logistics_setup = pm4py.objects.powl.obj.Transition(label='Logistics Setup')
export_docs = pm4py.objects.powl.obj.Transition(label='Export Docs')
customs_clearance = pm4py.objects.powl.obj.Transition(label='Customs Clearance')
shipment_track = pm4py.objects.powl.obj.Transition(label='Shipment Track')
client_feedback = pm4py.objects.powl.obj.Transition(label='Client Feedback')

# Define the operators
xor1 = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[quality_testing, milk_pasturize])
xor2 = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[culture_addition, whey_drain])
xor3 = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[curd_cutting, cheese_molding])
xor4 = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[controlled_aging, sensory_check])
xor5 = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[health_certify, custom_labeling])
xor6 = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[logistics_setup, export_docs])
xor7 = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[customs_clearance, shipment_track])
xor8 = pm4py.objects.powl.obj.OperatorPOWL(operator=pm4py.objects.powl.obj.Operator.XOR, children=[client_feedback, None])  # Assuming 'None' means exit

# Define the partial order
root = pm4py.objects.powl.obj.StrictPartialOrder(nodes=[milk_sourcing, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(milk_sourcing, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

print(root)