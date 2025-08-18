from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Site Survey -> Climate Study
climate_study_node = OperatorPOWL(operator=Operator.XOR, children=[climate_study, skip])
root.order.add_edge(site_survey, climate_study_node)

# Climate Study -> Design Layout
design_layout_node = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])
root.order.add_edge(climate_study_node, design_layout_node)

# Design Layout -> System Install
system_install_node = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])
root.order.add_edge(design_layout_node, system_install_node)

# System Install -> Crop Select
crop_select_node = OperatorPOWL(operator=Operator.XOR, children=[crop_select, skip])
root.order.add_edge(system_install_node, crop_select_node)

# Crop Select -> Nutrient Plan
nutrient_plan_node = OperatorPOWL(operator=Operator.XOR, children=[nutrient_plan, skip])
root.order.add_edge(crop_select_node, nutrient_plan_node)

# Nutrient Plan -> Sensor Setup
sensor_setup_node = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, skip])
root.order.add_edge(nutrient_plan_node, sensor_setup_node)

# Sensor Setup -> Automation Test
automation_test_node = OperatorPOWL(operator=Operator.XOR, children=[automation_test, skip])
root.order.add_edge(sensor_setup_node, automation_test_node)

# Automation Test -> Staff Train
staff_train_node = OperatorPOWL(operator=Operator.XOR, children=[staff_train, skip])
root.order.add_edge(automation_test_node, staff_train_node)

# Staff Train -> Compliance Check
compliance_check_node = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
root.order.add_edge(staff_train_node, compliance_check_node)

# Compliance Check -> Marketing Sync
marketing_sync_node = OperatorPOWL(operator=Operator.XOR, children=[marketing_sync, skip])
root.order.add_edge(compliance_check_node, marketing_sync_node)

# Marketing Sync -> Data Monitor
data_monitor_node = OperatorPOWL(operator=Operator.XOR, children=[data_monitor, skip])
root.order.add_edge(marketing_sync_node, data_monitor_node)

# Data Monitor -> Yield Analyze
yield_analyze_node = OperatorPOWL(operator=Operator.XOR, children=[yield_analyze, skip])
root.order.add_edge(data_monitor_node, yield_analyze_node)

# Yield Analyze -> Supply Chain
supply_chain_node = OperatorPOWL(operator=Operator.XOR, children=[supply_chain, skip])
root.order.add_edge(yield_analyze_node, supply_chain_node)

# Supply Chain -> Customer Engage
customer_engage_node = OperatorPOWL(operator=Operator.XOR, children=[customer_engage, skip])
root.order.add_edge(supply_chain_node, customer_engage_node)

# Define the root node
root = StrictPartialOrder(nodes=[
    site_survey, climate_study, design_layout, system_install,
    crop_select, nutrient_plan, sensor_setup, automation_test,
    staff_train, compliance_check, marketing_sync, data_monitor,
    yield_analyze, supply_chain, customer_engage,
    climate_study_node, design_layout_node, system_install_node,
    crop_select_node, nutrient_plan_node, sensor_setup_node,
    automation_test_node, staff_train_node, compliance_check_node,
    marketing_sync_node, data_monitor_node, yield_analyze_node,
    supply_chain_node, customer_engage_node
])

# Add edges
root.order.add_edge(site_survey, climate_study_node)
root.order.add_edge(climate_study_node, design_layout_node)
root.order.add_edge(design_layout_node, system_install_node)
root.order.add_edge(system_install_node, crop_select_node)
root.order.add_edge(crop_select_node, nutrient_plan_node)
root.order.add_edge(nutrient_plan_node, sensor_setup_node)
root.order.add_edge(sensor_setup_node, automation_test_node)
root.order.add_edge(automation_test_node, staff_train_node)
root.order.add_edge(staff_train_node, compliance_check_node)
root.order.add_edge(compliance_check_node, marketing_sync_node)
root.order.add_edge(marketing_sync_node, data_monitor_node)
root.order.add_edge(data_monitor_node, yield_analyze_node)
root.order.add_edge(yield_analyze_node, supply_chain_node)
root.order.add_edge(supply_chain_node, customer_engage_node)