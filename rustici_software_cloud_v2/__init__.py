# coding: utf-8

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.

    OpenAPI spec version: 2.0 beta
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.activity_result_schema import ActivityResultSchema
from .models.application_list_schema import ApplicationListSchema
from .models.application_schema import ApplicationSchema
from .models.application_token import ApplicationToken
from .models.batch_tags_schema import BatchTagsSchema
from .models.comment_schema import CommentSchema
from .models.completion_amount_schema import CompletionAmountSchema
from .models.course_activity_schema import CourseActivitySchema
from .models.course_list_non_paged_schema import CourseListNonPagedSchema
from .models.course_list_schema import CourseListSchema
from .models.course_reference_schema import CourseReferenceSchema
from .models.course_schema import CourseSchema
from .models.create_registration_schema import CreateRegistrationSchema
from .models.credential_created_schema import CredentialCreatedSchema
from .models.credential_list_schema import CredentialListSchema
from .models.credential_request_schema import CredentialRequestSchema
from .models.credential_schema import CredentialSchema
from .models.import_fetch_request_schema import ImportFetchRequestSchema
from .models.import_job_result_schema import ImportJobResultSchema
from .models.import_result_schema import ImportResultSchema
from .models.integer_result_schema import IntegerResultSchema
from .models.item_value_pair_schema import ItemValuePairSchema
from .models.launch_history_list_schema import LaunchHistoryListSchema
from .models.launch_history_schema import LaunchHistorySchema
from .models.launch_link_request_schema import LaunchLinkRequestSchema
from .models.launch_link_schema import LaunchLinkSchema
from .models.learner_preference_schema import LearnerPreferenceSchema
from .models.learner_schema import LearnerSchema
from .models.message_schema import MessageSchema
from .models.metadata_schema import MetadataSchema
from .models.objective_schema import ObjectiveSchema
from .models.permissions_schema import PermissionsSchema
from .models.ping_schema import PingSchema
from .models.post_back_schema import PostBackSchema
from .models.registration_completion import RegistrationCompletion
from .models.registration_list_schema import RegistrationListSchema
from .models.registration_schema import RegistrationSchema
from .models.registration_success import RegistrationSuccess
from .models.response_error import ResponseError
from .models.runtime_interaction_schema import RuntimeInteractionSchema
from .models.runtime_objective_schema import RuntimeObjectiveSchema
from .models.runtime_schema import RuntimeSchema
from .models.score_schema import ScoreSchema
from .models.setting_item import SettingItem
from .models.setting_list_schema import SettingListSchema
from .models.setting_metadata import SettingMetadata
from .models.setting_valid_value import SettingValidValue
from .models.settings_individual_schema import SettingsIndividualSchema
from .models.settings_post_schema import SettingsPostSchema
from .models.shared_data_entry_schema import SharedDataEntrySchema
from .models.static_properties_schema import StaticPropertiesSchema
from .models.string_result_schema import StringResultSchema
from .models.tag_list_schema import TagListSchema
from .models.title_schema import TitleSchema
from .models.token_request_schema import TokenRequestSchema
from .models.xapi_account import XapiAccount
from .models.xapi_activity import XapiActivity
from .models.xapi_activity_definition import XapiActivityDefinition
from .models.xapi_agent_group import XapiAgentGroup
from .models.xapi_attachment import XapiAttachment
from .models.xapi_context import XapiContext
from .models.xapi_context_activity import XapiContextActivity
from .models.xapi_interaction_component import XapiInteractionComponent
from .models.xapi_result import XapiResult
from .models.xapi_score import XapiScore
from .models.xapi_statement import XapiStatement
from .models.xapi_statement_reference import XapiStatementReference
from .models.xapi_statement_result import XapiStatementResult
from .models.xapi_verb import XapiVerb

# import apis into sdk package
from .apis.application_management_api import ApplicationManagementApi
from .apis.authentication_api import AuthenticationApi
from .apis.course_api import CourseApi
from .apis.ping_api import PingApi
from .apis.registration_api import RegistrationApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
