"""add lasr few columns to posts table

Revision ID: e8ecf78ce854
Revises: ea4c382ab3ec
Create Date: 2026-05-25 12:17:14.002715

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8ecf78ce854'
down_revision: Union[str, Sequence[str], None] = 'ea4c382ab3ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE' ),)
    op.add_column('posts',sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True),nullable=False, server_default=sa.text('NOW()') ),)
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
