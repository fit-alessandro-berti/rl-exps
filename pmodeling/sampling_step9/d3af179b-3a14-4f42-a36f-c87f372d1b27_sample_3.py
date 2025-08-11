import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loops and choices
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, energy_audit])
yield_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, yield_forecast])
waste_system_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_system, waste_system])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
community_meet_choice = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])

# Define the root node with all activities and loops/choices
root = StrictPartialOrder(nodes=[site_survey, design_modules, climate_loop, nutrient_mix, led_tuning, seed_automation, growth_monitor, pest_control_choice, yield_forecast_loop, energy_audit, waste_system_loop, community_meet_choice, compliance_check, crop_packing, logistics_plan])
root.order.add_edge(site_survey, design_modules)
root.order.add_edge(design_modules, climate_loop)
root.order.add_edge(climate_loop, nutrient_mix)
root.order.add_edge(nutrient_mix, led_tuning)
root.order.add_edge(led_tuning, seed_automation)
root.order.add_edge(seed_automation, growth_monitor)
root.order.add_edge(growth_monitor, pest_control_choice)
root.order.add_edge(pest_control_choice, yield_forecast_loop)
root.order.add_edge(yield_forecast_loop, energy_audit)
root.order.add_edge(energy_audit, waste_system_loop)
root.order.add_edge(waste_system_loop, community_meet_choice)
root.order.add_edge(community_meet_choice, compliance_check)
root.order.add_edge(compliance_check, crop_packing)
root.order.add_edge(crop_packing, logistics_plan)