"""Adding new table

Revision ID: 97ce61b7c07b
Revises: a2bbc5808fd5
Create Date: 2025-03-11 11:30:06.960583

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97ce61b7c07b'
down_revision: Union[str, None] = 'f6d8d9da9d2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("New_table",
                    sa.Column("id",sa.Integer,primary_key=True),
                    sa.Column("description",sa.String(20)))
    


def downgrade() -> None:
    pass
