import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
iot_setup = Transition(label='IoT Setup')
crop_selection = Transition(label='Crop Selection')
hydroponic_install = Transition(label='Hydroponic Install')
water_recycling = Transition(label='Water Recycling')
energy_audit = Transition(label='Energy Audit')
plant_scheduling = Transition(label='Plant Scheduling')
yield_monitoring = Transition(label='Yield Monitoring')
regulation_review = Transition(label='Regulation Review')
staff_training = Transition(label='Staff Training')
data_integration = Transition(label='Data Integration')
supply_setup = Transition(label='Supply Setup')
quality_audit = Transition(label='Quality Audit')
logistics_plan = Transition(label='Logistics Plan')

# Create the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, data_integration])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[supply_setup, quality_audit])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, site_survey])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[structural_check, iot_setup])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, hydroponic_install])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[water_recycling, energy_audit])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[plant_scheduling, yield_monitoring])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)

# Print the POWL model
print(root)