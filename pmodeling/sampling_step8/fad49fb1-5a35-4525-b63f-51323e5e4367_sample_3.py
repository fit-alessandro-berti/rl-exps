import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
source_materials = Transition(label='Source Materials')
install_framework = Transition(label='Install Framework')
setup_irrigation = Transition(label='Setup Irrigation')
integrate_sensors = Transition(label='Integrate Sensors')
configure_ai = Transition(label='Configure AI')
select_crops = Transition(label='Select Crops')
calibrate_climate = Transition(label='Calibrate Climate')
plant_seeds = Transition(label='Plant Seeds')
monitor_growth = Transition(label='Monitor Growth')
manage_pests = Transition(label='Manage Pests')
recycle_waste = Transition(label='Recycle Waste')
engage_community = Transition(label='Engage Community')
ensure_compliance = Transition(label='Ensure Compliance')
distribute_produce = Transition(label='Distribute Produce')

# Define the control flow operators
site_survey_xor_design = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_modules])
source_materials_xor_framework = OperatorPOWL(operator=Operator.XOR, children=[source_materials, install_framework])
irrigation_xor_sensors = OperatorPOWL(operator=Operator.XOR, children=[setup_irrigation, integrate_sensors])
ai_xor_crops = OperatorPOWL(operator=Operator.XOR, children=[configure_ai, select_crops])
climate_xor_seeds = OperatorPOWL(operator=Operator.XOR, children=[calibrate_climate, plant_seeds])
growth_xor_pests = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, manage_pests])
waste_xor_community = OperatorPOWL(operator=Operator.XOR, children=[recycle_waste, engage_community])
compliance_xor_produce = OperatorPOWL(operator=Operator.XOR, children=[ensure_compliance, distribute_produce])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey_xor_design, source_materials_xor_framework, irrigation_xor_sensors, ai_xor_crops, climate_xor_seeds, growth_xor_pests, waste_xor_community, compliance_xor_produce])
root.order.add_edge(site_survey_xor_design, source_materials_xor_framework)
root.order.add_edge(source_materials_xor_framework, irrigation_xor_sensors)
root.order.add_edge(irrigation_xor_sensors, ai_xor_crops)
root.order.add_edge(ai_xor_crops, climate_xor_seeds)
root.order.add_edge(climate_xor_seeds, growth_xor_pests)
root.order.add_edge(growth_xor_pests, waste_xor_community)
root.order.add_edge(waste_xor_community, compliance_xor_produce)