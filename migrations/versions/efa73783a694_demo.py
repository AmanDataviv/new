"""Demo

Revision ID: efa73783a694
Revises: 
Create Date: 2025-03-11 11:15:00.647667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'efa73783a694'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("books-author",
                    sa.Column('Todays Date',sa.DateTime))


def downgrade() -> None:
    pass
