
def test_tmpdir(tmpdir):
    a_file = tmpdir.join('something.txt')
    a_sub_dir = tmpdir.mkdir("anything")
    another_file = a_sub_dir.join('something_else.txt')
    a_file.write("a file write something")
    another_file.write("another file write something")
    assert a_file.read() == "a file write something"
    assert another_file.read() == "another file write something"


def test_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp("mydir")

    base_tmp = tmpdir_factory.getbasetemp()
    print('base: ', base_tmp)

    a_file = a_dir.join('something.txt')
    a_sub_dir = a_dir.mkdir("anything")
    another_file = a_sub_dir.join('something_else.txt')
    a_file.write("a file write something")
    another_file.write("another file write something")
    assert a_file.read() == "a file write something"
    assert another_file.read() == "another file write something"