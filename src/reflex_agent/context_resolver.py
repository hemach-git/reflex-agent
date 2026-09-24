class ContextResolver:
    """
    Resolves contextual references such as 'that'
    using the agent's current context.
    """

    def __init__(self, context):
        self.context = context

    def has_previous_result(self) -> bool:
        """Return True when a previous result is available."""

        return self.context.last_result is not None

    def resolve_reference(self, reference: str):
        """
        Resolve a contextual reference to a previous value.
        """

        if reference.lower().strip() == "that":
            if not self.has_previous_result():
                raise ValueError(
                    "I don't have a previous result to use."
                )

            return self.context.last_result

        raise ValueError(
            f"I don't know how to resolve '{reference}'."
        )
