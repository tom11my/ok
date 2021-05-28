"""Add export token system

Revision ID: fb49c4643d00
Revises: 9bc6f244678d
Create Date: 2021-05-27 19:03:26.637151

"""

# revision identifiers, used by Alembic.
revision = 'fb49c4643d00'
down_revision = '9bc6f244678d'

from alembic import op
import sqlalchemy as sa
import server


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('export_access_token', sa.String(length=255), nullable=True, default=""))
    op.add_column('course', sa.Column('export_access_token_active', sa.Boolean(), nullable=False, default=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('course', 'export_access_token_active')
    op.drop_column('course', 'export_access_token')
    # ### end Alembic commands ###