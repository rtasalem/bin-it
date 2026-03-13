from unittest.mock import MagicMock
from mongo.create_index import create_index


def test_creates_index_with_default_params(mocker, capsys):
  mocker.patch("mongo.create_index.database")
  collection = MagicMock()
  params = [("data.date", 1)]
  index_name = "date_index"

  create_index(collection, params, index_name)

  collection.create_index.assert_called_once_with(
    params,
    unique=False,
    name=index_name
  )
  output = capsys.readouterr().out
  assert f"🍃 MongoDB index has been created: {index_name}" in output


def test_creates_index_with_unique_true(mocker):
  mocker.patch("mongo.create_index.database")
  collection = MagicMock()
  params = [("data.bin_colours", 1)]
  index_name = "bin_colours_index"

  create_index(collection, params, index_name, unique=True)

  collection.create_index.assert_called_once_with(
    params,
    unique=True,
    name=index_name
  )


def test_prints_confirmation_message(mocker, capsys):
  mocker.patch("mongo.create_index.database")
  collection = MagicMock()
  params = [("data.date", 1)]
  index_name = "test_index"

  create_index(collection, params, index_name)

  output = capsys.readouterr().out
  assert output.strip() == "🍃 MongoDB index has been created: test_index"
