"""Generated client library for testing version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.testing.v1 import testing_v1_messages as messages


class TestingV1(base_api.BaseApiClient):
  """Generated client library for service testing version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://testing.googleapis.com/'
  MTLS_BASE_URL = 'https://testing.mtls.googleapis.com/'

  _PACKAGE = 'testing'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/cloud-platform.read-only']
  _VERSION = 'v1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'TestingV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new testing handle."""
    url = url or self.BASE_URL
    super(TestingV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.applicationDetailService = self.ApplicationDetailServiceService(self)
    self.projects_deviceSessions = self.ProjectsDeviceSessionsService(self)
    self.projects_testMatrices = self.ProjectsTestMatricesService(self)
    self.projects = self.ProjectsService(self)
    self.testEnvironmentCatalog = self.TestEnvironmentCatalogService(self)

  class ApplicationDetailServiceService(base_api.BaseApiService):
    """Service class for the applicationDetailService resource."""

    _NAME = 'applicationDetailService'

    def __init__(self, client):
      super(TestingV1.ApplicationDetailServiceService, self).__init__(client)
      self._upload_configs = {
          }

    def GetApkDetails(self, request, global_params=None):
      r"""Gets the details of an Android application APK.

      Args:
        request: (TestingApplicationDetailServiceGetApkDetailsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GetApkDetailsResponse) The response message.
      """
      config = self.GetMethodConfig('GetApkDetails')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetApkDetails.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='testing.applicationDetailService.getApkDetails',
        ordered_params=[],
        path_params=[],
        query_params=['bundleLocation_gcsPath'],
        relative_path='v1/applicationDetailService/getApkDetails',
        request_field='fileReference',
        request_type_name='TestingApplicationDetailServiceGetApkDetailsRequest',
        response_type_name='GetApkDetailsResponse',
        supports_download=False,
    )

  class ProjectsDeviceSessionsService(base_api.BaseApiService):
    """Service class for the projects_deviceSessions resource."""

    _NAME = 'projects_deviceSessions'

    def __init__(self, client):
      super(TestingV1.ProjectsDeviceSessionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""POST /v1/projects/{project_id}/deviceSessions/{device_session_id}:cancel Changes the DeviceSession to state FINISHED and terminates all connections. Canceled sessions are not deleted and can be retrieved or listed by the user until they expire based on the 28 day deletion policy.

      Args:
        request: (TestingProjectsDeviceSessionsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/deviceSessions/{deviceSessionsId}:cancel',
        http_method='POST',
        method_id='testing.projects.deviceSessions.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelDeviceSessionRequest',
        request_type_name='TestingProjectsDeviceSessionsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""POST /v1/projects/{project_id}/deviceSessions.

      Args:
        request: (TestingProjectsDeviceSessionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeviceSession) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/deviceSessions',
        http_method='POST',
        method_id='testing.projects.deviceSessions.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/deviceSessions',
        request_field='deviceSession',
        request_type_name='TestingProjectsDeviceSessionsCreateRequest',
        response_type_name='DeviceSession',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""GET /v1/projects/{project_id}/deviceSessions/{device_session_id} Return a DeviceSession, which documents the allocation status and whether the device is allocated. Clients making requests from this API must poll GetDeviceSession.

      Args:
        request: (TestingProjectsDeviceSessionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeviceSession) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/deviceSessions/{deviceSessionsId}',
        http_method='GET',
        method_id='testing.projects.deviceSessions.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='TestingProjectsDeviceSessionsGetRequest',
        response_type_name='DeviceSession',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""GET /v1/projects/{project_id}/deviceSessions Lists device Sessions owned by the project user.

      Args:
        request: (TestingProjectsDeviceSessionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListDeviceSessionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/deviceSessions',
        http_method='GET',
        method_id='testing.projects.deviceSessions.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/deviceSessions',
        request_field='',
        request_type_name='TestingProjectsDeviceSessionsListRequest',
        response_type_name='ListDeviceSessionsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""PATCH /v1/projects/{projectId}/deviceSessions/deviceSessionId}:updateDeviceSession Updates the current device session to the fields described by the update_mask.

      Args:
        request: (TestingProjectsDeviceSessionsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DeviceSession) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/deviceSessions/{deviceSessionsId}',
        http_method='PATCH',
        method_id='testing.projects.deviceSessions.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='deviceSession',
        request_type_name='TestingProjectsDeviceSessionsPatchRequest',
        response_type_name='DeviceSession',
        supports_download=False,
    )

  class ProjectsTestMatricesService(base_api.BaseApiService):
    """Service class for the projects_testMatrices resource."""

    _NAME = 'projects_testMatrices'

    def __init__(self, client):
      super(TestingV1.ProjectsTestMatricesService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Cancels unfinished test executions in a test matrix. This call returns immediately and cancellation proceeds asynchronously. If the matrix is already final, this operation will have no effect. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Test Matrix does not exist.

      Args:
        request: (TestingProjectsTestMatricesCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CancelTestMatrixResponse) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='testing.projects.testMatrices.cancel',
        ordered_params=['projectId', 'testMatrixId'],
        path_params=['projectId', 'testMatrixId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/testMatrices/{testMatrixId}:cancel',
        request_field='',
        request_type_name='TestingProjectsTestMatricesCancelRequest',
        response_type_name='CancelTestMatrixResponse',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Creates and runs a matrix of tests according to the given specifications. Unsupported environments will be returned in the state UNSUPPORTED. A test matrix is limited to use at most 2000 devices in parallel. The returned matrix will not yet contain the executions that will be created for this matrix. Execution creation happens later on and will require a call to GetTestMatrix. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed or if the matrix tries to use too many simultaneous devices.

      Args:
        request: (TestingProjectsTestMatricesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestMatrix) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='testing.projects.testMatrices.create',
        ordered_params=['projectId'],
        path_params=['projectId'],
        query_params=['requestId'],
        relative_path='v1/projects/{projectId}/testMatrices',
        request_field='testMatrix',
        request_type_name='TestingProjectsTestMatricesCreateRequest',
        response_type_name='TestMatrix',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Checks the status of a test matrix and the executions once they are created. The test matrix will contain the list of test executions to run if and only if the resultStorage.toolResultsExecution fields have been populated. Note: Flaky test executions may be added to the matrix at a later stage. May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Test Matrix does not exist.

      Args:
        request: (TestingProjectsTestMatricesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestMatrix) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='testing.projects.testMatrices.get',
        ordered_params=['projectId', 'testMatrixId'],
        path_params=['projectId', 'testMatrixId'],
        query_params=[],
        relative_path='v1/projects/{projectId}/testMatrices/{testMatrixId}',
        request_field='',
        request_type_name='TestingProjectsTestMatricesGetRequest',
        response_type_name='TestMatrix',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(TestingV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

  class TestEnvironmentCatalogService(base_api.BaseApiService):
    """Service class for the testEnvironmentCatalog resource."""

    _NAME = 'testEnvironmentCatalog'

    def __init__(self, client):
      super(TestingV1.TestEnvironmentCatalogService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the catalog of supported test environments. May return any of the following canonical error codes: - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the environment type does not exist - INTERNAL - if an internal error occurred.

      Args:
        request: (TestingTestEnvironmentCatalogGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestEnvironmentCatalog) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='testing.testEnvironmentCatalog.get',
        ordered_params=['environmentType'],
        path_params=['environmentType'],
        query_params=['projectId'],
        relative_path='v1/testEnvironmentCatalog/{environmentType}',
        request_field='',
        request_type_name='TestingTestEnvironmentCatalogGetRequest',
        response_type_name='TestEnvironmentCatalog',
        supports_download=False,
    )
