import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
site_survey = Transition(label='Site Survey')
load_test = Transition(label='Load Test')
soil_sample = Transition(label='Soil Sample')
climate_check = Transition(label='Climate Check')
crop_select = Transition(label='Crop Select')
irrigation_plan = Transition(label='Irrigation Plan')
energy_setup = Transition(label='Energy Setup')
pest_control = Transition(label='Pest Control')
permit_obtain = Transition(label='Permit Obtain')
stakeholder_meet = Transition(label='Stakeholder Meet')
bed_construction = Transition(label='Bed Construction')
seed_planting = Transition(label='Seed Planting')
water_schedule = Transition(label='Water Schedule')
growth_monitor = Transition(label='Growth Monitor')
harvest_plan = Transition(label='Harvest Plan')
waste_recycle = Transition(label='Waste Recycle')
yield_report = Transition(label='Yield Report')

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[permit_obtain, stakeholder_meet])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[bed_construction, seed_planting])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[water_schedule, growth_monitor])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, waste_recycle])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey, load_test, soil_sample, climate_check, crop_select, irrigation_plan, energy_setup, pest_control, xor1, xor2, xor3, xor4, yield_report])
root.order.add_edge(site_survey, load_test)
root.order.add_edge(load_test, soil_sample)
root.order.add_edge(soil_sample, climate_check)
root.order.add_edge(climate_check, crop_select)
root.order.add_edge(crop_select, irrigation_plan)
root.order.add_edge(irrigation_plan, energy_setup)
root.order.add_edge(energy_setup, pest_control)
root.order.add_edge(pest_control, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, yield_report)

print(root)