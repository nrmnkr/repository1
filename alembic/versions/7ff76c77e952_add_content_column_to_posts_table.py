"""add content column to posts table

Revision ID: 7ff76c77e952
Revises: f5e56a6102e9
Create Date: 2026-05-25 11:41:26.601161

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ff76c77e952'
down_revision: Union[str, Sequence[str], None] = 'f5e56a6102e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
