import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_analysis = Transition(label='Site Analysis')
design_layout = Transition(label='Design Layout')
module_assembly = Transition(label='Module Assembly')
climate_setup = Transition(label='Climate Setup')
sensor_install = Transition(label='Sensor Install')
water_testing = Transition(label='Water Testing')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
planting_phase = Transition(label='Planting Phase')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvest_plan = Transition(label='Harvest Plan')
yield_audit = Transition(label='Yield Audit')
packaging_prep = Transition(label='Packaging Prep')
market_delivery = Transition(label='Market Delivery')
waste_recycling = Transition(label='Waste Recycling')

# Define the partial order
root = StrictPartialOrder()

# Define the activities' dependencies
root.add_transition(site_analysis)
root.add_transition(design_layout)
root.add_transition(module_assembly)
root.add_transition(climate_setup)
root.add_transition(sensor_install)
root.add_transition(water_testing)
root.add_transition(nutrient_mix)
root.add_transition(seed_selection)
root.add_transition(planting_phase)
root.add_transition(growth_monitor)
root.add_transition(pest_control)
root.add_transition(harvest_plan)
root.add_transition(yield_audit)
root.add_transition(packaging_prep)
root.add_transition(market_delivery)
root.add_transition(waste_recycling)

# Define the dependencies between activities
root.add_edge(site_analysis, design_layout)
root.add_edge(design_layout, module_assembly)
root.add_edge(module_assembly, climate_setup)
root.add_edge(climate_setup, sensor_install)
root.add_edge(sensor_install, water_testing)
root.add_edge(water_testing, nutrient_mix)
root.add_edge(nutrient_mix, seed_selection)
root.add_edge(seed_selection, planting_phase)
root.add_edge(planting_phase, growth_monitor)
root.add_edge(growth_monitor, pest_control)
root.add_edge(pest_control, harvest_plan)
root.add_edge(harvest_plan, yield_audit)
root.add_edge(yield_audit, packaging_prep)
root.add_edge(packaging_prep, market_delivery)
root.add_edge(market_delivery, waste_recycling)

# Print the root
print(root)