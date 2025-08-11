import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, load_test])
xor = OperatorPOWL(operator=Operator.XOR, children=[soil_sample, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[crop_select, irrigation_plan])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[permit_apply, material_order])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[bed_install, pest_control])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[solar_setup, skip])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[staff_train, market_outreach])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[system_setup, supplier_contact])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[health_monitor, skip])

root = StrictPartialOrder(nodes=[loop, xor, loop2, xor2, loop3, xor3, loop4, xor4, loop5])
root.order.add_edge(loop, xor)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor3)
root.order.add_edge(loop4, xor4)
root.order.add_edge(loop5, xor4)