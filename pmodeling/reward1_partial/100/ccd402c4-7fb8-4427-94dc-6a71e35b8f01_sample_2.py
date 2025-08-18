from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
stakeholder_meet = Transition(label='Stakeholder Meet')
design_layout = Transition(label='Design Layout')
iot_install = Transition(label='IoT Install')
sensor_calibrate = Transition(label='Sensor Calibrate')
hydroponic_setup = Transition(label='Hydroponic Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_sowing = Transition(label='Seed Sowing')
climate_control = Transition(label='Climate Control')
data_monitor = Transition(label='Data Monitor')
yield_forecast = Transition(label='Yield Forecast')
energy_plan = Transition(label='Energy Plan')
maintenance_plan = Transition(label='Maintenance Plan')
harvest_prep = Transition(label='Harvest Prep')
supply_dispatch = Transition(label='Supply Dispatch')
market_launch = Transition(label='Market Launch')

# Define silent transitions for parallel operations
skip = SilentTransition()

# Define POWL models
site_survey_node = OperatorPOWL(operator=Operator.PARALLEL, children=[site_survey, permit_filing])
stakeholder_meet_node = OperatorPOWL(operator=Operator.PARALLEL, children=[stakeholder_meet, design_layout])
iot_install_node = OperatorPOWL(operator=Operator.PARALLEL, children=[iot_install, sensor_calibrate])
hydroponic_setup_node = OperatorPOWL(operator=Operator.PARALLEL, children=[hydroponic_setup, nutrient_mix])
seed_sowing_node = OperatorPOWL(operator=Operator.PARALLEL, children=[seed_sowing, climate_control])
data_monitor_node = OperatorPOWL(operator=Operator.PARALLEL, children=[data_monitor, yield_forecast])
energy_plan_node = OperatorPOWL(operator=Operator.PARALLEL, children=[energy_plan, maintenance_plan])
harvest_prep_node = OperatorPOWL(operator=Operator.PARALLEL, children=[harvest_prep, supply_dispatch])
market_launch_node = OperatorPOWL(operator=Operator.PARALLEL, children=[market_launch])

# Define the root POWL model with dependencies
root = StrictPartialOrder(nodes=[
    site_survey_node, stakeholder_meet_node, iot_install_node, hydroponic_setup_node, 
    seed_sowing_node, data_monitor_node, energy_plan_node, harvest_prep_node, market_launch_node
])

# Add dependencies between nodes
root.order.add_edge(site_survey_node, stakeholder_meet_node)
root.order.add_edge(site_survey_node, iot_install_node)
root.order.add_edge(site_survey_node, hydroponic_setup_node)
root.order.add_edge(site_survey_node, seed_sowing_node)
root.order.add_edge(site_survey_node, data_monitor_node)
root.order.add_edge(site_survey_node, energy_plan_node)
root.order.add_edge(site_survey_node, harvest_prep_node)
root.order.add_edge(site_survey_node, market_launch_node)

root.order.add_edge(stakeholder_meet_node, iot_install_node)
root.order.add_edge(stakeholder_meet_node, hydroponic_setup_node)
root.order.add_edge(stakeholder_meet_node, seed_sowing_node)
root.order.add_edge(stakeholder_meet_node, data_monitor_node)
root.order.add_edge(stakeholder_meet_node, energy_plan_node)
root.order.add_edge(stakeholder_meet_node, harvest_prep_node)
root.order.add_edge(stakeholder_meet_node, market_launch_node)

root.order.add_edge(iot_install_node, hydroponic_setup_node)
root.order.add_edge(iot_install_node, seed_sowing_node)
root.order.add_edge(iot_install_node, data_monitor_node)
root.order.add_edge(iot_install_node, energy_plan_node)
root.order.add_edge(iot_install_node, harvest_prep_node)
root.order.add_edge(iot_install_node, market_launch_node)

root.order.add_edge(hydroponic_setup_node, seed_sowing_node)
root.order.add_edge(hydroponic_setup_node, data_monitor_node)
root.order.add_edge(hydroponic_setup_node, energy_plan_node)
root.order.add_edge(hydroponic_setup_node, harvest_prep_node)
root.order.add_edge(hydroponic_setup_node, market_launch_node)

root.order.add_edge(seed_sowing_node, data_monitor_node)
root.order.add_edge(seed_sowing_node, energy_plan_node)
root.order.add_edge(seed_sowing_node, harvest_prep_node)
root.order.add_edge(seed_sowing_node, market_launch_node)

root.order.add_edge(data_monitor_node, energy_plan_node)
root.order.add_edge(data_monitor_node, harvest_prep_node)
root.order.add_edge(data_monitor_node, market_launch_node)

root.order.add_edge(energy_plan_node, harvest_prep_node)
root.order.add_edge(energy_plan_node, market_launch_node)

root.order.add_edge(harvest_prep_node, market_launch_node)

print(root)