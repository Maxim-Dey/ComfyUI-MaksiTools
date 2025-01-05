from .nodes.Time_Measure_Node import Time_Measure_Node
from .nodes.Datatype_Nodes import ReturnBooleanNode, ReturnIntegerNode, ReturnFloatNode, ReturnMultilineStringNode

NODE_CLASS_MAPPINGS = {
    "🔧 Time Measure Node": Time_Measure_Node,
    "🔢 Return Boolean": ReturnBooleanNode,
    "🔢 Return Integer": ReturnIntegerNode,
    "🔢 Return Float": ReturnFloatNode,
    "🔢 Return Multiline String": ReturnMultilineStringNode,
}

__all__ = ["NODE_CLASS_MAPPINGS"]