from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
environment_setup = Transition(label='Environment Setup')
pest_scan = Transition(label='Pest Scan')
light_control = Transition(label='Light Control')
growth_monitor = Transition(label='Growth Monitor')
water_cycle = Transition(label='Water Cycle')
air_quality = Transition(label='Air Quality')
robotic_harvest = Transition(label='Robotic Harvest')
quality_check = Transition(label='Quality Check')
data_logging = Transition(label='Data Logging')
packaging = Transition(label='Packaging')
waste_sort = Transition(label='Waste Sort')
energy_audit = Transition(label='Energy Audit')
retail_sync = Transition(label='Retail Sync')

seed_selection_to_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])
nutrient_mix_to_environment_setup = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, environment_setup])
environment_setup_to_pest_scan = OperatorPOWL(operator=Operator.XOR, children=[environment_setup, pest_scan])
pest_scan_to_light_control = OperatorPOWL(operator=Operator.XOR, children=[pest_scan, light_control])
light_control_to_growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[light_control, growth_monitor])
growth_monitor_to_water_cycle = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, water_cycle])
water_cycle_to_air_quality = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, air_quality])
air_quality_to_robotic_harvest = OperatorPOWL(operator=Operator.XOR, children=[air_quality, robotic_harvest])
robotic_harvest_to_quality_check = OperatorPOWL(operator=Operator.XOR, children=[robotic_harvest, quality_check])
quality_check_to_data_logging = OperatorPOWL(operator=Operator.XOR, children=[quality_check, data_logging])
data_logging_to_packaging = OperatorPOWL(operator=Operator.XOR, children=[data_logging, packaging])
packaging_to_waste_sort = OperatorPOWL(operator=Operator.XOR, children=[packaging, waste_sort])
waste_sort_to_energy_audit = OperatorPOWL(operator=Operator.XOR, children=[waste_sort, energy_audit])
energy_audit_to_retail_sync = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, retail_sync])

root = StrictPartialOrder(nodes=[
    seed_selection_to_nutrient_mix,
    nutrient_mix_to_environment_setup,
    environment_setup_to_pest_scan,
    pest_scan_to_light_control,
    light_control_to_growth_monitor,
    growth_monitor_to_water_cycle,
    water_cycle_to_air_quality,
    air_quality_to_robotic_harvest,
    robotic_harvest_to_quality_check,
    quality_check_to_data_logging,
    data_logging_to_packaging,
    packaging_to_waste_sort,
    waste_sort_to_energy_audit,
    energy_audit_to_retail_sync
])

root.order.add_edge(seed_selection_to_nutrient_mix, nutrient_mix_to_environment_setup)
root.order.add_edge(nutrient_mix_to_environment_setup, environment_setup_to_pest_scan)
root.order.add_edge(environment_setup_to_pest_scan, pest_scan_to_light_control)
root.order.add_edge(pest_scan_to_light_control, light_control_to_growth_monitor)
root.order.add_edge(light_control_to_growth_monitor, growth_monitor_to_water_cycle)
root.order.add_edge(growth_monitor_to_water_cycle, water_cycle_to_air_quality)
root.order.add_edge(water_cycle_to_air_quality, air_quality_to_robotic_harvest)
root.order.add_edge(air_quality_to_robotic_harvest, robotic_harvest_to_quality_check)
root.order.add_edge(robotic_harvest_to_quality_check, quality_check_to_data_logging)
root.order.add_edge(quality_check_to_data_logging, data_logging_to_packaging)
root.order.add_edge(data_logging_to_packaging, packaging_to_waste_sort)
root.order.add_edge(packaging_to_waste_sort, waste_sort_to_energy_audit)
root.order.add_edge(waste_sort_to_energy_audit, energy_audit_to_retail_sync)