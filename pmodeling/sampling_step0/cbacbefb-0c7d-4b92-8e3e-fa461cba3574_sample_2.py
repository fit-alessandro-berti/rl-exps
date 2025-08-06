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

# Define the operators
site_analysis_to_design_layout = OperatorPOWL(operator=Operator.XOR, children=[site_analysis, design_layout])
design_layout_to_module_assembly = OperatorPOWL(operator=Operator.XOR, children=[design_layout, module_assembly])
module_assembly_to_climate_setup = OperatorPOWL(operator=Operator.XOR, children=[module_assembly, climate_setup])
climate_setup_to_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, sensor_install])
sensor_install_to_water_testing = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, water_testing])
water_testing_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[water_testing, nutrient_mix])
nutrient_mix_to_seed_selection = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_selection])
seed_selection_to_planting_phase = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, planting_phase])
planting_phase_to_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[planting_phase, growth_monitor])
growth_monitor_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])
pest_control_to_harvest_plan = OperatorPOWL(operator=Operator.XOR, children=[pest_control, harvest_plan])
harvest_plan_to_yield_audit = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, yield_audit])
yield_audit_to_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[yield_audit, packaging_prep])
packaging_prep_to_market_delivery = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, market_delivery])
market_delivery_to_waste_recycling = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, waste_recycling])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[market_delivery, waste_recycling])

# Define the root
root = StrictPartialOrder(nodes=[site_analysis_to_design_layout, design_layout_to_module_assembly, module_assembly_to_climate_setup, climate_setup_to_sensor_install, sensor_install_to_water_testing, water_testing_to_nutrient_mix, nutrient_mix_to_seed_selection, seed_selection_to_planting_phase, planting_phase_to_growth_monitor, growth_monitor_to_pest_control, pest_control_to_harvest_plan, harvest_plan_to_yield_audit, yield_audit_to_packaging_prep, packaging_prep_to_market_delivery, loop])
root.order.add_edge(site_analysis_to_design_layout, design_layout_to_module_assembly)
root.order.add_edge(design_layout_to_module_assembly, module_assembly_to_climate_setup)
root.order.add_edge(module_assembly_to_climate_setup, climate_setup_to_sensor_install)
root.order.add_edge(climate_setup_to_sensor_install, sensor_install_to_water_testing)
root.order.add_edge(sensor_install_to_water_testing, water_testing_to_nutrient_mix)
root.order.add_edge(water_testing_to_nutrient_mix, nutrient_mix_to_seed_selection)
root.order.add_edge(nutrient_mix_to_seed_selection, seed_selection_to_planting_phase)
root.order.add_edge(seed_selection_to_planting_phase, planting_phase_to_growth_monitor)
root.order.add_edge(planting_phase_to_growth_monitor, growth_monitor_to_pest_control)
root.order.add_edge(growth_monitor_to_pest_control, pest_control_to_harvest_plan)
root.order.add_edge(pest_control_to_harvest_plan, harvest_plan_to_yield_audit)
root.order.add_edge(harvest_plan_to_yield_audit, yield_audit_to_packaging_prep)
root.order.add_edge(yield_audit_to_packaging_prep, packaging_prep_to_market_delivery)
root.order.add_edge(packaging_prep_to_market_delivery, loop)