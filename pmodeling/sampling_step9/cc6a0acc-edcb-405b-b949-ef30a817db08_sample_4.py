import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
water_check = Transition(label='Water Check')
design_plan = Transition(label='Design Plan')
bed_setup = Transition(label='Bed Setup')
irrigation_install = Transition(label='Irrigation Install')
climate_setup = Transition(label='Climate Setup')
seed_selection = Transition(label='Seed Selection')
planting_phase = Transition(label='Planting Phase')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
harvest_prep = Transition(label='Harvest Prep')
community_meet = Transition(label='Community Meet')
waste_manage = Transition(label='Waste Manage')
yield_report = Transition(label='Yield Report')
skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, skip])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[planting_phase, pest_control, growth_monitor])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[community_meet, waste_manage])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_prep, yield_report])

# Define root
root = StrictPartialOrder(nodes=[site_survey, load_test, soil_sample, water_check, design_plan, bed_setup, irrigation_install, climate_setup, xor, loop1, loop2, loop3])
root.order.add_edge(site_survey, load_test)
root.order.add_edge(site_survey, soil_sample)
root.order.add_edge(site_survey, water_check)
root.order.add_edge(load_test, design_plan)
root.order.add_edge(soil_sample, design_plan)
root.order.add_edge(water_check, design_plan)
root.order.add_edge(design_plan, bed_setup)
root.order.add_edge(bed_setup, irrigation_install)
root.order.add_edge(irrigation_install, climate_setup)
root.order.add_edge(climate_setup, xor)
root.order.add_edge(xor, loop1)
root.order.add_edge(xor, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, yield_report)