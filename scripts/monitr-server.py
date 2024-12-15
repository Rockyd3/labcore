from datetime import datetime
from pathlib import Path

import panel as pn
pn.extension()
pn.extension('floatpanel')

from labcore.analysis.hvapps import DataSelect, DDH5LoaderNode, LoaderNodeManager

ds = DataSelect('.')
loader = DDH5LoaderNode()
Loader_nodes = [loader, DDH5LoaderNode()]
load_multiple = LoaderNodeManager(Loader_nodes)

def data_selected_cb(*events):
    # loader.file_path = events[0].new
    for i, l in enumerate(Loader_nodes):
        l.file_path = events[0].new

watch_data_selected = ds.param.watch(data_selected_cb, ['selected_path'])


def refilter_data_select(*events):
    ds.data_select()

search_data_typed = ds.param.watch(refilter_data_select, ['search_term'])


pn.template.BootstrapTemplate(
    site="labcore",
    title="data explorer",
    sidebar=[],
    main=[ds, load_multiple],
).servable()
