import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define the loop for planting and growth phases
planting_growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_phase, growth_monitor])

# Define the XOR for pest control and pesticide application
pest_control_xor = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])

# Define the POWL model
root = StrictPartialOrder(nodes=[site_analysis, design_layout, module_assembly, climate_setup, sensor_install, water_testing, nutrient_mix, seed_selection, planting_growth_loop, pest_control_xor, packaging_prep, market_delivery, waste_recycling])
root.order.add_edge(site_analysis, design_layout)
root.order.add_edge(design_layout, module_assembly)
root.order.add_edge(module_assembly, climate_setup)
root.order.add_edge(climate_setup, sensor_install)
root.order.add_edge(sensor_install, water_testing)
root.order.add_edge(water_testing, nutrient_mix)
root.order.add_edge(nutrient_mix, seed_selection)
root.order.add_edge(seed_selection, planting_growth_loop)
root.order.add_edge(planting_growth_loop, pest_control_xor)
root.order.add_edge(pest_control_xor, packaging_prep)
root.order.add_edge(packaging_prep, market_delivery)
root.order.add_edge(market_delivery, waste_recycling)

print(root)