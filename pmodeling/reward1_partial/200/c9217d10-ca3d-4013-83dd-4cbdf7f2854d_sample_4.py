import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names as specified
site_survey = Transition(label='Site Survey')
climate_study = Transition(label='Climate Study')
design_layout = Transition(label='Design Layout')
system_install = Transition(label='System Install')
crop_select = Transition(label='Crop Select')
nutrient_plan = Transition(label='Nutrient Plan')
sensor_setup = Transition(label='Sensor Setup')
automation_test = Transition(label='Automation Test')
staff_train = Transition(label='Staff Train')
compliance_check = Transition(label='Compliance Check')
marketing_sync = Transition(label='Marketing Sync')
data_monitor = Transition(label='Data Monitor')
yield_analyze = Transition(label='Yield Analyze')
supply_chain = Transition(label='Supply Chain')
customer_engage = Transition(label='Customer Engage')

# Define silent transitions
skip = SilentTransition()

# Define the partial order model
root = StrictPartialOrder()

# Add activities to the root
root.nodes.add(site_survey)
root.nodes.add(climate_study)
root.nodes.add(design_layout)
root.nodes.add(system_install)
root.nodes.add(crop_select)
root.nodes.add(nutrient_plan)
root.nodes.add(sensor_setup)
root.nodes.add(automation_test)
root.nodes.add(staff_train)
root.nodes.add(compliance_check)
root.nodes.add(marketing_sync)
root.nodes.add(data_monitor)
root.nodes.add(yield_analyze)
root.nodes.add(supply_chain)
root.nodes.add(customer_engage)

# Define the dependencies (edges) in the partial order
root.order.add_edge(site_survey, climate_study)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(climate_study, design_layout)
root.order.add_edge(climate_study, system_install)
root.order.add_edge(design_layout, system_install)
root.order.add_edge(system_install, crop_select)
root.order.add_edge(crop_select, nutrient_plan)
root.order.add_edge(nutrient_plan, sensor_setup)
root.order.add_edge(sensor_setup, automation_test)
root.order.add_edge(automation_test, staff_train)
root.order.add_edge(staff_train, compliance_check)
root.order.add_edge(compliance_check, marketing_sync)
root.order.add_edge(marketing_sync, data_monitor)
root.order.add_edge(data_monitor, yield_analyze)
root.order.add_edge(yield_analyze, supply_chain)
root.order.add_edge(supply_chain, customer_engage)

print(root)