from lineapy.data.graph import Graph
from lineapy.data.types import (
    LiteralNode,
    VariableNode,
)
from tests.util import get_new_id, get_new_session

"""
```
a = 0
b = a
a = 2
```

TODO: in our slicing test, we should make sure that getting
      the slice for b returns.

```
a = 0
b = a
```
"""

code = """a = 0
b = a
a = 2
"""

session = get_new_session(code)

a_assign = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    assigned_variable_name="a",
    value=0,
    lineno=1,
    col_offset=0,
    end_lineno=1,
    end_col_offset=5,
)

b_assign = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    assigned_variable_name="b",
    source_variable_id=a_assign.id,
    lineno=2,
    col_offset=0,
    end_lineno=2,
    end_col_offset=5,
)

a_mutate = LiteralNode(
    id=get_new_id(),
    session_id=session.id,
    assigned_variable_name="a",
    value=2,
    lineno=3,
    col_offset=0,
    end_lineno=3,
    end_col_offset=5,
)

graph_with_alias_by_value = Graph([a_assign, b_assign, a_mutate], session)
