import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the loop for environmental adjustments and pest detection
loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, water_cycling, growth_monitoring, pest_detection, light_adjustment])

# Define the xor for data analysis and harvest planning
xor = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, harvest_planning])

# Define the xor for harvest planning and regulation check
xor2 = OperatorPOWL(operator=Operator.XOR, children=[harvest_planning, regulation_check])

# Define the xor for regulation check and waste recycling
xor3 = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, waste_recycling])

# Define the xor for waste recycling and system maintenance
xor4 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintenance])

# Define the xor for system maintenance and distribution plan
xor5 = OperatorPOWL(operator=Operator.XOR, children=[system_maintenance, distribution_plan])

# Define the xor for distribution plan and packaging prep
xor6 = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, packaging_prep])

# Define the xor for packaging prep and yield sorting
xor7 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, yield_sorting])

# Define the xor for yield sorting and crop harvest
xor8 = OperatorPOWL(operator=Operator.XOR, children=[yield_sorting, crop_harvest])

# Define the xor for crop harvest and nutrient mix
xor9 = OperatorPOWL(operator=Operator.XOR, children=[crop_harvest, nutrient_mix])

# Define the xor for nutrient mix and planting setup
xor10 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, planting_setup])

# Define the xor for planting setup and seed selection
xor11 = OperatorPOWL(operator=Operator.XOR, children=[planting_setup, seed_selection])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor11, xor10, xor9, xor8, xor7, xor6, xor5, xor4, xor3, xor2, loop])

# Define the edges between the nodes
root.order.add_edge(xor11, xor10)
root.order.add_edge(xor10, xor9)
root.order.add_edge(xor9, xor8)
root.order.add_edge(xor8, xor7)
root.order.add_edge(xor7, xor6)
root.order.add_edge(xor6, xor5)
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, loop)
root.order.add_edge(loop, xor11)

# Print the root POWL model
print(root)