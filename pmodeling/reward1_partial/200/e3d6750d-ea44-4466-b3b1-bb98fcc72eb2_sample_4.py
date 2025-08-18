import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_node = OperatorPOWL(operator=Operator.FORK, children=[structural_check, iot_setup])
iot_node = OperatorPOWL(operator=Operator.XOR, children=[crop_selection, skip])
crop_node = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_install, skip])
hydro_node = OperatorPOWL(operator=Operator.XOR, children=[water_recycling, skip])
water_node = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])
energy_node = OperatorPOWL(operator=Operator.XOR, children=[plant_scheduling, skip])
plant_node = OperatorPOWL(operator=Operator.XOR, children=[yield_monitoring, skip])
yield_node = OperatorPOWL(operator=Operator.XOR, children=[regulation_review, skip])
regulation_node = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
staff_node = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])
data_node = OperatorPOWL(operator=Operator.XOR, children=[supply_setup, skip])
supply_node = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, skip])
quality_node = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, skip])

root = StrictPartialOrder(nodes=[
    site_survey_node,
    iot_node,
    crop_node,
    hydro_node,
    water_node,
    energy_node,
    plant_node,
    yield_node,
    regulation_node,
    staff_node,
    data_node,
    supply_node,
    quality_node
])
root.order.add_edge(site_survey_node, iot_node)
root.order.add_edge(iot_node, crop_node)
root.order.add_edge(crop_node, hydro_node)
root.order.add_edge(hydro_node, water_node)
root.order.add_edge(water_node, energy_node)
root.order.add_edge(energy_node, plant_node)
root.order.add_edge(plant_node, yield_node)
root.order.add_edge(yield_node, regulation_node)
root.order.add_edge(regulation_node, staff_node)
root.order.add_edge(staff_node, data_node)
root.order.add_edge(data_node, supply_node)
root.order.add_edge(supply_node, quality_node)