import pathlib

from pytest import fixture

from asic.files.definitions.curt import CURT

from .conftest import ALL_FILES, TESTFILES


@fixture
def curt_remote_path():
    curt_path = ALL_FILES["curt"]["path"]
    path = pathlib.PureWindowsPath(curt_path)
    return path


@fixture
def curt_file(curt_remote_path):
    path = curt_remote_path
    file = CURT.from_remote_path(path)
    return file


@fixture
def local_curt_file(curt_file: CURT, datafiles: pathlib.Path) -> pathlib.Path:
    relative_path = curt_file.path.relative_to(curt_file.path.anchor)
    local_file = datafiles / relative_path
    assert local_file.is_file()
    return local_file


@TESTFILES
def test_curt_read(curt_file: CURT, local_curt_file):
    data = curt_file.read(local_curt_file)
    print(len(data))
    assert len(data) == 189


@TESTFILES
def test_curt_preprocess(curt_file: CURT, local_curt_file):
    long_data = curt_file.preprocess(local_curt_file)
    print(len(long_data))
    assert len(long_data) == 4536
