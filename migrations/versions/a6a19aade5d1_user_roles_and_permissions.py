"""User Roles and Permissions

Revision ID: a6a19aade5d1
Revises: 56372de9bdd7
Create Date: 2016-04-23 19:00:35.944588

"""

# revision identifiers, used by Alembic.
revision = 'a6a19aade5d1'
down_revision = '56372de9bdd7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('default', sa.Boolean(), nullable=True))
    op.add_column('roles', sa.Column('permissions', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_column('roles', 'permissions')
    op.drop_column('roles', 'default')
    ### end Alembic commands ###