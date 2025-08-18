import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
permit_filing = Transition(label='Permit Filing')
design_layout = Transition(label='Design Layout')
install_hvac = Transition(label='Install HVAC')
set_lighting = Transition(label='Set Lighting')
build_racks = Transition(label='Build Racks')
install_hydroponics = Transition(label='Install Hydroponics')
configure_sensors = Transition(label='Configure Sensors')
select_crops = Transition(label='Select Crops')
seed_planting = Transition(label='Seed Planting')
monitor_growth = Transition(label='Monitor Growth')
nutrient_mixing = Transition(label='Nutrient Mixing')
staff_training = Transition(label='Staff Training')
market_launch = Transition(label='Market Launch')
waste_recycling = Transition(label='Waste Recycling')
customer_onboarding = Transition(label='Customer Onboarding')

skip = SilentTransition()

site_survey_audit = OperatorPOWL(operator=Operator.XOR, children=[site_survey, structural_audit])
permit_design = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, design_layout])
hvac_racks = OperatorPOWL(operator=Operator.XOR, children=[install_hvac, build_racks])
hydroponics_sensors = OperatorPOWL(operator=Operator.XOR, children=[install_hydroponics, configure_sensors])
crops_planting = OperatorPOWL(operator=Operator.XOR, children=[select_crops, seed_planting])
growth_monitor = OperatorPOWL(operator=Operator.XOR, children=[monitor_growth, nutrient_mixing])
training_market = OperatorPOWL(operator=Operator.XOR, children=[staff_training, market_launch])
waste_recycling_customer = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, customer_onboarding])

root = StrictPartialOrder(nodes=[
    site_survey_audit, permit_design, hvac_racks, hydroponics_sensors, crops_planting,
    growth_monitor, training_market, waste_recycling_customer])
root.order.add_edge(site_survey_audit, permit_design)
root.order.add_edge(permit_design, hvac_racks)
root.order.add_edge(hvac_racks, hydroponics_sensors)
root.order.add_edge(hydroponics_sensors, crops_planting)
root.order.add_edge(crops_planting, growth_monitor)
root.order.add_edge(growth_monitor, training_market)
root.order.add_edge(training_market, waste_recycling_customer)