import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Site_Survey = Transition(label='Site Survey')
Climate_Study = Transition(label='Climate Study')
System_Design = Transition(label='System Design')
Seed_Selection = Transition(label='Seed Selection')
Unit_Install = Transition(label='Unit Install')
Sensor_Setup = Transition(label='Sensor Setup')
Nutrient_Mix = Transition(label='Nutrient Mix')
Energy_Audit = Transition(label='Energy Audit')
Pest_Control = Transition(label='Pest Control')
Crop_Plan = Transition(label='Crop Plan')
Quality_Check = Transition(label='Quality Check')
Yield_Forecast = Transition(label='Yield Forecast')
Supply_Sync = Transition(label='Supply Sync')
Staff_Train = Transition(label='Staff Train')
Data_Review = Transition(label='Data Review')

skip = SilentTransition()

site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[Site_Survey, Climate_Study])
system_design_choice = OperatorPOWL(operator=Operator.XOR, children=[System_Design, skip])
seed_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[Seed_Selection, skip])
unit_install_choice = OperatorPOWL(operator=Operator.XOR, children=[Unit_Install, skip])
sensor_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[Sensor_Setup, skip])
nutrient_mix_choice = OperatorPOWL(operator=Operator.XOR, children=[Nutrient_Mix, skip])
energy_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[Energy_Audit, skip])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[Pest_Control, skip])
crop_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[Crop_Plan, skip])
quality_check_choice = OperatorPOWL(operator=Operator.XOR, children=[Quality_Check, skip])
yield_forecast_choice = OperatorPOWL(operator=Operator.XOR, children=[Yield_Forecast, skip])
supply_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[Supply_Sync, skip])
staff_train_choice = OperatorPOWL(operator=Operator.XOR, children=[Staff_Train, skip])
data_review_choice = OperatorPOWL(operator=Operator.XOR, children=[Data_Review, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_survey_choice, system_design_choice, seed_selection_choice, unit_install_choice, sensor_setup_choice, nutrient_mix_choice, energy_audit_choice, pest_control_choice, crop_plan_choice, quality_check_choice])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast_choice, supply_sync_choice, staff_train_choice, data_review_choice])

root = StrictPartialOrder(nodes=[loop1, loop2])
root.order.add_edge(loop1, loop2)