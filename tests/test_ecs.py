import unittest
from troposphere import Ref
import troposphere.ecs as ecs
from troposphere import iam


class TestECS(unittest.TestCase):

    def test_allow_string_cluster(self):
        task_definition = ecs.TaskDefinition(
            "mytaskdef",
            ContainerDefinitions=[
                ecs.ContainerDefinition(
                    Image="myimage",
                    Memory="300",
                    Name="mycontainer",
                )
            ],
            Volumes=[
                ecs.Volume(Name="my-vol"),
            ],
        )
        ecs_service = ecs.Service(
            'Service',
            Cluster='cluster',
            DesiredCount=2,
            TaskDefinition=Ref(task_definition),
        )

        ecs_service.JSONrepr()

    def test_allow_ref_cluster(self):
        task_definition = ecs.TaskDefinition(
            "mytaskdef",
            ContainerDefinitions=[
                ecs.ContainerDefinition(
                    Image="myimage",
                    Memory="300",
                    Name="mycontainer",
                )
            ],
            Volumes=[
                ecs.Volume(Name="my-vol"),
            ],
        )
        cluster = ecs.Cluster("mycluster")
        ecs_service = ecs.Service(
            'Service',
            Cluster=Ref(cluster),
            DesiredCount=2,
            TaskDefinition=Ref(task_definition),
        )

        ecs_service.JSONrepr()

    def test_task_role_arn_is_optional(self):
        task_definition = ecs.TaskDefinition(
            "mytaskdef",
            ContainerDefinitions=[
                ecs.ContainerDefinition(
                    Image="myimage",
                    Memory="300",
                    Name="mycontainer",
                )
            ],
        )

        task_definition.JSONrepr()

    def test_allow_string_task_role_arn(self):
        task_definition = ecs.TaskDefinition(
            "mytaskdef",
            ContainerDefinitions=[
                ecs.ContainerDefinition(
                    Image="myimage",
                    Memory="300",
                    Name="mycontainer",
                )
            ],
            TaskRoleArn="myiamrole"
        )

        task_definition.JSONrepr()

    def test_allow_ref_task_role_arn(self):
        task_definition = ecs.TaskDefinition(
            "mytaskdef",
            ContainerDefinitions=[
                ecs.ContainerDefinition(
                    Image="myimage",
                    Memory="300",
                    Name="mycontainer",
                )
            ],
            TaskRoleArn=Ref(iam.Role("myRole"))
        )

        task_definition.JSONrepr()

    def test_allow_port_mapping_protocol(self):
        container_definition = ecs.ContainerDefinition(
            Image="myimage",
            Memory="300",
            Name="mycontainer",
            PortMappings=[
                ecs.PortMapping(
                    ContainerPort=8125, HostPort=8125, Protocol="udp"
                )
            ]
        )

        container_definition.JSONrepr()

    def test_port_mapping_does_not_require_protocol(self):
        container_definition = ecs.ContainerDefinition(
            Image="myimage",
            Memory="300",
            Name="mycontainer",
            PortMappings=[
                ecs.PortMapping(
                    ContainerPort=8125, HostPort=8125,
                )
            ]
        )

        container_definition.JSONrepr()

    def test_allow_host_network_mode(self):
        container_definition = ecs.ContainerDefinition(
            Image="myimage",
            Memory="300",
            Name="mycontainer",
            NetworkMode="host"
        )

        container_definition.JSONrepr()
