"""Containers module."""

from dependency_injector import containers, providers

from .database import Database
from .Controller.repositories import UserRepository, AdminRepository
from .Controller.services import UserService, AdminService

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".View.Endpoint_Admin.endpointAdmin",".View.Endpoint_Status.endpointStatus",".View.Endpoint_User.endpointUser"])

    config = providers.Configuration(yaml_files=["config.yml"])

    db = providers.Singleton(Database, db_url=config.db.url)

    user_repository = providers.Factory(
        UserRepository,
        session_factory=db.provided.session,
    )

    user_service = providers.Factory(
        UserService,
        user_repository=user_repository,
    )
    
    admin_repository = providers.Factory(
        AdminRepository,
        session_factory=db.provided.session,
    )

    admin_service = providers.Factory(
        AdminService,
        admin_repository=admin_repository,
    )
