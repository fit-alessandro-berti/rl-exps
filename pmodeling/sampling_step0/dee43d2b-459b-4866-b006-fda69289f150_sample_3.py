from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for pest detection and data analysis
xor = OperatorPOWL(operator=Operator.XOR, children=[pest_detection, data_analysis])

# Define exclusive choice for nutrient mix and planting setup
xor2 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, planting_setup])

# Define loop for climate control, light adjustment, and water cycling
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, light_adjustment, water_cycling])

# Define exclusive choice for harvest planning and distribution plan
xor3 = OperatorPOWL(operator=Operator.XOR, children=[harvest_planning, distribution_plan])

# Define loop for data analysis and yield sorting
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, yield_sorting])

# Define loop for regulation check and waste recycling
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check, waste_recycling])

# Define exclusive choice for system maintenance and system maintenance
xor4 = OperatorPOWL(operator=Operator.XOR, children=[system_maintenance, system_maintenance])

# Define root POWL model
root = StrictPartialOrder(nodes=[xor, xor2, loop, xor3, loop2, loop3, xor4])

# Add dependencies to root POWL model
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, loop)
root.order.add_edge(loop, xor3)
root.order.add_edge(xor3, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor4)

print(root)