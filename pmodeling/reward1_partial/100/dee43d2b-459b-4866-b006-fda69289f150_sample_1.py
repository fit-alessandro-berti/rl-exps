from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
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
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_detection, light_adjustment])
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, water_cycling, growth_monitoring, data_analysis, harvest_planning, crop_harvest, yield_sorting, packaging_prep, distribution_plan, regulation_check, waste_recycling, system_maintenance])
xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, waste_recycling, system_maintenance])

# Create the root POWL model
root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, planting_setup, exclusive_choice, loop, xor])
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_setup)
root.order.add_edge(planting_setup, exclusive_choice)
root.order.add_edge(exclusive_choice, loop)
root.order.add_edge(loop, xor)

# Print the final POWL model
print(root)