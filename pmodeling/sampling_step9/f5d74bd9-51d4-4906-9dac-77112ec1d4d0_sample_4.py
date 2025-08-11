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

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[site_review, impact_study])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[design_plan, structure_mod])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[hydroponics_setup, crop_select])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix, pest_control])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, staff_train])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[compliance_audit, packaging_dev])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[logistics_plan, community_engage])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_check, skip])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop5, loop6])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop7, loop8])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor1)

print(root)