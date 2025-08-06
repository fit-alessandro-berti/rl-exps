import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loops
load_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[load_test, soil_sample])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, soil_sample])

# Define choices
choice_1 = OperatorPOWL(operator=Operator.XOR, children=[permit_apply, material_order])
choice_2 = OperatorPOWL(operator=Operator.XOR, children=[system_setup, supplier_contact])

# Define root
root = StrictPartialOrder(nodes=[site_survey, load_test_loop, soil_sample, crop_select, irrigation_plan, choice_1, material_order, bed_install, pest_control_loop, pest_control, solar_setup, staff_train, market_outreach, choice_2, supplier_contact, health_monitor])
root.order.add_edge(load_test_loop, soil_sample)
root.order.add_edge(pest_control_loop, soil_sample)
root.order.add_edge(choice_1, material_order)
root.order.add_edge(choice_2, supplier_contact)
root.order.add_edge(system_setup, health_monitor)
root.order.add_edge(pest_control, system_setup)
root.order.add_edge(solar_setup, pest_control)
root.order.add_edge(bed_install, pest_control)
root.order.add_edge(supplier_contact, system_setup)
root.order.add_edge(staff_train, market_outreach)
root.order.add_edge(market_outreach, system_setup)
root.order.add_edge(system_setup, health_monitor)

print(root)