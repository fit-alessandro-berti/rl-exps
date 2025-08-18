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

# Define partial order for site analysis and design layout
site_design_partial_order = StrictPartialOrder(nodes=[site_analysis, design_layout])
site_design_partial_order.order.add_edge(site_analysis, design_layout)

# Define partial order for module assembly and climate setup
module_climate_partial_order = StrictPartialOrder(nodes=[module_assembly, climate_setup])
module_climate_partial_order.order.add_edge(module_assembly, climate_setup)

# Define partial order for sensor install and water testing
sensor_water_partial_order = StrictPartialOrder(nodes=[sensor_install, water_testing])
sensor_water_partial_order.order.add_edge(sensor_install, water_testing)

# Define partial order for nutrient mix and seed selection
nutrient_seed_partial_order = StrictPartialOrder(nodes=[nutrient_mix, seed_selection])
nutrient_seed_partial_order.order.add_edge(nutrient_mix, seed_selection)

# Define partial order for planting phase and growth monitor
planting_growth_partial_order = StrictPartialOrder(nodes=[planting_phase, growth_monitor])
planting_growth_partial_order.order.add_edge(planting_phase, growth_monitor)

# Define partial order for pest control and harvest plan
pest_control_harvest_partial_order = StrictPartialOrder(nodes=[pest_control, harvest_plan])
pest_control_harvest_partial_order.order.add_edge(pest_control, harvest_plan)

# Define partial order for yield audit and packaging prep
yield_audit_packaging_partial_order = StrictPartialOrder(nodes=[yield_audit, packaging_prep])
yield_audit_packaging_partial_order.order.add_edge(yield_audit, packaging_prep)

# Define partial order for market delivery and waste recycling
market_delivery_waste_partial_order = StrictPartialOrder(nodes=[market_delivery, waste_recycling])
market_delivery_waste_partial_order.order.add_edge(market_delivery, waste_recycling)

# Define exclusive choice for nutrient mix and seed selection
nutrient_seed_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_selection])

# Define exclusive choice for planting phase and growth monitor
planting_growth_choice = OperatorPOWL(operator=Operator.XOR, children=[planting_phase, growth_monitor])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define loop for sensor install and water testing
sensor_water_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, water_testing])

# Define loop for pest control and harvest plan
pest_control_harvest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, harvest_plan])

# Define loop for yield audit and packaging prep
yield_audit_packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_audit, packaging_prep])

# Define loop for market delivery and waste recycling
market_delivery_waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

# Define exclusive choice for market delivery and waste recycling
market_delivery_waste_choice = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define exclusive choice for sensor install and water testing
sensor_water_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])

# Define exclusive choice for pest control and harvest plan
pest_control_harvest_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])

# Define exclusive choice for yield audit and packaging prep
yield_audit_packaging_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])

#