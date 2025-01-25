"""Generated client library for file version v1p1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.file.v1p1alpha1 import file_v1p1alpha1_messages as messages


class FileV1p1alpha1(base_api.BaseApiClient):
  """Generated client library for service file version v1p1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://file.googleapis.com/'
  MTLS_BASE_URL = 'https://file.mtls.googleapis.com/'

  _PACKAGE = 'file'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1p1alpha1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'FileV1p1alpha1'
  _URL_VERSION = 'v1p1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new file handle."""
    url = url or self.BASE_URL
    super(FileV1p1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_backups = self.ProjectsLocationsBackupsService(self)
    self.projects_locations_instances = self.ProjectsLocationsInstancesService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_snapshots = self.ProjectsLocationsSnapshotsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsBackupsService(base_api.BaseApiService):
    """Service class for the projects_locations_backups resource."""

    _NAME = 'projects_locations_backups'

    def __init__(self, client):
      super(FileV1p1alpha1.ProjectsLocationsBackupsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a backup.

      Args:
        request: (FileProjectsLocationsBackupsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/backups',
        http_method='POST',
        method_id='file.projects.locations.backups.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['backupId'],
        relative_path='v1p1alpha1/{+parent}/backups',
        request_field='backup',
        request_type_name='FileProjectsLocationsBackupsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a backup.

      Args:
        request: (FileProjectsLocationsBackupsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/backups/{backupsId}',
        http_method='DELETE',
        method_id='file.projects.locations.backups.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}',
        request_field='',
        request_type_name='FileProjectsLocationsBackupsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the details of a specific backup.

      Args:
        request: (FileProjectsLocationsBackupsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Backup) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/backups/{backupsId}',
        http_method='GET',
        method_id='file.projects.locations.backups.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}',
        request_field='',
        request_type_name='FileProjectsLocationsBackupsGetRequest',
        response_type_name='Backup',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all backups in a project for either a specified location or for all locations.

      Args:
        request: (FileProjectsLocationsBackupsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListBackupsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/backups',
        http_method='GET',
        method_id='file.projects.locations.backups.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1p1alpha1/{+parent}/backups',
        request_field='',
        request_type_name='FileProjectsLocationsBackupsListRequest',
        response_type_name='ListBackupsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the settings of a specific backup.

      Args:
        request: (FileProjectsLocationsBackupsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/backups/{backupsId}',
        http_method='PATCH',
        method_id='file.projects.locations.backups.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1p1alpha1/{+name}',
        request_field='backup',
        request_type_name='FileProjectsLocationsBackupsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsInstancesService(base_api.BaseApiService):
    """Service class for the projects_locations_instances resource."""

    _NAME = 'projects_locations_instances'

    def __init__(self, client):
      super(FileV1p1alpha1.ProjectsLocationsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def CopyInstance(self, request, global_params=None):
      r"""Copies the fileshare content of a Basic instance to a High Scale or Enterprise tier instance. If the source instance is being written to during the copy, the copy will not be a consistent snapshot of the fileshare. If the target instance already has files, these files will be overwritten if the source instance has the same file but with different checksum values. Files that exist in the target but not in the source will be deleted. Hard links are copied as separate files. POSIX ACLs are not copied. The source and target instances must be on the same VPC and using the same `connect_mode`.

      Args:
        request: (FileProjectsLocationsInstancesCopyInstanceRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('CopyInstance')
      return self._RunMethod(
          config, request, global_params=global_params)

    CopyInstance.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:copyInstance',
        http_method='POST',
        method_id='file.projects.locations.instances.copyInstance',
        ordered_params=['targetInstance'],
        path_params=['targetInstance'],
        query_params=[],
        relative_path='v1p1alpha1/{+targetInstance}:copyInstance',
        request_field='copyInstanceRequest',
        request_type_name='FileProjectsLocationsInstancesCopyInstanceRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Creates an instance. When creating from a snapshot or backup, the capacity of the new instance needs to be equal to or larger than the capacity of the snapshot or backup (and also equal to or larger than the minimum capacity of the tier).

      Args:
        request: (FileProjectsLocationsInstancesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/instances',
        http_method='POST',
        method_id='file.projects.locations.instances.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['instanceId'],
        relative_path='v1p1alpha1/{+parent}/instances',
        request_field='instance',
        request_type_name='FileProjectsLocationsInstancesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes an instance.

      Args:
        request: (FileProjectsLocationsInstancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='DELETE',
        method_id='file.projects.locations.instances.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}',
        request_field='',
        request_type_name='FileProjectsLocationsInstancesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the details of a specific instance.

      Args:
        request: (FileProjectsLocationsInstancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Instance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='GET',
        method_id='file.projects.locations.instances.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}',
        request_field='',
        request_type_name='FileProjectsLocationsInstancesGetRequest',
        response_type_name='Instance',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all instances in a project for either a specified location or for all locations.

      Args:
        request: (FileProjectsLocationsInstancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListInstancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/instances',
        http_method='GET',
        method_id='file.projects.locations.instances.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1p1alpha1/{+parent}/instances',
        request_field='',
        request_type_name='FileProjectsLocationsInstancesListRequest',
        response_type_name='ListInstancesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the settings of a specific instance.

      Args:
        request: (FileProjectsLocationsInstancesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='PATCH',
        method_id='file.projects.locations.instances.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1p1alpha1/{+name}',
        request_field='instance',
        request_type_name='FileProjectsLocationsInstancesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Restore(self, request, global_params=None):
      r"""Restores an existing instance's file share from a snapshot or backup. The capacity of the instance needs to be equal to or larger than the capacity of the snapshot or backup (and also equal to or larger than the minimum capacity of the tier).

      Args:
        request: (FileProjectsLocationsInstancesRestoreRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Restore')
      return self._RunMethod(
          config, request, global_params=global_params)

    Restore.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:restore',
        http_method='POST',
        method_id='file.projects.locations.instances.restore',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}:restore',
        request_field='restoreInstanceRequest',
        request_type_name='FileProjectsLocationsInstancesRestoreRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(FileV1p1alpha1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

      Args:
        request: (FileProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='file.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='FileProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (FileProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='file.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}',
        request_field='',
        request_type_name='FileProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (FileProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='file.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}',
        request_field='',
        request_type_name='FileProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (FileProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='file.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1p1alpha1/{+name}/operations',
        request_field='',
        request_type_name='FileProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsSnapshotsService(base_api.BaseApiService):
    """Service class for the projects_locations_snapshots resource."""

    _NAME = 'projects_locations_snapshots'

    def __init__(self, client):
      super(FileV1p1alpha1.ProjectsLocationsSnapshotsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a snapshot.

      Args:
        request: (FileProjectsLocationsSnapshotsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/snapshots',
        http_method='POST',
        method_id='file.projects.locations.snapshots.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['snapshotId'],
        relative_path='v1p1alpha1/{+parent}/snapshots',
        request_field='snapshot',
        request_type_name='FileProjectsLocationsSnapshotsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a snapshot.

      Args:
        request: (FileProjectsLocationsSnapshotsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/snapshots/{snapshotsId}',
        http_method='DELETE',
        method_id='file.projects.locations.snapshots.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}',
        request_field='',
        request_type_name='FileProjectsLocationsSnapshotsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the details of a specific snapshot.

      Args:
        request: (FileProjectsLocationsSnapshotsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Snapshot) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/snapshots/{snapshotsId}',
        http_method='GET',
        method_id='file.projects.locations.snapshots.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}',
        request_field='',
        request_type_name='FileProjectsLocationsSnapshotsGetRequest',
        response_type_name='Snapshot',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists all snapshots in a project for either a specified location or for all locations.

      Args:
        request: (FileProjectsLocationsSnapshotsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListSnapshotsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/snapshots',
        http_method='GET',
        method_id='file.projects.locations.snapshots.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1p1alpha1/{+parent}/snapshots',
        request_field='',
        request_type_name='FileProjectsLocationsSnapshotsListRequest',
        response_type_name='ListSnapshotsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the settings of a specific snapshot.

      Args:
        request: (FileProjectsLocationsSnapshotsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}/snapshots/{snapshotsId}',
        http_method='PATCH',
        method_id='file.projects.locations.snapshots.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1p1alpha1/{+name}',
        request_field='snapshot',
        request_type_name='FileProjectsLocationsSnapshotsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(FileV1p1alpha1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (FileProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='file.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1p1alpha1/{+name}',
        request_field='',
        request_type_name='FileProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (FileProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1p1alpha1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='file.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'includeUnrevealedLocations', 'pageSize', 'pageToken'],
        relative_path='v1p1alpha1/{+name}/locations',
        request_field='',
        request_type_name='FileProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(FileV1p1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
