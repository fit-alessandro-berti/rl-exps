from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the exclusive choice of activities for each step
site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_modules])
design_modules_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_mix])
climate_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[led_tuning, seed_automation])
nutrient_mix_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])
led_tuning_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, energy_audit])
seed_automation_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_system, community_meet])
growth_monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, crop_packing])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, None])

# Define the partial order of the activities
root = StrictPartialOrder(nodes=[
    site_survey_choice,
    design_modules_choice,
    climate_setup_choice,
    nutrient_mix_choice,
    led_tuning_choice,
    seed_automation_choice,
    growth_monitor_choice,
    pest_control_choice
])

# Add dependencies between activities in the partial order
root.order.add_edge(site_survey_choice, design_modules_choice)
root.order.add_edge(design_modules_choice, climate_setup_choice)
root.order.add_edge(climate_setup_choice, nutrient_mix_choice)
root.order.add_edge(nutrient_mix_choice, led_tuning_choice)
root.order.add_edge(led_tuning_choice, seed_automation_choice)
root.order.add_edge(seed_automation_choice, growth_monitor_choice)
root.order.add_edge(growth_monitor_choice, pest_control_choice)
root.order.add_edge(pest_control_choice, compliance_check_choice)
root.order.add_edge(compliance_check_choice, crop_packing_choice)
root.order.add_edge(crop_packing_choice, logistics_plan_choice)

# Print the root POWL model
print(root)