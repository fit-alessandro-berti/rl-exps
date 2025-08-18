import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

inspect = Transition(label='Inspect Item')
verify = Transition(label='Verify Provenance')
document = Transition(label='Document Condition')
disassemble = Transition(label='Disassemble Parts')
clean = Transition(label='Clean Components')
analyze = Transition(label='Analyze Damage')
select = Transition(label='Select Materials')
repair = Transition(label='Perform Repairs')
finish = Transition(label='Match Finishes')
treat = Transition(label='Apply Treatments')
reassemble = Transition(label='Reassemble Item')
check = Transition(label='Quality Check')
photograph = Transition(label='Photograph Results')
update = Transition(label='Update Archive')
client_review = Transition(label='Client Review')
final_report = Transition(label='Finalize Report')

skip = SilentTransition()
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[inspect, verify, document, disassemble, clean])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[analyze, select, repair, finish, treat])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[reassemble, check, photograph])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[update, client_review, final_report])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)