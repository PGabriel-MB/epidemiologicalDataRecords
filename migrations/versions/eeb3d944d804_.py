"""empty message

Revision ID: eeb3d944d804
Revises: bf58d4392aa3
Create Date: 2020-12-05 20:53:26.384740

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'eeb3d944d804'
down_revision = 'bf58d4392aa3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dado_epidemiologico', 'doenca_associada_id',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('dado_epidemiologico', 'doenca_associada_id',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###