import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define sub-processes
climate_control_sub = StrictPartialOrder(nodes=[climate_control, skip])
water_cycling_sub = StrictPartialOrder(nodes=[water_cycling, skip])
light_adjustment_sub = StrictPartialOrder(nodes=[light_adjustment, skip])
pest_detection_sub = StrictPartialOrder(nodes=[pest_detection, skip])
regulation_check_sub = StrictPartialOrder(nodes=[regulation_check, skip])
waste_recycling_sub = StrictPartialOrder(nodes=[waste_recycling, skip])
system_maintenance_sub = StrictPartialOrder(nodes=[system_maintenance, skip])

# Define loops
climate_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_control_sub])
water_cycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_cycling_sub])
light_adjustment_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_adjustment_sub])
pest_detection_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_detection_sub])
regulation_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check_sub])
waste_recycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycling_sub])
system_maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_maintenance_sub])

# Define XOR nodes
climate_control_xor = OperatorPOWL(operator=Operator.XOR, children=[climate_control_loop, skip])
water_cycling_xor = OperatorPOWL(operator=Operator.XOR, children=[water_cycling_loop, skip])
light_adjustment_xor = OperatorPOWL(operator=Operator.XOR, children=[light_adjustment_loop, skip])
pest_detection_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_detection_loop, skip])
regulation_check_xor = OperatorPOWL(operator=Operator.XOR, children=[regulation_check_loop, skip])
waste_recycling_xor = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling_loop, skip])
system_maintenance_xor = OperatorPOWL(operator=Operator.XOR, children=[system_maintenance_loop, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    seed_selection,
    nutrient_mix,
    planting_setup,
    climate_control_xor,
    water_cycling_xor,
    light_adjustment_xor,
    data_analysis,
    harvest_planning,
    crop_harvest,
    yield_sorting,
    packaging_prep,
    distribution_plan,
    regulation_check_xor,
    waste_recycling_xor,
    system_maintenance_xor
])

# Define dependencies
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_setup)
root.order.add_edge(planting_setup, climate_control_xor)
root.order.add_edge(climate_control_xor, data_analysis)
root.order.add_edge(data_analysis, harvest_planning)
root.order.add_edge(harvest_planning, crop_harvest)
root.order.add_edge(crop_harvest, yield_sorting)
root.order.add_edge(yield_sorting, packaging_prep)
root.order.add_edge(packaging_prep, distribution_plan)
root.order.add_edge(distribution_plan, regulation_check_xor)
root.order.add_edge(regulation_check_xor, waste_recycling_xor)
root.order.add_edge(waste_recycling_xor, system_maintenance_xor)
root.order.add_edge(system_maintenance_xor, skip)