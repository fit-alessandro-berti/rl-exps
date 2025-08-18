import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the activities
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

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[bed_construction, seed_planting, water_schedule, growth_monitor])
xor = OperatorPOWL(operator=Operator.XOR, children=[permit_obtain, stakeholder_meet])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, energy_setup])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[irrigation_plan, waste_recycle])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[crop_select, climate_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[load_test, soil_sample])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, yield_report])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)

# Print the root POWL model
print(root)