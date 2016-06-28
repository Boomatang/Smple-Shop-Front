"""empty message

Revision ID: d71bc2f1f802
Revises: None
Create Date: 2016-06-28 21:30:53.853498

"""

# revision identifiers, used by Alembic.
revision = 'd71bc2f1f802'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('emial', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('signup_date', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('roles')
    ### end Alembic commands ###
