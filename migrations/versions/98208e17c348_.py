"""empty message

Revision ID: 98208e17c348
Revises: None
Create Date: 2016-02-06 00:55:27.111851

"""

# revision identifiers, used by Alembic.
revision = '98208e17c348'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('arduino',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('ip_address', sa.String(length=15), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('ip_address')
    )
    op.create_table('data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('luminosity', sa.Integer(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.Column('bustling', sa.Boolean(), nullable=True),
    sa.Column('date_log', sa.DateTime(), nullable=True),
    sa.Column('arduino_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['arduino_id'], ['arduino.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data')
    op.drop_table('arduino')
    ### end Alembic commands ###
