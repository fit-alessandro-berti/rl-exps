import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.log.obj import EventLog
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.algo.conformance.tokenreplay import factory as token_replay
from pm4py.algo.conformance.tokenreplay.parameters import Parameters
from pm4py.visualization.petri_net import factory as pn_vis_factory
from pm4py.visualization.petri_net.variants import basic as pn_vis_ba

# Define the POWL model
A = Transition(label='Provenance Check')
B = Transition(label='Material Test')
C = Transition(label='Archive Search')
D = Transition(label='Expert Review')
E = Transition(label='3D Scanning')
F = Transition(label='Wear Analysis')
G = Transition(label='Database Cross')
H = Transition(label='Law Consult')
I = Transition(label='Forgery Detect')
J = Transition(label='Certification')
K = Transition(label='Document Prep')
L = Transition(label='Client Brief')
M = Transition(label='Secure Storage')
N = Transition(label='Risk Assessment')
O = Transition(label='Final Approval')
X = SilentTransition()
Y = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[A, X])
material_choice = OperatorPOWL(operator=Operator.XOR, children=[B, X])
archive_loop = OperatorPOWL(operator=Operator.LOOP, children=[C, D, X])
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[E, F, X])
database_loop = OperatorPOWL(operator=Operator.LOOP, children=[G, H, X])
law_loop = OperatorPOWL(operator=Operator.LOOP, children=[I, J, X])
certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[K, L, X])
secure_loop = OperatorPOWL(operator=Operator.LOOP, children=[M, N, X])
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[O, Y])

root = StrictPartialOrder(nodes=[provenance_loop, material_choice, archive_loop, expert_choice, database_loop, law_loop, certification_loop, secure_loop, risk_loop])
root.order.add_edge(provenance_loop, material_choice)
root.order.add_edge(material_choice, archive_loop)
root.order.add_edge(archive_loop, expert_choice)
root.order.add_edge(expert_choice, database_loop)
root.order.add_edge(database_loop, law_loop)
root.order.add_edge(law_loop, certification_loop)
root.order.add_edge(certification_loop, secure_loop)
root.order.add_edge(secure_loop, risk_loop)

# Visualize the POWL model
graph = pn_vis_ba.apply(root)
pn_vis_ba.view(graph)