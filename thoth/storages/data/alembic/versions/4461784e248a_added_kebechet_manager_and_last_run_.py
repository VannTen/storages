"""Added kebechet manager and last run columns

Revision ID: 4461784e248a
Revises: b9f960cdd223
Create Date: 2020-09-29 18:08:42.771601+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4461784e248a'
down_revision = 'b9f960cdd223'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kebechet_github_installations', sa.Column('info_manager', sa.Boolean(), server_default='false', nullable=False))
    op.add_column('kebechet_github_installations', sa.Column('last_run', sa.DateTime(), nullable=True))
    op.add_column('kebechet_github_installations', sa.Column('pipfile_requirements_manager', sa.Boolean(), server_default='false', nullable=False))
    op.add_column('kebechet_github_installations', sa.Column('thoth_advise_manager', sa.Boolean(), server_default='false', nullable=False))
    op.add_column('kebechet_github_installations', sa.Column('thoth_provenance_manager', sa.Boolean(), server_default='false', nullable=False))
    op.add_column('kebechet_github_installations', sa.Column('update_manager', sa.Boolean(), server_default='false', nullable=False))
    op.add_column('kebechet_github_installations', sa.Column('version_manager', sa.Boolean(), server_default='false', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kebechet_github_installations', 'version_manager')
    op.drop_column('kebechet_github_installations', 'update_manager')
    op.drop_column('kebechet_github_installations', 'thoth_provenance_manager')
    op.drop_column('kebechet_github_installations', 'thoth_advise_manager')
    op.drop_column('kebechet_github_installations', 'pipfile_requirements_manager')
    op.drop_column('kebechet_github_installations', 'last_run')
    op.drop_column('kebechet_github_installations', 'info_manager')
    # ### end Alembic commands ###
