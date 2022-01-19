"""Introduce Thoth specific entries found in the container image

Revision ID: b957aa9cce3e
Revises: 91620576525b
Create Date: 2021-01-28 06:59:01.137118+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b957aa9cce3e"
down_revision = "91620576525b"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("package_extract_run", sa.Column("thoth_image_name", sa.Text(), nullable=True))
    op.add_column("package_extract_run", sa.Column("thoth_image_version", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("package_extract_run", "thoth_image_version")
    op.drop_column("package_extract_run", "thoth_image_name")
    # ### end Alembic commands ###
