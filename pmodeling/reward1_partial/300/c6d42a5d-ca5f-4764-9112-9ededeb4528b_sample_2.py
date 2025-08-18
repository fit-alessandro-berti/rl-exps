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

loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, load_test, soil_sample, crop_select, irrigation_plan, permit_apply, material_order, bed_install, pest_control, solar_setup, staff_train, market_outreach, system_setup, supplier_contact, health_monitor])

root = StrictPartialOrder(nodes=[loop, skip])
root.order.add_edge(loop, skip)

print(root)