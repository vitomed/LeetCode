import asyncio
import typer

from app.models import init_models, drop_all_tables
from app.utils import get_logger

cli = typer.Typer()
logger = get_logger(__name__)


@cli.command()
def db_drop_all():
    asyncio.run(drop_all_tables())
    logger.info("Done")


@cli.command()
def db_init_models():
    asyncio.run(init_models())
    logger.info("Done")


if __name__ == "__main__":
    cli()
