import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
crop_select = Transition(label='Crop Select')
irrigation_plan = Transition(label='Irrigation Plan')
permit_apply = Transition(label='Permit Apply')
material_order = Transition(label='Material Order')
bed_install = Transition(label='Bed Install')
pest_control = Transition(label='Pest Control')
solar_setup = Transition(label='Solar Setup')
staff_train = Transition(label='Staff Train')
market_outreach = Transition(label='Market Outreach')
system_setup = Transition(label='System Setup')
supplier_contact = Transition(label='Supplier Contact')
health_monitor = Transition(label='Health Monitor')

# Define silent transitions for concurrency
skip = SilentTransition()

# Define exclusive choices for certain activities
xor1 = OperatorPOWL(operator=Operator.XOR, children=[permit_apply, material_order])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[bed_install, pest_control])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[solar_setup, system_setup])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[supplier_contact, market_outreach])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[health_monitor, skip])

# Define loops for repeating activities
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor])

# Define the root node with all the activities
root = StrictPartialOrder(nodes=[site_survey, load_test, soil_sample, crop_select, irrigation_plan, xor1, xor2, xor3, xor4, xor5, loop1])
root.order.add_edge(site_survey, load_test)
root.order.add_edge(site_survey, soil_sample)
root.order.add_edge(site_survey, crop_select)
root.order.add_edge(site_survey, irrigation_plan)
root.order.add_edge(load_test, xor1)
root.order.add_edge(soil_sample, xor1)
root.order.add_edge(crop_select, xor1)
root.order.add_edge(irrigation_plan, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor1, xor5)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor2, xor5)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, loop1)
root.order.add_edge(loop1, health_monitor)

# Print the root node to verify the model
print(root)