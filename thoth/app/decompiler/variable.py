from typing import Optional


class Variable:
    """
    Variable class
    """

    counter = 0

    def __init__(self, variable_name: Optional[str] = None) -> None:
        """
        Initialize a new variable
        """
        self.variable_name = variable_name
        self.is_set = False
        self.used_in_condition = False
        self.instance = Variable.counter if self.is_set else None

    def set(self) -> None:
        """
        A variable is set when it's accessed
        """
        self.is_set = True
        self.instance = Variable.counter
        Variable.counter += 1

    @property
    def name(self) -> str:
        """
        Return the variable name
        Either a custom name (function arguments/return value) or v_<n> by default
        """
        if not self.used_in_condition:
            self.used_in_condition = True

        if not self.is_set:
            self.set()

        # If the variable has a name
        if self.variable_name is not None:
            return self.variable_name

        # Use default name (v_<n>)
        name = "v_%s" % self.instance
        return name
