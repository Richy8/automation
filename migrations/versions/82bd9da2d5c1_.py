"""empty message

Revision ID: 82bd9da2d5c1
Revises: 64230b51cad3
Create Date: 2019-08-04 22:52:39.953024

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '82bd9da2d5c1'
down_revision = '64230b51cad3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('salesone',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('opening', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('bank', sa.Integer(), nullable=True),
    sa.Column('cash', sa.Integer(), nullable=True),
    sa.Column('credit', sa.Integer(), nullable=True),
    sa.Column('outstanding', sa.Integer(), nullable=True),
    sa.Column('closing', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('salesoneitems',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('category', sa.String(length=50), nullable=True),
    sa.Column('salesone_id', sa.Integer(), nullable=True),
    sa.Column('sales_type', sa.String(length=50), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['salesone_id'], ['salesone.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('eggsales')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eggsales',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('customer_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('requested', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('size', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('cost', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('bank', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('cash', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('debit', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('credit', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('pen_allocation', mysql.TEXT(), nullable=True),
    sa.Column('comment', mysql.TEXT(), nullable=True),
    sa.Column('issued', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='eggsales_ibfk_1', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('salesoneitems')
    op.drop_table('salesone')
    # ### end Alembic commands ###
