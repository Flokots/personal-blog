"""add pass_secure column

Revision ID: 489ee966623b
Revises: b33ae170e705
Create Date: 2022-05-16 09:36:26.281391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '489ee966623b'
down_revision = 'b33ae170e705'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'pass_secure')
    # ### end Alembic commands ###
