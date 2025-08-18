import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
modular_design = Transition(label='Modular Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_config = Transition(label='Climate Config')
nutrient_mix = Transition(label='Nutrient Mix')
pest_detect = Transition(label='Pest Detect')
lighting_setup = Transition(label='Lighting Setup')
energy_audit = Transition(label='Energy Audit')
automation_install = Transition(label='Automation Install')
staff_training = Transition(label='Staff Training')
market_analysis = Transition(label='Market Analysis')
regulation_check = Transition(label='Regulation Check')
yield_monitor = Transition(label='Yield Monitor')
waste_manage = Transition(label='Waste Manage')
data_analytics = Transition(label='Data Analytics')

# Define the process
site_survey_order = OperatorPOWL(operator=Operator.ORDER, children=[structural_audit, modular_design])
modular_design_order = OperatorPOWL(operator=Operator.ORDER, children=[hydroponic_setup, climate_config, nutrient_mix, pest_detect])
climate_config_order = OperatorPOWL(operator=Operator.ORDER, children=[lighting_setup, energy_audit, automation_install])
hydroponic_setup_order = OperatorPOWL(operator=Operator.ORDER, children=[staff_training, market_analysis, regulation_check])
pest_detect_order = OperatorPOWL(operator=Operator.ORDER, children=[yield_monitor, waste_manage, data_analytics])

# Define the root node
root = StrictPartialOrder(nodes=[site_survey, site_survey_order, modular_design_order, hydroponic_setup_order, climate_config_order, pest_detect_order])
root.order.add_edge(site_survey, site_survey_order)
root.order.add_edge(site_survey_order, modular_design_order)
root.order.add_edge(modular_design_order, hydroponic_setup_order)
root.order.add_edge(hydroponic_setup_order, climate_config_order)
root.order.add_edge(climate_config_order, pest_detect_order)

# Print the root node
print(root)