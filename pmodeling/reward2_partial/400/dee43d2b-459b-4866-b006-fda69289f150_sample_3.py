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

# Define the partial order
root = StrictPartialOrder(nodes=[
    seed_selection,
    nutrient_mix,
    planting_setup,
    climate_control,
    water_cycling,
    growth_monitoring,
    pest_detection,
    light_adjustment,
    data_analysis,
    harvest_planning,
    crop_harvest,
    yield_sorting,
    packaging_prep,
    distribution_plan,
    regulation_check,
    waste_recycling,
    system_maintenance
])

# Define the dependencies between activities
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_setup)
root.order.add_edge(planting_setup, climate_control)
root.order.add_edge(climate_control, water_cycling)
root.order.add_edge(water_cycling, growth_monitoring)
root.order.add_edge(growth_monitoring, pest_detection)
root.order.add_edge(pest_detection, light_adjustment)
root.order.add_edge(light_adjustment, data_analysis)
root.order.add_edge(data_analysis, harvest_planning)
root.order.add_edge(harvest_planning, crop_harvest)
root.order.add_edge(crop_harvest, yield_sorting)
root.order.add_edge(yield_sorting, packaging_prep)
root.order.add_edge(packaging_prep, distribution_plan)
root.order.add_edge(distribution_plan, regulation_check)
root.order.add_edge(regulation_check, waste_recycling)
root.order.add_edge(waste_recycling, system_maintenance)

# Print the root
print(root)