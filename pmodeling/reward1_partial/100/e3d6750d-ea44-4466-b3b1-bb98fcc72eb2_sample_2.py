import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions (activities)
site_survey = Transition(label='Site Survey')
structural_check = Transition(label='Structural Check')
iot_setup = Transition(label='IoT Setup')
crop_selection = Transition(label='Crop Selection')
hydroponic_install = Transition(label='Hydroponic Install')
water_recycling = Transition(label='Water Recycling')
energy_audit = Transition(label='Energy Audit')
plant_scheduling = Transition(label='Plant Scheduling')
yield_monitoring = Transition(label='Yield Monitoring')
regulation_review = Transition(label='Regulation Review')
staff_training = Transition(label='Staff Training')
data_integration = Transition(label='Data Integration')
supply_setup = Transition(label='Supply Setup')
quality_audit = Transition(label='Quality Audit')
logistics_plan = Transition(label='Logistics Plan')

# Define silent transitions
skip = SilentTransition()

# Define nodes and operators
site_survey_node = OperatorPOWL(operator=Operator.PO, children=[site_survey, structural_check])
iot_node = OperatorPOWL(operator=Operator.PO, children=[iot_setup, crop_selection])
hydroponic_node = OperatorPOWL(operator=Operator.PO, children=[hydroponic_install, water_recycling, energy_audit])
planting_node = OperatorPOWL(operator=Operator.PO, children=[plant_scheduling, yield_monitoring])
regulation_node = OperatorPOWL(operator=Operator.PO, children=[regulation_review, staff_training, data_integration])
supply_node = OperatorPOWL(operator=Operator.PO, children=[supply_setup, quality_audit, logistics_plan])

# Create the root node with partial order
root = StrictPartialOrder(nodes=[site_survey_node, iot_node, hydroponic_node, planting_node, regulation_node, supply_node])

# Define dependencies between nodes
root.order.add_edge(site_survey_node, iot_node)
root.order.add_edge(iot_node, hydroponic_node)
root.order.add_edge(hydroponic_node, planting_node)
root.order.add_edge(planting_node, regulation_node)
root.order.add_edge(regulation_node, supply_node)

print(root)