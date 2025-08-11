import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Receive_Artifact = Transition(label='Receive Artifact')
Condition_Log = Transition(label='Condition Log')
Radiocarbon_Test = Transition(label='Radiocarbon Test')
Spectroscopy_Scan = Transition(label='Spectroscopy Scan')
Expert_Consult = Transition(label='Expert Consult')
Provenance_Check = Transition(label='Provenance Check')
Archive_Search = Transition(label='Archive Search')
Risk_Assess = Transition(label='Risk Assess')
Three_D_Scan = Transition(label='3D Scan')
Legal_Review = Transition(label='Legal Review')
Insurance_Setup = Transition(label='Insurance Setup')
Certificate_Draft = Transition(label='Certificate Draft')
Certificate_Approve = Transition(label='Certificate Approve')
Climate_Pack = Transition(label='Climate Pack')
Conservation_Plan = Transition(label='Conservation Plan')
Monitoring_Schedule = Transition(label='Monitoring Schedule')

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Receive_Artifact, Condition_Log, Radiocarbon_Test, Spectroscopy_Scan, Expert_Consult, Provenance_Check, Archive_Search, Risk_Assess, Three_D_Scan, Legal_Review, Insurance_Setup, Certificate_Draft, Certificate_Approve, Climate_Pack, Conservation_Plan, Monitoring_Schedule])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)