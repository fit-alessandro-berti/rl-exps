import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define choice nodes for activities
climate_control_and_water_cycling = OperatorPOWL(operator=Operator.XOR, children=[climate_control, water_cycling])
pest_detection_and_light_adjustment = OperatorPOWL(operator=Operator.XOR, children=[pest_detection, light_adjustment])

# Define loop nodes for activities
data_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis])
yield_sorting_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_sorting])
packaging_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep])

# Define partial order for the process
root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, planting_setup, climate_control_and_water_cycling,
                                 pest_detection_and_light_adjustment, growth_monitoring, data_analysis_loop,
                                 harvest_planning, crop_harvest, yield_sorting_loop, packaging_prep_loop,
                                 distribution_plan, regulation_check, waste_recycling, system_maintenance])

# Add edges to the partial order
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(seed_selection, planting_setup)
root.order.add_edge(nutrient_mix, climate_control_and_water_cycling)
root.order.add_edge(planting_setup, climate_control_and_water_cycling)
root.order.add_edge(climate_control_and_water_cycling, growth_monitoring)
root.order.add_edge(growth_monitoring, pest_detection_and_light_adjustment)
root.order.add_edge(pest_detection_and_light_adjustment, data_analysis_loop)
root.order.add_edge(data_analysis_loop, yield_sorting_loop)
root.order.add_edge(yield_sorting_loop, packaging_prep_loop)
root.order.add_edge(packaging_prep_loop, distribution_plan)
root.order.add_edge(distribution_plan, regulation_check)
root.order.add_edge(regulation_check, waste_recycling)
root.order.add_edge(waste_recycling, system_maintenance)