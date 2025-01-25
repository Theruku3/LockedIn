"""Generated client library for edgecontainer version v1beta."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.edgecontainer.v1beta import edgecontainer_v1beta_messages as messages


class EdgecontainerV1beta(base_api.BaseApiClient):
  """Generated client library for service edgecontainer version v1beta."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://edgecontainer.googleapis.com/'
  MTLS_BASE_URL = 'https://edgecontainer.mtls.googleapis.com/'

  _PACKAGE = 'edgecontainer'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'EdgecontainerV1beta'
  _URL_VERSION = 'v1beta'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new edgecontainer handle."""
    url = url or self.BASE_URL
    super(EdgecontainerV1beta, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_clusters_nodePools = self.ProjectsLocationsClustersNodePoolsService(self)
    self.projects_locations_clusters = self.ProjectsLocationsClustersService(self)
    self.projects_locations_machines = self.ProjectsLocationsMachinesService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_vpnConnections = self.ProjectsLocationsVpnConnectionsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsClustersNodePoolsService(base_api.BaseApiService):
    """Service class for the projects_locations_clusters_nodePools resource."""

    _NAME = 'projects_locations_clusters_nodePools'

    def __init__(self, client):
      super(EdgecontainerV1beta.ProjectsLocationsClustersNodePoolsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new NodePool in a given project and location.

      Args:
        request: (EdgecontainerProjectsLocationsClustersNodePoolsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}/nodePools',
        http_method='POST',
        method_id='edgecontainer.projects.locations.clusters.nodePools.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['nodePoolId', 'requestId'],
        relative_path='v1beta/{+parent}/nodePools',
        request_field='nodePool',
        request_type_name='EdgecontainerProjectsLocationsClustersNodePoolsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single NodePool.

      Args:
        request: (EdgecontainerProjectsLocationsClustersNodePoolsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}/nodePools/{nodePoolsId}',
        http_method='DELETE',
        method_id='edgecontainer.projects.locations.clusters.nodePools.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsClustersNodePoolsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single NodePool.

      Args:
        request: (EdgecontainerProjectsLocationsClustersNodePoolsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (NodePool) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}/nodePools/{nodePoolsId}',
        http_method='GET',
        method_id='edgecontainer.projects.locations.clusters.nodePools.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsClustersNodePoolsGetRequest',
        response_type_name='NodePool',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists NodePools in a given project and location.

      Args:
        request: (EdgecontainerProjectsLocationsClustersNodePoolsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListNodePoolsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}/nodePools',
        http_method='GET',
        method_id='edgecontainer.projects.locations.clusters.nodePools.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta/{+parent}/nodePools',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsClustersNodePoolsListRequest',
        response_type_name='ListNodePoolsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single NodePool.

      Args:
        request: (EdgecontainerProjectsLocationsClustersNodePoolsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}/nodePools/{nodePoolsId}',
        http_method='PATCH',
        method_id='edgecontainer.projects.locations.clusters.nodePools.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1beta/{+name}',
        request_field='nodePool',
        request_type_name='EdgecontainerProjectsLocationsClustersNodePoolsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsClustersService(base_api.BaseApiService):
    """Service class for the projects_locations_clusters resource."""

    _NAME = 'projects_locations_clusters'

    def __init__(self, client):
      super(EdgecontainerV1beta.ProjectsLocationsClustersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Cluster in a given project and location.

      Args:
        request: (EdgecontainerProjectsLocationsClustersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters',
        http_method='POST',
        method_id='edgecontainer.projects.locations.clusters.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['clusterId', 'requestId'],
        relative_path='v1beta/{+parent}/clusters',
        request_field='cluster',
        request_type_name='EdgecontainerProjectsLocationsClustersCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Cluster.

      Args:
        request: (EdgecontainerProjectsLocationsClustersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}',
        http_method='DELETE',
        method_id='edgecontainer.projects.locations.clusters.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsClustersDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def GenerateAccessToken(self, request, global_params=None):
      r"""Generates an access token for a Cluster.

      Args:
        request: (EdgecontainerProjectsLocationsClustersGenerateAccessTokenRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GenerateAccessTokenResponse) The response message.
      """
      config = self.GetMethodConfig('GenerateAccessToken')
      return self._RunMethod(
          config, request, global_params=global_params)

    GenerateAccessToken.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}:generateAccessToken',
        http_method='GET',
        method_id='edgecontainer.projects.locations.clusters.generateAccessToken',
        ordered_params=['cluster'],
        path_params=['cluster'],
        query_params=[],
        relative_path='v1beta/{+cluster}:generateAccessToken',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsClustersGenerateAccessTokenRequest',
        response_type_name='GenerateAccessTokenResponse',
        supports_download=False,
    )

    def GenerateOfflineCredential(self, request, global_params=None):
      r"""Generates an offline credential for a Cluster.

      Args:
        request: (EdgecontainerProjectsLocationsClustersGenerateOfflineCredentialRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GenerateOfflineCredentialResponse) The response message.
      """
      config = self.GetMethodConfig('GenerateOfflineCredential')
      return self._RunMethod(
          config, request, global_params=global_params)

    GenerateOfflineCredential.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}:generateOfflineCredential',
        http_method='GET',
        method_id='edgecontainer.projects.locations.clusters.generateOfflineCredential',
        ordered_params=['cluster'],
        path_params=['cluster'],
        query_params=[],
        relative_path='v1beta/{+cluster}:generateOfflineCredential',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsClustersGenerateOfflineCredentialRequest',
        response_type_name='GenerateOfflineCredentialResponse',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Cluster.

      Args:
        request: (EdgecontainerProjectsLocationsClustersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Cluster) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}',
        http_method='GET',
        method_id='edgecontainer.projects.locations.clusters.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsClustersGetRequest',
        response_type_name='Cluster',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Clusters in a given project and location.

      Args:
        request: (EdgecontainerProjectsLocationsClustersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListClustersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters',
        http_method='GET',
        method_id='edgecontainer.projects.locations.clusters.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta/{+parent}/clusters',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsClustersListRequest',
        response_type_name='ListClustersResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single Cluster.

      Args:
        request: (EdgecontainerProjectsLocationsClustersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}',
        http_method='PATCH',
        method_id='edgecontainer.projects.locations.clusters.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId', 'updateMask'],
        relative_path='v1beta/{+name}',
        request_field='cluster',
        request_type_name='EdgecontainerProjectsLocationsClustersPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Upgrade(self, request, global_params=None):
      r"""Upgrades a single cluster.

      Args:
        request: (EdgecontainerProjectsLocationsClustersUpgradeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Upgrade')
      return self._RunMethod(
          config, request, global_params=global_params)

    Upgrade.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/clusters/{clustersId}:upgrade',
        http_method='POST',
        method_id='edgecontainer.projects.locations.clusters.upgrade',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}:upgrade',
        request_field='upgradeClusterRequest',
        request_type_name='EdgecontainerProjectsLocationsClustersUpgradeRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsMachinesService(base_api.BaseApiService):
    """Service class for the projects_locations_machines resource."""

    _NAME = 'projects_locations_machines'

    def __init__(self, client):
      super(EdgecontainerV1beta.ProjectsLocationsMachinesService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets details of a single Machine.

      Args:
        request: (EdgecontainerProjectsLocationsMachinesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Machine) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/machines/{machinesId}',
        http_method='GET',
        method_id='edgecontainer.projects.locations.machines.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsMachinesGetRequest',
        response_type_name='Machine',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Machines in a given project and location.

      Args:
        request: (EdgecontainerProjectsLocationsMachinesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListMachinesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/machines',
        http_method='GET',
        method_id='edgecontainer.projects.locations.machines.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta/{+parent}/machines',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsMachinesListRequest',
        response_type_name='ListMachinesResponse',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(EdgecontainerV1beta.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of `1`, corresponding to `Code.CANCELLED`.

      Args:
        request: (EdgecontainerProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='edgecontainer.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='EdgecontainerProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (EdgecontainerProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='edgecontainer.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (EdgecontainerProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='edgecontainer.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (EdgecontainerProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='edgecontainer.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta/{+name}/operations',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsVpnConnectionsService(base_api.BaseApiService):
    """Service class for the projects_locations_vpnConnections resource."""

    _NAME = 'projects_locations_vpnConnections'

    def __init__(self, client):
      super(EdgecontainerV1beta.ProjectsLocationsVpnConnectionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new VPN connection in a given project and location.

      Args:
        request: (EdgecontainerProjectsLocationsVpnConnectionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/vpnConnections',
        http_method='POST',
        method_id='edgecontainer.projects.locations.vpnConnections.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['requestId', 'vpnConnectionId'],
        relative_path='v1beta/{+parent}/vpnConnections',
        request_field='vpnConnection',
        request_type_name='EdgecontainerProjectsLocationsVpnConnectionsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single VPN connection.

      Args:
        request: (EdgecontainerProjectsLocationsVpnConnectionsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/vpnConnections/{vpnConnectionsId}',
        http_method='DELETE',
        method_id='edgecontainer.projects.locations.vpnConnections.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['requestId'],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsVpnConnectionsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single VPN connection.

      Args:
        request: (EdgecontainerProjectsLocationsVpnConnectionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (VpnConnection) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/vpnConnections/{vpnConnectionsId}',
        http_method='GET',
        method_id='edgecontainer.projects.locations.vpnConnections.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsVpnConnectionsGetRequest',
        response_type_name='VpnConnection',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists VPN connections in a given project and location.

      Args:
        request: (EdgecontainerProjectsLocationsVpnConnectionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListVpnConnectionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/vpnConnections',
        http_method='GET',
        method_id='edgecontainer.projects.locations.vpnConnections.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1beta/{+parent}/vpnConnections',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsVpnConnectionsListRequest',
        response_type_name='ListVpnConnectionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(EdgecontainerV1beta.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (EdgecontainerProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='edgecontainer.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def GetServerConfig(self, request, global_params=None):
      r"""Gets the server config.

      Args:
        request: (EdgecontainerProjectsLocationsGetServerConfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServerConfig) The response message.
      """
      config = self.GetMethodConfig('GetServerConfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetServerConfig.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations/{locationsId}/serverConfig',
        http_method='GET',
        method_id='edgecontainer.projects.locations.getServerConfig',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}/serverConfig',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsGetServerConfigRequest',
        response_type_name='ServerConfig',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (EdgecontainerProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/projects/{projectsId}/locations',
        http_method='GET',
        method_id='edgecontainer.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'includeUnrevealedLocations', 'pageSize', 'pageToken'],
        relative_path='v1beta/{+name}/locations',
        request_field='',
        request_type_name='EdgecontainerProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(EdgecontainerV1beta.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
