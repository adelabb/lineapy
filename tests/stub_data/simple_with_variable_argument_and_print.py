from lineapy.data.graph import Graph
from tests.util import get_new_id
from lineapy.data.types import ArgumentNode, CallNode, DirectedEdge

from tests.stub_data.simple_graph import line_1, line_1_id, session, arg_literal

"""
```
a = abs(-11)
b = min(a, 10)
print(b)
```
"""

arg_a_id = get_new_id()
arg_10_id = get_new_id()

arg_a = ArgumentNode(
    id=arg_a_id, session_id=session.uuid, positional_order=1, value_node_id=line_1_id
)

arg_10 = ArgumentNode(
    id=arg_10_id, session_id=session.uuid, positional_order=2, value_literal=10
)

line_2_id = get_new_id()
line_2 = CallNode(
    id=line_2_id,
    session_id=session.uuid,
    code="min(a, 10)",
    function_name="min",
    assigned_variable_name="b",
    arguments=[arg_a_id, arg_10_id],
)

e2 = DirectedEdge(source_node_id=line_1_id, sink_node_id=line_2_id)

arg_b_id = get_new_id()

arg_b = ArgumentNode(
    id=arg_b_id, session_id=session.uuid, positional_order=1, value_node_id=line_2_id
)

line_3_id = get_new_id()
line_3 = CallNode(
    id=line_3_id,
    session_id=session.uuid,
    code="print(b)",
    function_name="print",
    arguments=[arg_b_id],
)

e3 = DirectedEdge(source_node_id=line_2_id, sink_node_id=line_3_id)

simple_with_variable_argument_and_print = Graph(
    [arg_a, arg_10, arg_b, arg_literal, line_1, line_2, line_3], [e2, e3]
)