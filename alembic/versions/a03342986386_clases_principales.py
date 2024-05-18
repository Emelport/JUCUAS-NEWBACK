"""Clases Principales

Revision ID: a03342986386
Revises: 
Create Date: 2024-05-17 21:23:40.575500

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a03342986386'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deadline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_edition', sa.String(length=150), nullable=True),
    sa.Column('date_edition', sa.String(length=4), nullable=True),
    sa.Column('date_to_upload_activities', sa.Date(), nullable=True),
    sa.Column('date_to_upload_evidence', sa.Date(), nullable=True),
    sa.Column('date_to_validate_evidence', sa.Date(), nullable=True),
    sa.Column('date_edition_start', sa.Date(), nullable=True),
    sa.Column('end_date_of_the_edition', sa.Date(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('file', sa.Text(), nullable=True),
    sa.Column('file_name', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organizational_unit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('acronym', sa.String(length=10), nullable=True),
    sa.Column('key_code', sa.String(length=10), nullable=True),
    sa.Column('region', sa.Enum('N', 'CN', 'C', 'S'), nullable=True),
    sa.Column('municipality', sa.String(length=150), nullable=True),
    sa.Column('locality', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('title', sa.String(length=800), nullable=True),
    sa.Column('max_copresenter', sa.String(length=100), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_evidence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('type', sa.Enum('PDF', 'URL'), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('is_optional', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('university',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('acronym', sa.String(length=10), nullable=True),
    sa.Column('key_code', sa.String(length=10), nullable=True),
    sa.Column('type', sa.Enum('PREESC', 'PRIM', 'SEC', 'P', 'U'), nullable=True),
    sa.Column('region', sa.Enum('N', 'CN', 'C', 'S'), nullable=True),
    sa.Column('municipality', sa.String(length=150), nullable=True),
    sa.Column('locality', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.Enum('M', 'H', 'O', 'N'), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('activity_manager',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.Enum('M', 'H', 'O'), nullable=True),
    sa.Column('academic_degree', sa.Enum('L', 'M', 'D'), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('presenter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('gender', sa.Enum('M', 'H', 'O'), nullable=True),
    sa.Column('curp', sa.String(length=18), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.Column('academic_degree', sa.String(length=50), nullable=True),
    sa.Column('origin_university_id', sa.Integer(), nullable=True),
    sa.Column('origin_organizational_unit_id', sa.Integer(), nullable=True),
    sa.Column('if_belong_to_school', sa.Boolean(), nullable=True),
    sa.Column('position_institution', sa.Enum('1', '2', '3', '4', '5'), nullable=True),
    sa.Column('birth_date', sa.DateTime(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['origin_organizational_unit_id'], ['organizational_unit.id'], ),
    sa.ForeignKeyConstraint(['origin_university_id'], ['university.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('representative',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('origin_university_id', sa.Integer(), nullable=True),
    sa.Column('origin_organizational_unit_id', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['origin_organizational_unit_id'], ['organizational_unit.id'], ),
    sa.ForeignKeyConstraint(['origin_university_id'], ['university.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviewer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('user_name', sa.String(length=50), nullable=True),
    sa.Column('region', sa.Enum('N', 'CN', 'C', 'S'), nullable=True),
    sa.Column('global_reviewer', sa.Boolean(), nullable=True),
    sa.Column('origin_university_id', sa.Integer(), nullable=True),
    sa.Column('origin_highschool_id', sa.Integer(), nullable=True),
    sa.Column('origin_organizational_unit_id', sa.Integer(), nullable=True),
    sa.Column('reviewer_permission', sa.String(length=10), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['origin_highschool_id'], ['university.id'], ),
    sa.ForeignKeyConstraint(['origin_organizational_unit_id'], ['organizational_unit.id'], ),
    sa.ForeignKeyConstraint(['origin_university_id'], ['university.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('type_activity_type_evidence',
    sa.Column('type_activity_id', sa.Integer(), nullable=True),
    sa.Column('type_evidence_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['type_activity_id'], ['type_activity.id'], ),
    sa.ForeignKeyConstraint(['type_evidence_id'], ['type_evidence.id'], )
    )
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('numbers_expected_attendees', sa.Integer(), nullable=True),
    sa.Column('numbers_total_attendees', sa.Integer(), nullable=True),
    sa.Column('modality', sa.Enum('V', 'P'), nullable=True),
    sa.Column('edition_id', sa.Integer(), nullable=True),
    sa.Column('date_activity', sa.DateTime(), nullable=True),
    sa.Column('educational_level_to_is_directed', sa.Enum('PCO', 'PREESC', 'PRIM', 'SEC', 'MDSUP', 'SUP'), nullable=True),
    sa.Column('type_of_public', sa.Enum('INT', 'EXT'), nullable=True),
    sa.Column('area_knowledge', sa.Enum('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'), nullable=True),
    sa.Column('presenter_id', sa.Integer(), nullable=True),
    sa.Column('type_id', sa.Integer(), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('certificate_file', sa.String(length=255), nullable=True),
    sa.Column('activity_status', sa.Enum('DUE', 'INC', 'REJECT', 'OK'), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['edition_id'], ['deadline.id'], ),
    sa.ForeignKeyConstraint(['presenter_id'], ['presenter.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['type_activity.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activity_co_presenter',
    sa.Column('activity_id', sa.Integer(), nullable=False),
    sa.Column('co_presenter_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ),
    sa.ForeignKeyConstraint(['co_presenter_id'], ['presenter.id'], ),
    sa.PrimaryKeyConstraint('activity_id', 'co_presenter_id')
    )
    op.create_table('evidence',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.Column('observation', sa.String(length=1500), nullable=True),
    sa.Column('evidence_file', sa.String(length=255), nullable=True),
    sa.Column('evidence_status', sa.Enum('SEND', 'DUE', 'INC', 'REJECT', 'OK'), nullable=True),
    sa.Column('created_by_id', sa.Integer(), nullable=True),
    sa.Column('status_changed_by_id', sa.Integer(), nullable=True),
    sa.Column('type_evidence_id', sa.Integer(), nullable=True),
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ),
    sa.ForeignKeyConstraint(['created_by_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['status_changed_by_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['type_evidence_id'], ['type_evidence.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('evidence')
    op.drop_table('activity_co_presenter')
    op.drop_table('activity')
    op.drop_table('type_activity_type_evidence')
    op.drop_table('reviewer')
    op.drop_table('representative')
    op.drop_table('presenter')
    op.drop_table('activity_manager')
    op.drop_table('user')
    op.drop_table('university')
    op.drop_table('type_evidence')
    op.drop_table('type_activity')
    op.drop_table('organizational_unit')
    op.drop_table('deadline')
    # ### end Alembic commands ###
