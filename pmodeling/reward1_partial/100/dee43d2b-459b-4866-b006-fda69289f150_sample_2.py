import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the control flow operators
xor_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix, planting_setup])
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_control, water_cycling, growth_monitoring])
xor_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[pest_detection, light_adjustment, data_analysis])
xor_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[harvest_planning, crop_harvest, yield_sorting])
xor_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, distribution_plan, regulation_check])
xor_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintenance])

# Define the partial order
root = StrictPartialOrder(nodes=[xor_choice, exclusive_choice, xor_choice_2, xor_choice_3, xor_choice_4, xor_choice_5])
root.order.add_edge(xor_choice, exclusive_choice)
root.order.add_edge(exclusive_choice, xor_choice_2)
root.order.add_edge(xor_choice_2, xor_choice_3)
root.order.add_edge(xor_choice_3, xor_choice_4)
root.order.add_edge(xor_choice_4, xor_choice_5)