class FlatIterator:

    def __init__(self, list_of_list):
        self.ext_iter = iter(list_of_list)

    def __iter__(self):
        self.curr_iter = iter(next(self.ext_iter))
        return self

    def __next__(self):
        try:
            item = next(self.curr_iter)
        except StopIteration:
            try:
                self.curr_iter = iter(next(self.ext_iter))
                item = next(self.curr_iter)
            except StopIteration:
                raise StopIteration
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()