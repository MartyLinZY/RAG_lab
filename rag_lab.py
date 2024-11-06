import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))


from IPython.display import Markdown, display
import torch
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.core.prompts import PromptTemplate
from modelscope import snapshot_download
from llama_index.core.base.embeddings.base import BaseEmbedding, Embedding
from abc import ABC
from typing import Any, List, Optional, Dict, cast
from llama_index.core import (
    VectorStoreIndex,
    ServiceContext,
    set_global_service_context,
    SimpleDirectoryReader,
)
