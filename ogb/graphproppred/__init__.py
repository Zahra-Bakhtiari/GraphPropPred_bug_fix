from .evaluate import Evaluator
from .dataset import GraphPropPredDataset
import logging
logger = logging.getLogger(__name__)

try:
    from .dataset_pyg import PygGraphPropPredDataset
except Exception as e:
    logger.info(f'Exception: {e}')
    pass

try:
    from .dataset_dgl import DglGraphPropPredDataset
    from .dataset_dgl import collate_dgl
except Exception as e:
    logger.info(f'Exception: {e}')
    pass


