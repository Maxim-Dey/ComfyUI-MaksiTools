from .nodes.MT_Time_Measure_Node import MT_Time_Measure_Node
from .nodes.Datatype_Nodes import ReturnBooleanNode, ReturnIntegerNode, ReturnFloatNode, ReturnStringNode

NODE_CLASS_MAPPINGS = {
    "MT Time Measure Node": MT_Time_Measure_Node,
    "Return Boolean": ReturnBooleanNode,
    "Return Integer": ReturnIntegerNode,
    "Return Float": ReturnFloatNode,
    "Return String": ReturnStringNode,
}

__all__ = ["NODE_CLASS_MAPPINGS"]