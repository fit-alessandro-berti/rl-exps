import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
root = StrictPartialOrder(nodes=[
    Transition(label='Collection Survey'),
    Transition(label='Provenance Check'),
    Transition(label='Legal Review'),
    Transition(label='Scientific Test'),
    Transition(label='Material Analysis'),
    Transition(label='Ownership Audit'),
    Transition(label='Ethical Screening'),
    Transition(label='Condition Report'),
    Transition(label='Expert Consultation'),
    Transition(label='Transport Planning'),
    Transition(label='Secure Packing'),
    Transition(label='Customs Clearance'),
    Transition(label='Insurance Setup'),
    Transition(label='Exhibit Preparation'),
    Transition(label='Final Approval')
])
root.order.add_edge(Transition(label='Collection Survey'), Transition(label='Provenance Check'))
root.order.add_edge(Transition(label='Provenance Check'), Transition(label='Legal Review'))
root.order.add_edge(Transition(label='Legal Review'), Transition(label='Scientific Test'))
root.order.add_edge(Transition(label='Scientific Test'), Transition(label='Material Analysis'))
root.order.add_edge(Transition(label='Material Analysis'), Transition(label='Ownership Audit'))
root.order.add_edge(Transition(label='Ownership Audit'), Transition(label='Ethical Screening'))
root.order.add_edge(Transition(label='Ethical Screening'), Transition(label='Condition Report'))
root.order.add_edge(Transition(label='Condition Report'), Transition(label='Expert Consultation'))
root.order.add_edge(Transition(label='Expert Consultation'), Transition(label='Transport Planning'))
root.order.add_edge(Transition(label='Transport Planning'), Transition(label='Secure Packing'))
root.order.add_edge(Transition(label='Secure Packing'), Transition(label='Customs Clearance'))
root.order.add_edge(Transition(label='Customs Clearance'), Transition(label='Insurance Setup'))
root.order.add_edge(Transition(label='Insurance Setup'), Transition(label='Exhibit Preparation'))
root.order.add_edge(Transition(label='Exhibit Preparation'), Transition(label='Final Approval'))