"""Removed async status field

Revision ID: 00c26d2953fb
Revises: 401a786ee015
Create Date: 2019-06-16 06:24:27.649443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00c26d2953fb'
down_revision = '401a786ee015'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_async_task_task_status', table_name='async_task')
    op.drop_column('async_task', 'task_status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('async_task', sa.Column('task_status', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_index('ix_async_task_task_status', 'async_task', ['task_status'], unique=False)
    # ### end Alembic commands ###
