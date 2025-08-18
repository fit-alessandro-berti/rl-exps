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

# Define POWL models for each activity
site_survey_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[site_survey])
design_modules_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[design_modules])
climate_setup_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[climate_setup])
nutrient_mix_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[nutrient_mix])
led_tuning_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[led_tuning])
seed_automation_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[seed_automation])
growth_monitor_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[growth_monitor])
pest_control_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[pest_control])
yield_forecast_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[yield_forecast])
energy_audit_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[energy_audit])
waste_system_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[waste_system])
community_meet_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[community_meet])
compliance_check_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[compliance_check])
crop_packing_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[crop_packing])
logistics_plan_model = OperatorPOWL(operator=Operator.ACTIVITY, children=[logistics_plan])

# Define loops and choices
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup_model, nutrient_mix_model])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control_model, yield_forecast_model, energy_audit_model])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_system_model])
community_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_meet_model, compliance_check_model, crop_packing_model])
logistics_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan_model])

# Define the root model
root = StrictPartialOrder(nodes=[site_survey_model, design_modules_model, climate_loop, pest_loop, waste_loop, community_loop, logistics_loop])
root.order.add_edge(site_survey_model, design_modules_model)
root.order.add_edge(site_survey_model, climate_loop)
root.order.add_edge(site_survey_model, pest_loop)
root.order.add_edge(site_survey_model, waste_loop)
root.order.add_edge(site_survey_model, community_loop)
root.order.add_edge(site_survey_model, logistics_loop)

print(root)