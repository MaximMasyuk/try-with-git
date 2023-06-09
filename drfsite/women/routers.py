from rest_framework import routers


class MyCastomRouter(routers.SimpleRouter):  # this is roter
    routes = [
        routers.Route(
            url=r"^{prefix}/$",
            mapping={"get": "list"},
            name="{basename}-list",
            detail=False,
            initkwargs={"suffix": "List"},  # jsfhbgb
        ),
        routers.Route(
            url=r"^{prefix}/{lookup}/$",
            mapping={"get": "retrieve"},
            name="{basename}-detail",
            detail=True,
            initkwargs={"suffix": "Detail"},
        ),
    ]
