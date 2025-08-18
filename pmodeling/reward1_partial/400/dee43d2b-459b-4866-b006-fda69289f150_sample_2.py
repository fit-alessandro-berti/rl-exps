import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as POWL transitions
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
planting_setup = Transition(label='Planting Setup')
climate_control = Transition(label='Climate Control')
water_cycling = Transition(label='Water Cycling')
growth_monitoring = Transition(label='Growth Monitoring')
pest_detection = Transition(label='Pest Detection')
light_adjustment = Transition(label='Light Adjustment')
data_analysis = Transition(label='Data Analysis')
harvest_planning = Transition(label='Harvest Planning')
crop_harvest = Transition(label='Crop Harvest')
yield_sorting = Transition(label='Yield Sorting')
packaging_prep = Transition(label='Packaging Prep')
distribution_plan = Transition(label='Distribution Plan')
regulation_check = Transition(label='Regulation Check')
waste_recycling = Transition(label='Waste Recycling')
system_maintenance = Transition(label='System Maintenance')

# Create the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[climate_control, data_analysis])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[water_cycling, light_adjustment])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[pest_detection, growth_monitoring])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[system_maintenance, waste_recycling])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, distribution_plan])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[yield_sorting, packaging_prep])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[harvest_planning, crop_harvest])

root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, planting_setup, xor1, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_setup)
root.order.add_edge(planting_setup, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor4, xor6)
root.order.add_edge(xor5, xor7)
root.order.add_edge(xor6, harvest_planning)
root.order.add_edge(xor7, crop_harvest)

print(root)