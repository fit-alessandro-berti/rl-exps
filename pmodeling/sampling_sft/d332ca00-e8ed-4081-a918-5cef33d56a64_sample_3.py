import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake = Transition(label='Intake Document')
visual = Transition(label='Visual Inspect')
imaging = Transition(label='Imaging Scan')
material = Transition(label='Material Test')
database = Transition(label='Database Cross')
provenance = Transition(label='Provenance Check')
expert = Transition(label='Expert Consult')
carbon = Transition(label='Carbon Dating')
forensic = Transition(label='Forensic Analyze')
anomaly = Transition(label='Anomaly Review')
risk = Transition(label='Risk Assess')
report = Transition(label='Report Draft')
insurance = Transition(label='Insurance Quote')
storage = Transition(label='Storage Plan')
approval = Transition(label='Final Approval')

# Loop for anomaly review and risk assessment
loop_anomaly = OperatorPOWL(operator=Operator.LOOP, children=[anomaly, risk])

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake,
    visual,
    imaging,
    material,
    database,
    provenance,
    expert,
    carbon,
    forensic,
    loop_anomaly,
    report,
    insurance,
    storage,
    approval
])

# Define the control-flow order
root.order.add_edge(intake, visual)
root.order.add_edge(intake, imaging)
root.order.add_edge(intake, material)
root.order.add_edge(intake, database)
root.order.add_edge(intake, provenance)
root.order.add_edge(intake, expert)

# After initial intake, imaging and material tests precede provenance check
root.order.add_edge(visual, provenance)
root.order.add_edge(imaging, provenance)
root.order.add_edge(material, provenance)

# Provenance check must complete before expert consultation
root.order.add_edge(provenance, expert)

# Expert consultation must complete before carbon dating
root.order.add_edge(expert, carbon)

# Carbon dating must complete before forensic analysis
root.order.add_edge(carbon, forensic)

# Forensic analysis can happen in parallel with the anomaly review loop
root.order.add_edge(forensic, loop_anomaly)

# After forensic analysis, anomaly review and risk assessment loop can proceed
root.order.add_edge(forensic, loop_anomaly)

# Anomaly review and risk assessment loop must complete before report drafting
root.order.add_edge(loop_anomaly, report)

# Report drafting can proceed in parallel with insurance and storage planning
root.order.add_edge(report, insurance)
root.order.add_edge(report, storage)

# Insurance and storage planning can proceed in parallel before final approval
root.order.add_edge(insurance, approval)
root.order.add_edge(storage, approval)

# Final approval must complete after all other activities
root.order.add_edge(approval, None)