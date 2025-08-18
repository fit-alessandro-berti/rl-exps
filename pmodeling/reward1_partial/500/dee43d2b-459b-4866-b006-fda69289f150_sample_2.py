import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control, water_cycling, growth_monitoring, pest_detection, light_adjustment, data_analysis])
harvest_planning_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_planning, crop_harvest, yield_sorting, packaging_prep, distribution_plan])
regulation_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check, waste_recycling, system_maintenance])

root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, planting_setup, climate_control_loop, harvest_planning_loop, regulation_check_loop])
root.order.add_edge(climate_control_loop, harvest_planning_loop)
root.order.add_edge(harvest_planning_loop, regulation_check_loop)