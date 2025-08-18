import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

collection_survey = Transition(label='Collection Survey')
provenance_check = Transition(label='Provenance Check')
legal_review = Transition(label='Legal Review')
scientific_test = Transition(label='Scientific Test')
material_analysis = Transition(label='Material Analysis')
ownership_audit = Transition(label='Ownership Audit')
ethical_screening = Transition(label='Ethical Screening')
condition_report = Transition(label='Condition Report')
expert_consultation = Transition(label='Expert Consultation')
transport_planning = Transition(label='Transport Planning')
secure_packing = Transition(label='Secure Packing')
customs_clearance = Transition(label='Customs Clearance')
insurance_setup = Transition(label='Insurance Setup')
exhibit_preparation = Transition(label='Exhibit Preparation')
final_approval = Transition(label='Final Approval')

skip = SilentTransition()

xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ethical_screening, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[expert_consultation, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[customs_clearance, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[exhibit_preparation, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

root = StrictPartialOrder(nodes=[
    collection_survey,
    provenance_check,
    scientific_test,
    material_analysis,
    ownership_audit,
    xor1,
    xor2,
    xor3,
    xor4,
    xor5,
    xor6,
    xor7,
    xor8
])
root.order.add_edge(collection_survey, provenance_check)
root.order.add_edge(provenance_check, scientific_test)
root.order.add_edge(scientific_test, material_analysis)
root.order.add_edge(material_analysis, ownership_audit)
root.order.add_edge(ownership_audit, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)