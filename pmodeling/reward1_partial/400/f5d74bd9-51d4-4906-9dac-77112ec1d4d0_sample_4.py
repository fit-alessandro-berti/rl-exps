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

xor = OperatorPOWL(operator=Operator.XOR, children=[sustainability_check, skip])

loop = OperatorPOWL(operator=Operator.LOOP, children=[community_engage, logistics_plan])

xor2 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, sensor_install])

xor3 = OperatorPOWL(operator=Operator.XOR, children=[staff_train, nutrient_mix])

xor4 = OperatorPOWL(operator=Operator.XOR, children=[hydroponics_setup, design_plan])

xor5 = OperatorPOWL(operator=Operator.XOR, children=[crop_select, structure_mod])

xor6 = OperatorPOWL(operator=Operator.XOR, children=[impact_study, site_review])

root = StrictPartialOrder(nodes=[xor6, xor5, xor4, xor3, xor2, loop, xor])
root.order.add_edge(xor6, xor5)
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, loop)
root.order.add_edge(loop, xor)