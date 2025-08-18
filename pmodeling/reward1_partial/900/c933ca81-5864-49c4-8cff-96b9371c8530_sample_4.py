import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
ClientConsult = Transition(label='Client Consult')
SpecFinalize = Transition(label='Spec Finalize')
DesignDraft = Transition(label='Design Draft')
AerodynamicsTest = Transition(label='Aerodynamics Test')
AIIntegration = Transition(label='AI Integration')
MaterialSourcing = Transition(label='Material Sourcing')
ComponentOrder = Transition(label='Component Order')
AssemblyLine = Transition(label='Assembly Line')
FirmwareInstall = Transition(label='Firmware Install')
EnvironmentalTest = Transition(label='Environmental Test')
QualityCheck = Transition(label='Quality Check')
BrandPackaging = Transition(label='Brand Packaging')
ShippingPrep = Transition(label='Shipping Prep')
DeliverySchedule = Transition(label='Delivery Schedule')
PostSaleSupport = Transition(label='Post-Sale Support')

# Define the Partial Order (POWL model)
root = StrictPartialOrder(
    nodes=[
        ClientConsult,
        SpecFinalize,
        DesignDraft,
        AerodynamicsTest,
        AIIntegration,
        MaterialSourcing,
        ComponentOrder,
        AssemblyLine,
        FirmwareInstall,
        EnvironmentalTest,
        QualityCheck,
        BrandPackaging,
        ShippingPrep,
        DeliverySchedule,
        PostSaleSupport
    ]
)

# Define the partial order dependencies
root.order.add_edge(ClientConsult, SpecFinalize)
root.order.add_edge(SpecFinalize, DesignDraft)
root.order.add_edge(DesignDraft, AerodynamicsTest)
root.order.add_edge(AerodynamicsTest, AIIntegration)
root.order.add_edge(AIIntegration, MaterialSourcing)
root.order.add_edge(MaterialSourcing, ComponentOrder)
root.order.add_edge(ComponentOrder, AssemblyLine)
root.order.add_edge(AssemblyLine, FirmwareInstall)
root.order.add_edge(FirmwareInstall, EnvironmentalTest)
root.order.add_edge(EnvironmentalTest, QualityCheck)
root.order.add_edge(QualityCheck, BrandPackaging)
root.order.add_edge(BrandPackaging, ShippingPrep)
root.order.add_edge(ShippingPrep, DeliverySchedule)
root.order.add_edge(DeliverySchedule, PostSaleSupport)

# Print the root of the POWL model
print(root)