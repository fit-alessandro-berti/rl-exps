import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
led_tuning = Transition(label='LED Tuning')
seed_automation = Transition(label='Seed Automation')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
yield_forecast = Transition(label='Yield Forecast')
energy_audit = Transition(label='Energy Audit')
waste_system = Transition(label='Waste System')
community_meet = Transition(label='Community Meet')
compliance_check = Transition(label='Compliance Check')
crop_packing = Transition(label='Crop Packing')
logistics_plan = Transition(label='Logistics Plan')

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_mix, led_tuning, pest_control, yield_forecast])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, energy_audit, waste_system])

# Define main process
root = StrictPartialOrder(nodes=[site_survey, design_modules, climate_loop, monitor_loop, community_meet, compliance_check, crop_packing, logistics_plan])
root.order.add_edge(climate_loop, monitor_loop)
root.order.add_edge(monitor_loop, community_meet)
root.order.add_edge(community_meet, compliance_check)
root.order.add_edge(compliance_check, crop_packing)
root.order.add_edge(crop_packing, logistics_plan)