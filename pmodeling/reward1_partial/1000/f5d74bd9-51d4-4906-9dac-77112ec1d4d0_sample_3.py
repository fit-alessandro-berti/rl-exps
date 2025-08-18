import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_review = Transition(label='Site Review')
impact_study = Transition(label='Impact Study')
design_plan = Transition(label='Design Plan')
structure_mod = Transition(label='Structure Mod')
hydroponics_setup = Transition(label='Hydroponics Setup')
crop_select = Transition(label='Crop Select')
nutrient_mix = Transition(label='Nutrient Mix')
pest_control = Transition(label='Pest Control')
sensor_install = Transition(label='Sensor Install')
staff_train = Transition(label='Staff Train')
compliance_audit = Transition(label='Compliance Audit')
packaging_dev = Transition(label='Packaging Dev')
logistics_plan = Transition(label='Logistics Plan')
community_engage = Transition(label='Community Engage')
sustainability_check = Transition(label='Sustainability Check')

skip = SilentTransition()

site_analysis = OperatorPOWL(operator=Operator.LOOP, children=[site_review, impact_study])
structural_modifications = OperatorPOWL(operator=Operator.LOOP, children=[design_plan, structure_mod])
hydroponic_system = OperatorPOWL(operator=Operator.LOOP, children=[hydroponics_setup, nutrient_mix])
pest_control_system = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, sensor_install])
staff_training = OperatorPOWL(operator=Operator.LOOP, children=[staff_train, compliance_audit])
community_engagement = OperatorPOWL(operator=Operator.LOOP, children=[community_engage, sustainability_check])

root = StrictPartialOrder(nodes=[site_analysis, structural_modifications, hydroponic_system, pest_control_system, staff_training, community_engagement])
root.order.add_edge(site_analysis, structural_modifications)
root.order.add_edge(structural_modifications, hydroponic_system)
root.order.add_edge(hydroponic_system, pest_control_system)
root.order.add_edge(pest_control_system, staff_training)
root.order.add_edge(staff_training, community_engagement)