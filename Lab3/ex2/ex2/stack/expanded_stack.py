from stack import Stack


class ExpandedStack(Stack):

    def min_value(self):
        print(f'Minimalna wartość w stosie to: {min(self._Stack__m_buffer)}')
