import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define the loop nodes
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, water_testing, nutrient_mix])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, planting_phase, growth_monitor])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, harvest_plan, yield_audit])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, market_delivery, waste_recycling])

# Define the partial order
root = StrictPartialOrder(nodes=[site_analysis, design_layout, module_assembly, climate_loop, sensor_loop, pest_loop, packaging_loop])
root.order.add_edge(site_analysis, design_layout)
root.order.add_edge(design_layout, module_assembly)
root.order.add_edge(module_assembly, climate_loop)
root.order.add_edge(climate_loop, sensor_loop)
root.order.add_edge(sensor_loop, pest_loop)
root.order.add_edge(pest_loop, packaging_loop)