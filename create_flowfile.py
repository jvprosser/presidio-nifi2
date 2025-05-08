from nifiapi.flowfilesource import FlowFileSource, FlowFileSourceResult

class CreateFlowFile(FlowFileSource):
    class Java:
        implements = ['org.apache.nifi.python.processor.FlowFileSource']

    class ProcessorDetails:
        version = '0.0.1-SNAPSHOT'
        description = '''A Python processor that creates FlowFiles.'''

    def __init__(self, **kwargs):
        pass

    def create(self, context):
        return FlowFileSourceResult(relationship = 'success', attributes = {'Greeting': 'Hello'}, contents = 'HELLO WORLD!')
      



class CreateFlowFile(FlowFileSource):
    class Java:
        implements = ['org.apache.nifi.python.processor.FlowFileSource']

    class ProcessorDetails:
        version = '0.0.1-SNAPSHOT'
        description = '''A Python processor that creates FlowFiles.'''

    def __init__(self, **kwargs):
        pass

    def create(self, context):
        return FlowFileSourceResult(relationship = 'success', attributes = {'Greeting': 'Hello'}, contents = 'HELLO WORLD!')
      

from nifiapi.flowfiletransform import (
    FlowFileTransform,
    FlowFileTransformResult
)
from nifiapi.relationship import Relationship
from nifiapi.properties import (
    ProcessContext,
    PropertyDescriptor
)
from typing import List


class NERProcessor(FlowFileTransform):

    class Java:
        implements = ['org.apache.nifi.python.processor.FlowFileTransform']

    class ProcessorDetails:
        version = '0.0.1-SNAPSHOT'
        description = '''
        '''
        tags = []
        dependencies = []

    def __init__(self, *args, **kwargs):
        super().__init__()

    def getRelationships(self) -> List[Relationship]:
        '''
        Register any additional relationships.

        Returns:
            list(Relationship)
        '''
        return []

    def getPropertyDescriptors(self) -> List[PropertyDescriptor]:
        '''
        Register property descriptor required to successfully run the
        processor.

        Returns:
            list(PropertyDescriptor)
        '''
    

