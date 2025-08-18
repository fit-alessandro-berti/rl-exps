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

skip = SilentTransition()

# Process flow: Seed Selection -> Germination Start -> Nutrient Mix -> Climate Adjust -> Light Scheduling -> Pest Inspection -> Bio Control -> Growth Monitor -> Water Recirc
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[germination_start, nutrient_mix, climate_adjust, light_scheduling, pest_inspection, bio_control, growth_monitor, water_recirc])
# Process flow: Harvest Plan -> Yield Forecast -> Quality Check -> Packaging Prep -> Cold Storage -> Delivery Route
xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, yield_forecast, quality_check, packaging_prep, cold_storage, delivery_route])
# Process flow: Energy Audit -> Sustain Report
xor2 = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, sustain_report])

root = StrictPartialOrder(nodes=[loop1, xor, xor2])
root.order.add_edge(loop1, xor)
root.order.add_edge(xor, xor2)