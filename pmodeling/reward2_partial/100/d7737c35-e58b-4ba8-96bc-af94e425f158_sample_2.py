import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

MilkSourcing = Transition(label='Milk Sourcing')
SupplierAudit = Transition(label='Supplier Audit')
CulturePrep = Transition(label='Culture Prep')
MilkTesting = Transition(label='Milk Testing')
FermentationStart = Transition(label='Fermentation Start')
pHMonitoring = Transition(label='pH Monitoring')
CurdCutting = Transition(label='Curd Cutting')
MoldInoculation = Transition(label='Mold Inoculation')
AgingSetup = Transition(label='Aging Setup')
HumidityControl = Transition(label='Humidity Control')
TextureCheck = Transition(label='Texture Check')
FlavorProfiling = Transition(label='Flavor Profiling')
BatchLabeling = Transition(label='Batch Labeling')
Packaging = Transition(label='Packaging')
Distribution = Transition(label='Distribution')
FeedbackReview = Transition(label='Feedback Review')
SustainabilityAudit = Transition(label='Sustainability Audit')

root = StrictPartialOrder(nodes=[
    MilkSourcing, SupplierAudit, CulturePrep, MilkTesting, FermentationStart, pHMonitoring, CurdCutting, MoldInoculation, AgingSetup, HumidityControl, TextureCheck, FlavorProfiling, BatchLabeling, Packaging, Distribution, FeedbackReview, SustainabilityAudit
])

# Add dependencies
root.order.add_edge(MilkSourcing, SupplierAudit)
root.order.add_edge(SupplierAudit, CulturePrep)
root.order.add_edge(CulturePrep, MilkTesting)
root.order.add_edge(MilkTesting, FermentationStart)
root.order.add_edge(FermentationStart, pHMonitoring)
root.order.add_edge(pHMonitoring, CurdCutting)
root.order.add_edge(CurdCutting, MoldInoculation)
root.order.add_edge(MoldInoculation, AgingSetup)
root.order.add_edge(AgingSetup, HumidityControl)
root.order.add_edge(HumidityControl, TextureCheck)
root.order.add_edge(TextureCheck, FlavorProfiling)
root.order.add_edge(FlavorProfiling, BatchLabeling)
root.order.add_edge(BatchLabeling, Packaging)
root.order.add_edge(Packaging, Distribution)
root.order.add_edge(Distribution, FeedbackReview)
root.order.add_edge(FeedbackReview, SustainabilityAudit)

print(root)