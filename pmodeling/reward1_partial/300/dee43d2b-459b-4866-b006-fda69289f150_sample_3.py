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

climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control])
water_cycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_cycling])
pest_detection_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_detection])
light_adjustment_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_adjustment])
data_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis])
harvest_planning_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_planning])
yield_sorting_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_sorting])
packaging_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep])
distribution_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[distribution_plan])
regulation_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check])
waste_recycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycling])
system_maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_maintenance])

xor = OperatorPOWL(operator=Operator.XOR, children=[climate_control_loop, water_cycling_loop, pest_detection_loop, light_adjustment_loop, data_analysis_loop, harvest_planning_loop, yield_sorting_loop, packaging_prep_loop, distribution_plan_loop, regulation_check_loop, waste_recycling_loop, system_maintenance_loop])

root = StrictPartialOrder(nodes=[seed_selection, nutrient_mix, planting_setup, xor])
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_setup)
root.order.add_edge(planting_setup, xor)

print(root)