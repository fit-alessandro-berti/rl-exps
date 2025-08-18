from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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
root = StrictPartialOrder(nodes=[site_analysis, design_layout, module_assembly, climate_setup, sensor_install, water_testing, nutrient_mix, seed_selection, planting_phase, growth_monitor, pest_control, harvest_plan, yield_audit, packaging_prep, market_delivery, waste_recycling])

# Define the order dependencies
root.order.add_edge(site_analysis, design_layout)
root.order.add_edge(design_layout, module_assembly)
root.order.add_edge(module_assembly, climate_setup)
root.order.add_edge(climate_setup, sensor_install)
root.order.add_edge(sensor_install, water_testing)
root.order.add_edge(water_testing, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, planting_phase)
root.order.add_edge(planting_phase, growth_monitor)
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(pest_control, harvest_plan)
root.order.add_edge(harvest_plan, yield_audit)
root.order.add_edge(yield_audit, packaging_prep)
root.order.add_edge(packaging_prep, market_delivery)
root.order.add_edge(market_delivery, waste_recycling)

# Print the root POWL model
print(root)