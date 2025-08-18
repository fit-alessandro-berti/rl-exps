import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

seed_selection = Transition(label='Seed Selection')
germination_start = Transition(label='Germination Start')
nutrient_mix = Transition(label='Nutrient Mix')
climate_adjust = Transition(label='Climate Adjust')
light_scheduling = Transition(label='Light Scheduling')
pest_inspection = Transition(label='Pest Inspection')
bio_control = Transition(label='Bio Control')
growth_monitor = Transition(label='Growth Monitor')
water_recirc = Transition(label='Water Recirc')
harvest_plan = Transition(label='Harvest Plan')
yield_forecast = Transition(label='Yield Forecast')
quality_check = Transition(label='Quality Check')
packaging_prep = Transition(label='Packaging Prep')
cold_storage = Transition(label='Cold Storage')
delivery_route = Transition(label='Delivery Route')
energy_audit = Transition(label='Energy Audit')
sustain_report = Transition(label='Sustain Report')

# Choices
nutrient_mix_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, SilentTransition()])
climate_adjust_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_adjust, SilentTransition()])
light_scheduling_choice = OperatorPOWL(operator=Operator.XOR, children=[light_scheduling, SilentTransition()])
pest_inspection_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_inspection, SilentTransition()])
bio_control_choice = OperatorPOWL(operator=Operator.XOR, children=[bio_control, SilentTransition()])
growth_monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, SilentTransition()])
water_recirc_choice = OperatorPOWL(operator=Operator.XOR, children=[water_recirc, SilentTransition()])

# Loops
climate_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_adjust_choice, climate_adjust_choice])
light_scheduling_loop = OperatorPOWL(operator=Operator.LOOP, children=[light_scheduling_choice, light_scheduling_choice])
pest_inspection_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_inspection_choice, pest_inspection_choice])
bio_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[bio_control_choice, bio_control_choice])
growth_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor_choice, growth_monitor_choice])
water_recirc_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_recirc_choice, water_recirc_choice])

# Root process
root = StrictPartialOrder(nodes=[
    seed_selection,
    germination_start,
    nutrient_mix_choice,
    climate_adjust_loop,
    light_scheduling_loop,
    pest_inspection_loop,
    bio_control_loop,
    growth_monitor_loop,
    water_recirc_loop,
    harvest_plan,
    yield_forecast,
    quality_check,
    packaging_prep,
    cold_storage,
    delivery_route,
    energy_audit,
    sustain_report
])

root.order.add_edge(seed_selection, germination_start)
root.order.add_edge(germination_start, nutrient_mix_choice)
root.order.add_edge(nutrient_mix_choice, climate_adjust_loop)
root.order.add_edge(climate_adjust_loop, light_scheduling_loop)
root.order.add_edge(light_scheduling_loop, pest_inspection_loop)
root.order.add_edge(pest_inspection_loop, bio_control_loop)
root.order.add_edge(bio_control_loop, growth_monitor_loop)
root.order.add_edge(growth_monitor_loop, water_recirc_loop)
root.order.add_edge(water_recirc_loop, harvest_plan)
root.order.add_edge(harvest_plan, yield_forecast)
root.order.add_edge(yield_forecast, quality_check)
root.order.add_edge(quality_check, packaging_prep)
root.order.add_edge(packaging_prep, cold_storage)
root.order.add_edge(cold_storage, delivery_route)
root.order.add_edge(delivery_route, energy_audit)
root.order.add_edge(energy_audit, sustain_report)

print(root)