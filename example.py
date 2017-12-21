import os
import sys

from PySide import QtGui, QtCore

# load in the example nodes.
from BlueprintNodeGraph import nodes
# import the widgets.
from BlueprintNodeGraph.interfaces import NodeGraph, Node


class MyNode(Node):

    NODE_NAME = 'my test node'
    NODE_TYPE = 'MyNode'

    def __init__(self):
        super(MyNode, self).__init__()
        self.add_input('in')
        self.add_input('out')


class MyNodeGraph(NodeGraph):

    def __init__(self, parent=None):
        super(MyNodeGraph, self).__init__(parent)
        self.setWindowTitle('My Node Graph')
        self.resize(1100, 800)

    def keyPressEvent(self, event):
        key = event.key()
        if key == QtCore.Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    # create node graph.
    graph = MyNodeGraph()
    graph.show()

    # add a node.
    my_node = MyNode()
    graph.add_node(my_node)

    # create the nodes from the "nodes" package dir.
    foo_node = graph.create_node('BlueprintNodeGraph.nodes.foo.FooNode', name='Foo Node')
    bar_node = graph.create_node('BlueprintNodeGraph.nodes.bar.BarNode', name='Foo Node')
    text_node = graph.create_node('BlueprintNodeGraph.nodes.widget_nodes.TextInputNode', name='Text Node')
    menu_node = graph.create_node('BlueprintNodeGraph.nodes.widget_nodes.DropdownMenuNode', name='Menu Node')

    # change the color on "foo_node"
    foo_node.set_color(17, 52, 88)

    # change icon on "bar_node"
    this_path = os.path.dirname(os.path.abspath(__file__))
    icon = os.path.join(this_path, 'example_icon.png')
    bar_node.set_icon(icon)

    # position nodes.
    foo_node.set_pos(-487.0, 141.0)
    bar_node.set_pos(-77.0, 17.0)
    text_node.set_pos(-488.0, -158.0)
    menu_node.set_pos(310.0, -97.0)

    # connect nodes
    foo_node.set_output(0, bar_node.input(2))
    menu_node.set_input(0, bar_node.output(1))
    bar_node.set_input(0, text_node.output(0))

    app.exec_()
