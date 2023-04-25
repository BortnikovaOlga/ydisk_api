import attr


@attr.s
class ResourcesResponse:
    href = attr.ib(default=None)
    method = attr.ib(default=None)
    templated = attr.ib(default=None)
